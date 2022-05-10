
from flask import Flask, jsonify,send_from_directory,request
import os
from pathlib import Path
from YoutubeDownloader import YoutubeDownloader
from flask_cors import CORS
import time
import datetime
from json import JSONEncoder

import json

from LogManager import LogManager

lm = LogManager()

yd = YoutubeDownloader()

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"Access-Control-Allow-Origin": "*"}})


class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()


@app.route("/")
def hello_world():
    return jsonify(
        ip=os.environ.get("IP")
    )
    
    
@app.route("/info",methods=["GET"])
def info():
    
    url = request.args.get("url",None)
    
    if url == None:
        return jsonify({
            "status":False,
            "message":"url is missing...",
            "data":None
        })
    
    info = yd.fetchInfo(url)
    
    lm.increaseRequestCount("fetch-request")
    
    return jsonify({
            "status":True,
            "message":"200",
            "data":info
        })

@app.route("/redis",methods=["GET"])
def redis():
    key = request.args.get("key",None)
    
    if key == None:
        return jsonify({
            "status":False,
            "message":"key is missing...",
            "data":None
        })
    
    info = yd.redis.get(key)
    
    return jsonify({
            "status":True,
            "message":"200",
            "data":info
        })


@app.route("/download/<downloadType>/<quality>/<key>",methods=["GET"])
def download(downloadType,quality,key):
    
    if key == None or quality == None or downloadType == None:
        return jsonify({
            "status":False,
            "message":"id,key or quality is missing...",
            "data":None
        })
    
    if downloadType == "video":
        info = yd.downloadVideo(key,quality)
    elif downloadType == "audio":
        info = yd.downloadAudio(key,quality)
    else:
        info = None
    
    lm.increaseResolutionCount(f'{downloadType}-{quality}')
    
    lm.increaseRequestCount("download-server-request")
    
    return jsonify({
            "status":True,
            "message":"200",
            "data":info
        })



@app.route("/download/thumbnail",methods=["GET"])
def downloadThumbnail():
    
    url = request.args.get("url",None)
    
    if url == None:
        return jsonify({
            "status":False,
            "message":"url is missing...",
            "data":None
        })
    
    info = yd.downloadThumbnail(url) 
    time.sleep(1)
    lm.increaseRequestCount("download-thumbnail-request")
    return jsonify({
            "status":True,
            "message":"200",
            "data":info
        })
    
    
@app.route('/stats')
def stats():
    
    storage = list(lm.database.storage.find({},{'_id': False}).sort("updatedAt",-1).limit(20))
    
    requestCount = list(lm.database.requestCount.find({},{'_id': False}).sort("updatedAt",-1).limit(20))
    
    resolutionCount = list(lm.database.resolutionCount.find({},{'_id': False}).sort("updatedAt",-1).limit(20))
    
    data = {
        "storage":storage,
        "requestCount":requestCount,
        "resolutionCount":resolutionCount
    }
    
    return f'<html><body><pre><code>{json.dumps(data,indent=2,cls=DateTimeEncoder)}</code></pre></body></html>'

@app.route('/media/<folderName>/<fileName>')
def download_file(folderName,fileName):
    
    lm.increaseRequestCount("download-client-request")
    
    return send_from_directory(f'/usr/src/app/media/{folderName}',fileName, as_attachment=True)