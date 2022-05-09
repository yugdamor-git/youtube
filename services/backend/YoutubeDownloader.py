from pathlib import Path
import os
from slugify import slugify
from redisHandler import redisHandler
import math
import yt_dlp
import requests
import hashlib

class YoutubeDownloader:
    def __init__(self):
        print(f'Youtube Downloader init')
        
        self.cwd = Path.cwd()
        
        self.mediaDir = self.cwd.joinpath("media")
        
        self.host = f'http://{os.environ.get("IP")}:1337/media/'
        
        self.redis = redisHandler()
        
        self.image_resolutions = {
        'HD Image (1280x720)':'https://img.youtube.com/vi/{id}/maxresdefault.jpg',
        'SD Image (640x480)': 'https://img.youtube.com/vi/{id}/sddefault.jpg',
        'Normal Image (480x360)': 'https://img.youtube.com/vi/{id}/hqdefault.jpg',
        'Normal Image (320x180)': 'https://img.youtube.com/vi/{id}/mqdefault.jpg',
        'Small Image (120x90)': 'https://img.youtube.com/vi/{id}/default.jpg'
        }
        
        
        
        if not self.mediaDir.exists():
            self.mediaDir.mkdir()
        
    
    def fetchInfo(self,youtubeUrl):
        
        key = self.generateHash(youtubeUrl)
        
        info = self.redis.get(key)
        
        if info != None:
            info["fromCache"] = True
            return info
        
        options = {
            'continue_dl': False,
            'skip_download': True,
            'noplaylist': True,
        }
        
        ydl = yt_dlp.YoutubeDL(options)
        
        info = ydl.extract_info(youtubeUrl, download=False)
        
        data = {
        'id': info['id'],
        'key':key,
        'url':youtubeUrl,
        'title': info["fulltitle"],
        'titleSlug':slugify(info["fulltitle"]),
        "thumbnail": info["thumbnail"],
        "duration": info["duration"],
        "audio_formats": self.extractAudioResolutions(info),
        "video_formats":self.extractVideoResolutions(info)
        }
        
        self.redis.set(key,data)
        
        data["fromCache"] = False
        
        
        
        return data
    
    def convert_size(self,size_bytes):
        if size_bytes == 0:
            return {
                "filesize":0,
                "filesizeLabel":"0B",
                "unit":"B"
                }
        
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        
        return {
            "filesize":s,
            "filesizeLabel":f'{s} {size_name[i]}',
            "unit":size_name[i]
        }
    
    def extractFileSize(self,res):
        filesize = res.get("filesize",None)
        if filesize == None:
            filesize = res.get("filesize_approx",None)
        
        if filesize == None:
            return {
                "filesize":None,
                "filesizeLabel":None
            }
        else:
            return self.convert_size(int(float(filesize)))
    def generateHash(self,value):
        sha1 = hashlib.sha1()
        sha1.update(str(value).encode("utf-8"))
        return sha1.hexdigest()
        
    
    def extractVideoResolutions(self,info):
        
        duration = info["duration"]
        
        availableResolutions = {}
        
        try:
            directDownloadResolutions = [res for res in info['formats'] if res["vcodec"] != "none" and res['acodec'] != 'none' and res["ext"] =="mp4"]

            for res in directDownloadResolutions:
                height = int(res["format_note"].replace("p","").strip())
                tmp = {}
                tmp["quality"] = height
                tmp["url"] = res["url"]
                tmp.update(self.extractFileSize(res))
                
                if height not in availableResolutions:
                    availableResolutions[height]= tmp
            
            directDownloadResolutions = [res for res in info['formats'] if res["vcodec"] != "none" and res["acodec"] != None]

            for res in directDownloadResolutions:
                height = int(res["format_note"].replace("p","").strip())
                tmp = {}
                tmp["quality"] = height
                tmp["url"] = None
                tmp.update(self.extractFileSize(res))
                
                if height not in availableResolutions:
                    if height > 720:
                        if duration > 30 * 60:
                            continue
                    availableResolutions[height]= tmp
                    
        except Exception as e:
            print(f'error -> {str(e)}')
        
        tmp = dict(sorted(availableResolutions.items(),reverse=True))
        final = []
        for item in tmp.items():
            final.append(item[1])
        
        return final
    
    def extractAudioResolutions(self,info):
        availableBitrates = {}
        
        try:
            bitrates = [res for res in info['formats'] if "abr" in res and res["abr"] != "none" and res['abr'] != 0]

            for bitrate in bitrates:
                abr = int(bitrate["abr"])
                tmp = {}
                tmp["quality"] = abr
                tmp["url"] = bitrate["url"]
                tmp["label"] = bitrate["format"]
                tmp.update(self.extractFileSize(bitrate))
                
                if abr not in availableBitrates:
                    availableBitrates[abr] = tmp
        except Exception as e:
            print(f'error -> {str(e)}')
        
        tmp = dict(sorted(availableBitrates.items(),reverse=True))
        final = []
        for item in tmp.items():
            final.append(item[1])
        
        return final
    
    def downloadVideo(self,key,quality):
        
        data = self.redis.get(key)
        
        fileName = f'{data["id"]}/ytshorts-savetube-{data["titleSlug"]}-{quality}.mp4'
        
        if self.mediaDir.joinpath(fileName).exists() == True:
            return {
            "downloadUrl":f'{self.host}{fileName}',
            "downloaded":False
        }
        
        ydl_opts = {
        'format': f'bestvideo[height<={quality}][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'media/%(id)s/ytshorts-savetube-{data["titleSlug"]}-{quality}.%(ext)s',
        'noplaylist': True,
        'quiet': True,
        'verbose': False
        
        }
        
        ydl = yt_dlp.YoutubeDL(ydl_opts)
        
        ydl.download(data["url"])
        
        return {
            "downloadUrl":f'{self.host}{fileName}',
             "downloaded":True
        }
    
    def downloadAudio(self,key,quality):
        
        data = self.redis.get(key)
        
        fileName = f'{data["id"]}/ytshorts-savetube-{data["titleSlug"]}-{quality}.mp3'
        
        if self.mediaDir.joinpath(fileName).exists() == True:
            return {
            "downloadUrl":f'{self.host}{fileName}',
            "downloaded":False
        }
        
        ydl_opts = {
                'format': 'bestaudio',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': str(quality),
                }],
                'outtmpl': f'media/%(id)s/ytshorts-savetube-{data["titleSlug"]}-{quality}.%(ext)s',
                'noplaylist': True,
                'quiet': True,
                'verbose': False
                
                }
        
        ydl = yt_dlp.YoutubeDL(ydl_opts)
        
        ydl.download(data["url"])
        
        return {
            "downloadUrl":f'{self.host}{fileName}',
             "downloaded":True
        }
    
    def downloadThumbnail(self,youtubeUrl):
        
        data = self.fetchInfo(youtubeUrl)
        
        thumbnails = []
        
        folder = self.mediaDir.joinpath(data["id"])
        
        if not folder.exists():
            folder.mkdir()
        
        for resolution in self.image_resolutions:
            r = requests.get(self.image_resolutions[resolution].format(id=data['id']))
            
            fileName = f'{data["id"]}/ytshorts-savetube-{data["titleSlug"]}-{slugify(resolution)}.jpg'
            
            filePath = self.mediaDir.joinpath(fileName)
            
            if filePath.exists() == True:
                thumbnails.append({
                    "label":resolution,
                    "downloadUrl":f'{self.host}{fileName}'
                })
                
                continue
            
            f = open(filePath, 'wb')
            
            for chunk in r.iter_content(chunk_size=512 * 1024): 
                if chunk: 
                    f.write(chunk)
            f.close()
            
            thumbnails.append({
                    "label":resolution,
                    "downloadUrl":f'{self.host}{fileName}'
                })
            
        return thumbnails