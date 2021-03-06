from pathlib import Path
import os
from slugify import slugify
from redisHandler import redisHandler
import math
import yt_dlp
import requests
import hashlib
import random
from concurrent.futures import ThreadPoolExecutor,as_completed

class YoutubeDownloader:
    def __init__(self):
        print(f'Youtube Downloader init')
        
        self.cwd = Path.cwd()
        
        self.mediaDir = self.cwd.joinpath("media")
        
        self.host = f'https://{os.environ.get("IP")}/media/'
        
        self.redis = redisHandler()
        
        self.image_resolutions = {
        'HD Image (1280x720)':'https://img.youtube.com/vi/{id}/maxresdefault.jpg',
        'SD Image (640x480)': 'https://img.youtube.com/vi/{id}/sddefault.jpg',
        'Normal Image (480x360)': 'https://img.youtube.com/vi/{id}/hqdefault.jpg',
        'Normal Image (320x180)': 'https://img.youtube.com/vi/{id}/mqdefault.jpg',
        'Small Image (120x90)': 'https://img.youtube.com/vi/{id}/default.jpg'
        }
        
        
        self.resolutionMap = {
            "144p":{
                "height":256,
                "width":144,
            },
            "240p":{
                "height":352,
                "width":240
            },
            "360p":{
                "height":640,
                "width":360
            },
            "480p":{
                "height":640,
                "width":480
            },
            "720p":{
                "height":1280,
                "width":720
            },
            "1080p":{
                "height":1920,
                "width":1080
            },
            "1440p":{
                "height":2560,
                "width":1440
            },
            "2160p":{
                "height":3840,
                "width":2160
            },
            "4320p":{
                "height":7680,
                "width":4320
            }
        }
        
        
        
        if not self.mediaDir.exists():
            self.mediaDir.mkdir()
        
    def formatDuration(self,duration):
        try:
            d = int(duration)
            if d < 60:
                return f'{duration} sec'
            else:
                return f'{round(duration/60,2)} min'
        except:
            return f'NA'
        
    def reformatShortsUrl(self,url):
        if "/shorts/" in url:
            id = url.split("/shorts/")[-1].split("?")[0]
            return f'https://www.youtube.com/watch?v={id}'
        else:
            return url
            
    def fetchInfo(self,ytUrl):
        
        youtubeUrl = self.reformatShortsUrl(ytUrl)
        
        key = self.generateHash(youtubeUrl)
        
        info = self.redis.get(key)
        
        if info != None:
            info["fromCache"] = True
            return info
        
        options = {
            'continue_dl': False,
            'skip_download': True,
            'noplaylist': True,
            'cookiefile':f'{os.environ.get("IP").split(".")[0]}--{random.randint(0,1)}.txt'
            
        }
        
        ydl = yt_dlp.YoutubeDL(options)
        
        info = ydl.extract_info(youtubeUrl, download=False)
        
        title = "NA"
        
        if "title" in info:
            title = info["title"]
        elif "fulltitle" in info:
            title = info["fulltitle"]
        
        thumbnail = None
        
        if "thumbnail" in info:
            thumbnail = info["thumbnail"]
        elif "thumbnails" in info:
            if len(info["thumbnails"]) > 0:
                thumbnail = info["thumbnails"][0]
        default_selected = None
        video_formats = self.extractVideoResolutions(info)
        
        for f in video_formats:
            if f["url"] != None:
                default_selected = f["height"]
                tmp_copy = f.copy()
                tmp_copy["label"] = "MP4 video"
                tmp_copy["default_selected"] = 1
                video_formats.insert(0,tmp_copy)
                break
        
        data = {
        'id': info['id'],
        'key':key,
        'url':youtubeUrl,
        'title': title,
        'titleSlug':slugify(title),
        "thumbnail": thumbnail,
        "duration": info["duration"],
        "durationLabel":self.formatDuration(info["duration"]),
        "audio_formats": self.extractAudioResolutions(info),
        "video_formats":video_formats,
        "default_selected":default_selected
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
    
    def bucket_sorter_direct_download(self,formats):
        bucket = {}
        main_bucket = []
        
        for item in formats:
            try:
                height = item["height"]
                width = item["width"]
                res = int(item["format"].split("(")[-1].strip(")").split("p")[0])
                if not res in bucket and item["url"]!=None and item["acodec"]!="none" and item["vcodec"]!="none" and item["ext"] == "mp4":
                    bucket[res] = []
                bucket[res].append({"height":height,"width":width,"url":item["url"]})
            except:
                pass
            
        for key in bucket:
            bucket[key] = sorted(bucket[key],reverse=True,key=lambda i:i["height"])
            tmp = bucket[key][0]
            tmp["quality"] = key
            tmp["label"] = f'{key}p'
            tmp["default_selected"] = 0
            
            main_bucket.append(tmp)
        return sorted(main_bucket,reverse=True,key=lambda i:i["quality"])
    
    def bucket_sorter_direct_download_for_shorts(self,formats):
        bucket = {}
        main_bucket = []
        
        for item in formats:
            try:
                if item["format_id"] == "22":
                    height = item["height"]
                    width = item["width"]
                    res = int(item["format"].split("(")[-1].strip(")").split("p")[0])
                    if not res in bucket and item["url"]!=None and item["acodec"]!="none" and item["vcodec"]!="none" and item["ext"] == "mp4":
                        bucket[res] = []
                    bucket[res].append({"height":height,"width":width,"url":item["url"]})
            except:
                pass
            
        for key in bucket:
            bucket[key] = sorted(bucket[key],reverse=True,key=lambda i:i["height"])
            tmp = bucket[key][0]
            tmp["quality"] = key
            tmp["label"] = f'{key}p'
            tmp["default_selected"] = 0
            
            main_bucket.append(tmp)
        return sorted(main_bucket,reverse=True,key=lambda i:i["quality"])    
    
    def bucket_sorter_server_downloads(self,formats):
        bucket = {}
        main_bucket = []
        
        for item in formats:
            try:
                height = item["height"]
                width = item["width"]
                res = int(item["format"].split("(")[-1].strip(")").split("p")[0])
                if not res in bucket:
                    bucket[res] = []
                bucket[res].append({"height":height,"width":width})
            except:
                pass
        
        for key in bucket:
            bucket[key] = sorted(bucket[key],reverse=True,key=lambda i:i["height"])
            tmp = bucket[key][0]
            tmp["quality"] = key
            tmp["label"] = f'{key}p'
            tmp["default_selected"] = 0
            tmp["url"] = None
            
            main_bucket.append(tmp)
        
        return sorted(main_bucket,reverse=True,key=lambda i:i["quality"])    
    
    def extractVideoResolutions(self,info):
        
        duration = info["duration"]
        
        availableResolutions = {}
        
        main_bucket = []
        
        direct_downloads = []
        
        if duration <= 60:
            direct_downloads = self.bucket_sorter_direct_download_for_shorts(info["formats"])
        else:
            direct_downloads = self.bucket_sorter_direct_download(info["formats"])
        
        for item in direct_downloads:
            availableResolutions[item["quality"]] = item
        
        server_downloads = self.bucket_sorter_server_downloads(info["formats"])
        
        for item in server_downloads:
            if not item["quality"] in availableResolutions:
                if duration <= 20 * 60:
                    availableResolutions[item["quality"]]= item
                elif duration <= 30 * 60 and duration > 20 * 60:
                    if item["height"] <= 1080:
                        availableResolutions[item["quality"]]= item
                elif duration <= 40 * 60 and duration < 30 * 60:
                    if item["height"] <= 720:
                        availableResolutions[item["quality"]] = item
                else:
                    continue
        
        for key in availableResolutions:
            main_bucket.append(availableResolutions[key])
        
        return sorted(main_bucket,reverse=True,key=lambda x:x["quality"])
    
    def extractAudioResolutions(self,info):
        availableBitrates = []
        try:
            abr = int(128)
            tmp = {}
            tmp["quality"] = abr
            tmp["url"] = None
            tmp["label"] = f'MP3 {abr}kbps'
            availableBitrates.append(tmp)
            
        except Exception as e:
            print(f'error -> {str(e)}')
        
        return availableBitrates
    
    def downloadVideo(self,key,quality):
        
        data = self.redis.get(key)
        
        fileName = f'{data["id"]}/{data["titleSlug"]}-{quality}-ytshorts.savetube.me.mp4'
        
        if self.mediaDir.joinpath(fileName).exists() == True:
            return {
            "downloadUrl":f'{self.host}{fileName}',
            "downloaded":False
        }
            
            
        tmpPath = f'media/{data["id"]}/{data["titleSlug"]}-{quality}-ytshorts.savetube.me.mp4'
        
        ydl_opts = {
        'format':  f'bestvideo[height<={quality}][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': tmpPath,
        'noplaylist': True,
        'quiet': True,
        'verbose': False,
        }
        
        if data["duration"]  <= 60:
            ydl_opts['format_sort'] = ['vcodec:h264']
        
        ydl = yt_dlp.YoutubeDL(ydl_opts)
        
        ydl.download(data["url"])
        
        return {
            "downloadUrl":f'{self.host}{fileName}',
             "downloaded":True
        }
    
    def downloadAudio(self,key,quality):
        
        data = self.redis.get(key)
        
        fileName = f'{data["id"]}/{data["titleSlug"]}-{quality}-ytshorts.savetube.me.mp3'
        
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
                }],
                'outtmpl': f'media/%(id)s/{data["titleSlug"]}-{quality}-ytshorts.savetube.me.%(ext)s',
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
        
    def downloadImage(self,resolution,url,data,position):
        try:
            r = requests.get(url)

            fileName = f'{data["id"]}/{data["titleSlug"]}-{slugify(resolution)}-ytshorts.savetube.me.jpg'

            filePath = self.mediaDir.joinpath(fileName)

            if filePath.exists() == True:
                return {
                    "status":True,
                    "label":resolution,
                    "downloadUrl":f'{self.host}{fileName}',
                    "position":position
                }

            f = open(filePath, 'wb')

            for chunk in r.iter_content(chunk_size=512 * 1024): 
                if chunk: 
                    f.write(chunk)
            f.close()

            return {"status":True,
                    "label":resolution,
                    "downloadUrl":f'{self.host}{fileName}',
                    "position":position
                }
        except Exception as e:
            print(f'error : {str(e)}')
            return {"status":False,
                    "label":resolution,
                    "downloadUrl":f'{self.host}{fileName}',
                    "position":position
                }
        
    def downloadThumbnailMultiThread(self,youtubeUrl):
        thumbnails = []
        
        threads = []
        
        data = self.fetchInfo(youtubeUrl)
        
        folder = self.mediaDir.joinpath(data["id"])
        
        if not folder.exists():
            folder.mkdir()
        
        try:
            with ThreadPoolExecutor(max_workers=10) as executor:
                for position,resolution in enumerate(self.image_resolutions):
                    url = self.image_resolutions[resolution].format(id=data['id'])
                    threads.append(executor.submit(self.downloadImage,resolution,url,data,position))
                    
                for task in as_completed(threads):
                    image = task.result()
                    if image["status"] == True:
                        thumbnails.append(image)
                        
        except Exception as e:
            print(f'error : {__file__} : {str(e)}')
        
        return sorted(thumbnails,key=lambda x:x["position"])
    
    def downloadThumbnail(self,youtubeUrl):
        
        data = self.fetchInfo(youtubeUrl)
        
        thumbnails = []
        
        folder = self.mediaDir.joinpath(data["id"])
        
        if not folder.exists():
            folder.mkdir()
        
        for resolution in self.image_resolutions:
            r = requests.get(self.image_resolutions[resolution].format(id=data['id']))
            
            fileName = f'{data["id"]}/{data["titleSlug"]}-{slugify(resolution)}-ytshorts.savetube.me.jpg'
            
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