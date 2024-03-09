
from tkinter import *
import tkinter
import matplotlib.pyplot as plt
import numpy as np
import socket 
from threading import Thread 
from socketserver import ThreadingMixIn
import json

main = tkinter.Tk()
main.title("Motag Application Server") #designing main screen
main.geometry("1300x1200")

def startApplicationServer():
    print("hello")
    class ClientThread(Thread): 
 
        def __init__(self,ip,port): 
            Thread.__init__(self) 
            self.ip = ip 
            self.port = port 
            text.insert(END,'Request received from IP : '+ip+' with port no : '+str(port)+"\n") 
 
        def run(self): 
            data = conn.recv(10000)
            data = json.loads(data.decode())
            name = str(data.get("name"))
            fdata = str(data.get("fdata"))
            f = open("ReceiveData/"+name, "w")
            f.write(fdata)
            f.close()
            text.insert(END,"Application server received data and saved inside ReceiveData folder\n")

    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    tcpServer.bind(('localhost', 2222))
    threads = []
    text.insert(END,"Application Server Started\n\n")
    while True:
        tcpServer.listen(4)
        (conn, (ip,port)) = tcpServer.accept()
        newthread = ClientThread(ip,port) 
        newthread.start() 
        threads.append(newthread) 
    for t in threads:
        t.join()

def startServer():
    Thread(target=startApplicationServer).start()
    

font = ('times', 16, 'bold')
title = Label(main, text='Motag Application Server')
title.config(bg='LightGoldenrod1', fg='medium orchid')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)

font1 = ('times', 12, 'bold')
serverButton = Button(main, text="Start Application Server", command=startServer)
serverButton.place(x=50,y=100)
serverButton.config(font=font1)

text=Text(main,height=28,width=130)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=150)
text.config(font=font1)

main.config(bg='OliveDrab2')
main.mainloop()


