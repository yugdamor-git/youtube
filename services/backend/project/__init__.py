
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


@app.route("/download",methods=["POST"])
def download():
    
    data = request.json
    
    id = data.get("id",None)
    
    quality = data.get("quality",None)
    
    if id == None or quality == None:
        return jsonify({
            "status":False,
            "message":"id or quality is missing...",
            "data":None
        })
    
    info = yd.downloadVideo(id,quality)
    
    return jsonify({
            "status":True,
            "message":"200",
            "data":info
        })


@app.route('/media/<folderName>/<fileName>')
def download_file(folderName,fileName):
    print(f'folderName : {folderName}')
    print(f'fileName : {fileName}')
    return send_from_directory(f'/usr/src/app/media/{folderName}',fileName, as_attachment=True)