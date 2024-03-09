
from tkinter import *
import tkinter
import matplotlib.pyplot as plt
import numpy as np
import socket 
from threading import Thread 
from socketserver import ThreadingMixIn
from random import randrange
import socket 

main = tkinter.Tk()
main.title("Motag Authentication Server") #designing main screen
main.geometry("1300x1200")

def getRandomShuffleProxy():
    proxy = randrange(2)
    return proxy

def startAuthenticationServer():
    class ClientThread(Thread): 
 
        def __init__(self,ip,port): 
            Thread.__init__(self) 
            self.ip = ip 
            self.port = port 
            text.insert(END,'Request received from IP : '+ip+' with port no : '+str(port)+"\n") 
 
        def run(self): 
            data = conn.recv(100)
            data = data.decode()
            proxy = getRandomShuffleProxy()
            proxyport = ''
            pno = 0
            if proxy == 0:
                proxyport = 4444
                pno = 1
            if proxy == 1:
                proxyport = 5555
                pno = 2
            proxyfirst = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.send(str(proxyport).encode())
            text.insert(END,'Client request assigned to proxy : '+str(pno)+'\n')
                 

    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    tcpServer.bind(('localhost', 3333))
    threads = []
    text.insert(END,"Authentication Server Started\n\n")
    while True:
        tcpServer.listen(4)
        (conn, (ip,port)) = tcpServer.accept()
        newthread = ClientThread(ip,port) 
        newthread.start() 
        threads.append(newthread) 
    for t in threads:
        t.join()

def startServer():
    Thread(target=startAuthenticationServer).start()
    

font = ('times', 16, 'bold')
title = Label(main, text='Motag Authentication Server')
title.config(bg='LightGoldenrod1', fg='medium orchid')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)

font1 = ('times', 12, 'bold')
serverButton = Button(main, text="Start Authentication Server", command=startServer)
serverButton.place(x=50,y=100)
serverButton.config(font=font1)

text=Text(main,height=28,width=130)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=150)
text.config(font=font1)

main.config(bg='OliveDrab2')
main.mainloop()


