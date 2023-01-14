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


def check_pc_health():
    if ps.virtual_memory()[2] > 65:
        print("Consider killing non-essential processes or restarting your PC")
    if ps.cpu_percent(1) > 50:
        print("Restarting your PC is advised. Unusual CPU usage.")

def print_pc_health():
    print("*"*15)
    print(f"RAM usage: {ps.virtual_memory()[2]}%")
    print(f"CPU count: {ps.cpu_count()}")
    print(f"CPU usage: {ps.cpu_percent(1)}%")
    print("*"*15)
        
    
ClearTemp()
print_pc_health()
check_pc_health()