from datetime import datetime
from pathlib import Path
import time
import sh
import os
import pymongo

from LogManager import LogManager

class FileManager:
    def __init__(self):
        print(f'FileManager init')
        
        self.cwd = Path.cwd()
        
        self.mediaDir = self.cwd.joinpath("media")

        deleteAfter = 20
        
        self.deleteAfter = deleteAfter * 60
        
        self.server = os.environ.get("IP")
#       30 min

        self.logManager = LogManager()
    
    def main(self):
        now = datetime.now()
        
        for folder in self.mediaDir.iterdir():
            if folder.is_dir() == True:
                for file in folder.iterdir():
                    createdAt = datetime.fromtimestamp(file.lstat().st_ctime)
                    
                    seconds = (now - createdAt).seconds
                    
                    if self.deleteAfter < seconds:
                        print(f'deleting file : {file}')
                        file.unlink()
                    else:
                        print(f'new file : {file}')

    def getDirectorySize(self,path):
        filesize = sh.du("-sh", str(path)).split("\t")[0].strip()
        return filesize
    
    def manageStorageStats(self):
        directorySize = self.getDirectorySize(self.mediaDir)
        self.logManager.updateStorageInfo(directorySize)
        
        
if __name__ == "__main__":
    
    fm = FileManager()
    
    while True:
        fm.main()
        fm.manageStorageStats()
        time.sleep(5 * 60)
