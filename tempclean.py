import os 
import psutil as ps
import shutil

def ClearTemp():
    PATH = f"C:\\Users\\admin\\AppData\\Local\\Temp"
    files = os.listdir(PATH)
    cmd = 'TASKKILL'
    count = 0
    for file in files:
        try:
            FILE_PATH = PATH + '\\' + file
            if os.path.isfile(FILE_PATH) and os.path.exists(FILE_PATH):
                os.system(cmd + FILE_PATH + ' /F')
                os.remove(FILE_PATH)
                count += 1
            elif os.path.isdir(FILE_PATH) and os.path.exists(FILE_PATH):
                os.system(cmd + FILE_PATH + ' /F')
                shutil.rmtree(FILE_PATH)
                count += 1
        except Exception:
            continue
    print(f"Deleted {count} files")


