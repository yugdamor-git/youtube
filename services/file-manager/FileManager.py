from datetime import datetime
from pathlib import Path
import time

class FileManager:
    def __init__(self):
        print(f'FileManager init')
        
        self.cwd = Path.cwd()
        
        self.mediaDir = self.cwd.joinpath("media")

        deleteAfter = 30
        
        self.deleteAfter = deleteAfter * 60
#       30 min
    
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
                        
                        
if __name__ == "__main__":
    
    fm = FileManager()
    
    while True:
        fm.main()
        time.sleep(5 * 60)