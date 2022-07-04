
from flask import Flask, jsonify,send_from_directory,request,redirect
import os
from pathlib import Path
from YoutubeDownloader import YoutubeDownloader
from flask_cors import CORS
import time
import datetime
from json import JSONEncoder

import traceback

import json

from LogManager import LogManager

import shutil

lm = LogManager()

yd = YoutubeDownloader()

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"Access-Control-Allow-Origin": "*"}})


class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()



@app.route("/alert/ping")
def ping():
    return jsonify(
        dns=os.environ.get("IP"),
        status=True
    )

@app.route("/alert/space")
def space():
    
    default_alert_percentage = 90
    
    alert_percentage = int(request.args.get("alert_percentage",default_alert_percentage))
        
    
    usage = shutil.disk_usage("/")
    
    total = round(usage.total/(1024 * 1024 * 1024),2)
    used = round(usage.used/(1024 * 1024 * 1024),2)
    free = round(usage.free/(1024 * 1024 * 1024),2)
    
    send_alert = False
    alert_message = ""
    percentage_used = round((used * 100)/total)
    
    if percentage_used > alert_percentage:
        send_alert = True
    
    dns = os.environ.get("IP")
    
    alert_message = f'{percentage_used}% space is used on server -> {dns}. please disable server in google sheet to stop receiving further emails regarding this.'
    
    return jsonify(
        dns=dns,
        total=total,
        used=used,
        free=free,
        send_alert=send_alert,
        percentage_used=percentage_used,
        alert_message=alert_message
    )

@app.route("/alert/yt-dlp/status")
def yt_dlp_status():
    try:
        fetch_duration = None
        download_duration = None
        
        url = request.args.get("url")
        t1 = datetime.datetime.now()
        info = yd.fetchInfo(url)
        t2 = datetime.datetime.now()
        
        fetch_duration = (t2 - t1).seconds
        
        key = info["key"]
        quality = info["video_formats"][1]["quality"]
        
        t1 = datetime.datetime.now()
        info = yd.downloadVideo(key,quality)
        t2 = datetime.datetime.now()
        
        download_url = info["downloadUrl"]
        
        download_duration = (t2 - t1).seconds
        
        status = True
        
        if "message" in info:
            if "error" in info["message"]:
                status = False
        
        return jsonify({
            
            "status":status,
            "data":{
                "fetch_duration":fetch_duration,
                "download_duration":download_duration,
                "download_url":download_url
            }
        })
    except Exception as e:
        return jsonify({
            "status":False,
            "message":f'error : {str(e)}'
        })



@app.route("/")
def hello_world():
    return jsonify(
        ip=os.environ.get("IP")
    )
    
    
@app.route("/info",methods=["GET"])
def info():
    try:
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
        
    except Exception as e:
        error  = traceback.format_exc()
        tmp = {}
        tmp["url"] = url
        tmp["type"] = "fetch-video-info"
        tmp["message"] = str(error)
        lm.insertErrorLog(tmp)
        
        return jsonify({
                "status":False,
                "message":format_error_message(str(e)),
                "data":None
            })


def format_error_message(message):
    error_msg = ""
    
    try:
        tmp = str(message).split(": ")
        
        if len(tmp) == 1:
            error_msg = "ERROR Please check the video url and try downloading the video again."
        elif len(tmp) < 3:
            error_msg = " ".join(tmp)[:150]
        else:
            error_msg = " ".join(tmp[:3])[:150]
        return error_msg
    except:
        return "ERROR Please check the video url and try downloading the video again."


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
    try:
        if key == None or quality == None or downloadType == None:
            return jsonify({
                "status":False,
                "message":"id,key or quality is missing...",
                "data":None
            })
        message = "200"
        info = None
        
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
                "message":message,
                "data":info
            })
    
    except Exception as e:
        error  = traceback.format_exc()
        tmp = {}
        tmp["url"] = {
            "downloadType":downloadType,
            "quality":quality,
            "key":key
        }
        tmp["type"] = "fetch-download-video-url"
        tmp["message"] = str(error)
        lm.insertErrorLog(tmp)
        
        return jsonify({
                "status":False,
                "message":format_error_message(str(e)),
                "data":None
            })


@app.route("/download/thumbnail",methods=["GET"])
def downloadThumbnail():
    try:
        url = request.args.get("url",None)
        
        if url == None:
            return jsonify({
                "status":False,
                "message":"url is missing...",
                "data":None
            })
        
        info = yd.downloadThumbnailMultiThread(url)
        
        lm.increaseRequestCount("download-thumbnail-request")
        return jsonify({
                "status":True,
                "message":"200",
                "data":info
            })
        
    except Exception as e:
        error  = traceback.format_exc()
        tmp = {}
        tmp["type"] = "download-thumbnail"
        tmp["url"] = url
        tmp["message"] = str(error)
        lm.insertErrorLog(tmp)
        
        return jsonify({
                "status":False,
                "message":format_error_message(str(e)),
                "data":None
            })
    
    
@app.route('/stats')
def stats():
    currentTime = datetime.datetime.now()
        
    today = currentTime.strftime("%d-%m-%Y")
    
    storage = list(lm.database.storage.find({"timestamp":today},{'_id': False}).sort("updatedAt",-1).limit(20))
    
    requestCount = list(lm.database.requestCount.find({},{'_id': False}).sort("updatedAt",-1).limit(20))
    
    resolutionCount = list(lm.database.resolutionCount.find({"server":"all"},{'_id': False}).sort("updatedAt",-1).limit(20))
    
    data = {
        "storage":storage,
        "requestCount":requestCount,
        "resolutionCount":resolutionCount
    }
    
    return f'<html><body><pre><code>{json.dumps(data,indent=2,cls=DateTimeEncoder)}</code></pre></body></html>'

@app.route('/media/<folderName>/<fileName>')
def download_file(folderName,fileName):
    try:
        
        lm.increaseRequestCount("download-client-request")
        
        return send_from_directory(f'/usr/src/app/media/{folderName}',fileName, as_attachment=True)
    except Exception as e:
        error  =traceback.format_exc()
        tmp = {}
        tmp["url"] = {
            "folderName":folderName,
            "fileName":folderName
        }
        tmp["type"] = "download-video-file"
        tmp["message"] = str(error)
        lm.insertErrorLog(tmp)
        
        return redirect("https://ytshorts.savetube.me")