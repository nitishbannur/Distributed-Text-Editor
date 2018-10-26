# Python program to implement client side of chat room. 
import socket 
import select 
import sys
import datetime 
import time
import random
import os.path
"""GUI Part"""


from tkinter import *

import tkinter.messagebox


root=Tk()   #First Screen+

CS=0                            #initally, root holds the token to the critical section
w=(root.winfo_screenwidth())/2
h=(root.winfo_screenheight())/2

root.geometry("%dx%d+0+0"%(w,h))

colors = ['orange', 'black', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

root.configure(background=random.choice(colors))

root.title('Text Editor')

basic_msg=Label(root,text="Enter your Text Below")
basic_msg.pack()

Editor = Text(root, width=50, height=15)

message_from_gui = ""

def writer():
    Editor.place(x=(w/4), y=100)
    submit.place(x=(w/2)-(w/4), y=360)
    update.place(x=(w/2)+(w/4)-75, y=360)
    save.place(x=(w/2)-(w/4), y=390)


def send_message():
    message_from_gui = Editor.get("1.0", "end-1c")
    message = message_from_gui
    print("\nMessage from GUI ", message)
    message = message+"\t"+str(datetime.datetime.now()) 
    server.send(message.encode()) 
    sys.stdout.write("\n<You>") 
    sys.stdout.write(message) 
    sys.stdout.flush()

def recv_message():
	message = server.recv(2048).decode()
	print(message)
	Editor.delete("1.0", "end-1c")
	Editor.insert("1.0", message)
	
def save_message():
	message_from_gui = Editor.get("1.0", "end-1c")
	with open("TextEditor.txt", "w", encoding='UTF-8') as f:
		f.write(message_from_gui)
		
def load_msg():
	with open("TextEditor.txt", "r", encoding='UTF-8') as f:
		message = f.read()
	print(message)
	Editor.delete("1.0", "end-1c")
	Editor.insert("1.0", message)

submit = Button(root, text="Submit", bg="white", font="bold",command=lambda: send_message())
update = Button(root, text="Update", bg="white", font="bold",command=lambda: recv_message())
save = Button(root, text="Save", bg="white", font="bold",command=lambda: save_message())
writer()

"""GUI Part End"""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
    print ("Correct usage: script, IP address, port number")
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port)) 

recv_message()
if (os.path.isfile("TextEditor.txt")):
	load_msg()
else:
	recv_message()
  
root.mainloop()

server.close()
