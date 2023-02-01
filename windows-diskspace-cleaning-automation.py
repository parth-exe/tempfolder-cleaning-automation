import os 
import psutil as ps
import shutil
import winshell
import time
############################################################################################################################################################################################## 
def ClearTemp():
    PATH = f"C:\\Users\\admin\\AppData\\Local\\Temp"
    files = os.listdir(PATH)
    count = 0
    size = 0
    for file in files:
        try:
            FILE_PATH = PATH + '\\' + file
            if os.path.exists(FILE_PATH):
                if os.path.isfile(FILE_PATH):
                    if Exception:
                        continue
                    size += os.path.getsize(FILE_PATH)
                    os.remove(FILE_PATH)
                    count += 1
                elif os.path.isdir(FILE_PATH):
                    if Exception:
                        continue
                    size += os.path.getsize(FILE_PATH)
                    shutil.rmtree(FILE_PATH)
                    count += 1
        except Exception:
            continue
    print("*"*15)
    print(f"Deleted {count} files from Temp")
    print(f"{round(size / 1048576, 2)} MB files cleared from Temp Folder")
    print("*"*15)
############################################################################################################################################################################################## 
def check_pc_health():
    if ps.virtual_memory()[2] > 65:
        print("Consider killing non-essential processes or restarting your PC")
    if ps.cpu_percent(1) > 50:
        print("Restarting your PC is advised. Unusual CPU usage.")
####################################################################################################################################################################################################
def print_pc_health():
    print("*"*15)
    print(f"RAM usage: {ps.virtual_memory()[2]}%")
    print(f"CPU count: {ps.cpu_count()}")
    print(f"CPU usage: {ps.cpu_percent(1)}%")
    print("*"*15)
############################################################################################################################################################################################## 
def EmptyRecycleBin():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        print("Recycle Bin emptied.")
    except Exception:
        print("The bin is already empty.")
        pass
##############################################################################################################################################################################################        
def CleanDownloads():
    target_path = f"C:\\Users\\admin\\Downloads"
    files = os.listdir(target_path)
    sec_per_day = 86400
    number_of_days = 30
    file_count = 0
    size = 0
    time_now = time.time()
    try:
        for file in files:
            target_file_path = target_path + '\\' + file
            file_age = os.stat(target_file_path).st_mtime
            if file_age < time_now - (sec_per_day*number_of_days):
                size += os.path.getsize(target_file_path)
                os.remove(target_file_path)
                file_count += 1
    except Exception:
        print("No files older than 30 days were found.")
        pass
    print(f"{file_count} files were deleted and were older than 30 days.")
    print(f"{round(size / 1048576, 2)} MB files cleared from Downloads Folder")
####################################################################################################################################################################################################           
def main():
    start = time.time()
    ClearTemp()
    CleanDownloads()
    EmptyRecycleBin()
    print_pc_health()
    check_pc_health()
    end = time.time()
    print(f"Execution time: {round(end - start - 2, 5)} seconds")
#################################################################################################################################################################################################### 

if __name__ == '__main__':
    main()
