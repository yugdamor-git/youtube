
from flask import Flask, jsonify,send_from_directory,request
import os
from pathlib import Path
from YoutubeDownloader import YoutubeDownloader

yd = YoutubeDownloader()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify(
        ip=os.environ.get("IP")
    )
    
@app.route("/info",methods=["POST"])
def info():
    
    data = request.json
    
    url = data.get("url",None)
    
    if url == None:
        return jsonify({
            "status":False,
            "message":"url is missing...",
            "data":None
        })
    
    info = yd.fetchInfo(url)
    
    return jsonify({
            "status":True,
            "message":"200",
            "data":info
        })

@app.route("/redis",methods=["POST"])
def redis():
    
    data = request.json
    
    key = data.get("key",None)
    
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
    
    return jsonify({
            "status":True,
            "message":"200",
            "data":info
        })


@app.route("/thumbnail",methods=["POST"])
def downloadThumbnail():
    
    jsonData = request.json
    
    url = jsonData.get("url")
    
    if url == None:
        return jsonify({
            "status":False,
            "message":"url is missing...",
            "data":None
        })
    
    info = yd.downloadThumbnail(url) 
    
    return jsonify({
            "status":True,
            "message":"200",
            "data":info
        })


@app.route('/media/<folderName>/<fileName>')
def download_file(folderName,fileName):
    return send_from_directory(f'/usr/src/app/media/{folderName}',fileName, as_attachment=True)