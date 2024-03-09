
from tkinter import *
import tkinter
import matplotlib.pyplot as plt
import numpy as np
import socket
from tkinter import filedialog
import json
import os

main = tkinter.Tk()
main.title("Motag Client Application") #designing main screen
main.geometry("1300x1200")

global port
global greedy
global requests
requests = 0
greedy = 0

def upload():
    global port
    global greedy
    global requests
    filename = filedialog.askopenfilename(initialdir=".")
    fname = os.path.basename(filename)
    with open(filename, "rb") as file:
        filedata = file.read()
    file.close()
    requests = requests + 1
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect(('localhost', 3333))
    message = client.send('getproxy'.encode())
    data = client.recv(100)
    data = data.decode()
    port = int(data)
    print(port)
    proxy_name = ''
    if port == 4444:
        proxy_name = 1
    else:
        proxy_name = 2
    text.insert(END,'Autentication server assigned client to proxy : '+str(proxy_name)+"\n")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect(('localhost', port))
    jsondata = json.dumps({"name": fname, "fdata": filedata.decode()})
    message = client.send(jsondata.encode())
    data = client.recv(100)
    data = data.decode()
    text.insert(END,data+"\n")
    if 'detected DDOS Attack & request dropping' in data:
        greedy = greedy + 1
    
def graph():
    height = [requests,2,greedy]
    bars = ('Total Requests','Shuffling Proxies','DDOS Attack Detected')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.show()
    

font = ('times', 16, 'bold')
title = Label(main, text='Motag Client Application')
title.config(bg='LightGoldenrod1', fg='medium orchid')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)

font1 = ('times', 12, 'bold')
serverButton = Button(main, text="Upload File to Application Server", command=upload)
serverButton.place(x=50,y=100)
serverButton.config(font=font1)

serverButton = Button(main, text="Attack Detection Graph", command=graph)
serverButton.place(x=350,y=100)
serverButton.config(font=font1)

text=Text(main,height=28,width=130)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=150)
text.config(font=font1)

main.config(bg='OliveDrab2')
main.mainloop()


