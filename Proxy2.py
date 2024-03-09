
from tkinter import *
import tkinter
import matplotlib.pyplot as plt
import numpy as np
import socket 
from threading import Thread 
from socketserver import ThreadingMixIn
import socket 

main = tkinter.Tk()
main.title("Motag Proxy2 Server") #designing main screen
main.geometry("1300x1200")


def startProxyServer():
    class ClientThread(Thread): 
 
        def __init__(self,ip,port): 
            Thread.__init__(self) 
            self.ip = ip 
            self.port = port 
            text.insert(END,'Request received from IP : '+ip+' with port no : '+str(port)+"\n") 
 
        def run(self): 
            data = conn.recv(10000)
            if len(data) < 8000:
                serversend = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                serversend.connect(('localhost', 2222))
                serversend.send(data)
                conn.send('Your request sent to Application Server via proxy2'.encode())
                text.insert(END,'Proxy2 sent client data to application server. No DDOS attack detected\n')
            else:
                conn.send("Proxy 2 detected DDOS Attack & request dropping".encode())
                text.insert(END,'Proxy2 detected DDOS attack and request is dropping\n')
                 

    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    tcpServer.bind(('localhost', 5555))
    threads = []
    text.insert(END,"Proxy2 Started\n\n")
    while True:
        tcpServer.listen(4)
        (conn, (ip,port)) = tcpServer.accept()
        newthread = ClientThread(ip,port) 
        newthread.start() 
        threads.append(newthread) 
    for t in threads:
        t.join()

def startServer():
    Thread(target=startProxyServer).start()
    

font = ('times', 16, 'bold')
title = Label(main, text='Motag Proxy1 Server')
title.config(bg='LightGoldenrod1', fg='medium orchid')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)

font1 = ('times', 12, 'bold')
serverButton = Button(main, text="Start Proxy2 Server", command=startServer)
serverButton.place(x=50,y=100)
serverButton.config(font=font1)

text=Text(main,height=28,width=130)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=150)
text.config(font=font1)

main.config(bg='OliveDrab2')
main.mainloop()


