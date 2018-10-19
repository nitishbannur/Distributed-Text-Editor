from tkinter import *

import tkinter.messagebox


root=Tk()   #First Screen+

CS=0                            #initally, root holds the token to the critical section
w=(root.winfo_screenwidth())/2
h=(root.winfo_screenheight())/2

#print("width is"+str(w)+"height is: "+str(h))

root1=Tk()  #Second Scree
root2=Tk()  #Third Screen

root.geometry("%dx%d+0+0"%(w,h))
root1.geometry("%dx%d+0+0"%(w,h))
root2.geometry("%dx%d+0+0"%(w,h))


root.configure(background='orange')
root1.configure(background='white')
root2.configure(background='green')

root.title('First Screen')
root1.title('Second Screen')
root2.title('Third Screen')

basic_msg=Label(root,text="FIRST Screen, Enter your Text Below")
basic_msg.pack()

basic_msg=Label(root1,text="Second Screen, Enter your Text Below")
basic_msg.pack()

basic_msg=Label(root2,text="Third Screen, Enter your Text Below")
basic_msg.pack()

Editor = Text(root, width=50, height=15)
Editor1 = Text(root1, width=50, height=15)
Editor2 = Text(root2, width=50, height=15)



def writer(k):

    if(k==1):

        Editor.place(x=30, y=100)
        submit.place(x=30, y=360)
        warning1.place(x=30, y=20)
        warning2.place(x=30, y=20)

    if (k == 2):
        Editor1.place(x=30, y=100)
        submit1.place(x=30, y=360)
        warning.place(x=30, y=20)
        warning2.place(x=30, y=20)

    if (k == 3):
        Editor2.place(x=30, y=100)
        submit2.place(x=30, y=360)
        warning.place(x=30, y=20)
        warning1.place(x=30, y=20)

def exect(l):
    if(l==1):
        print("\n Am i in 1??")
        entry = Editor.get("1.0", "end-1c")
        second = open("common.txt", 'a')
        second.write(entry)
        second.close()

        succ1 = open('common.txt', 'r')
        cool = succ1.read()
        print(cool)
        succ1.close()
        #warning3 = Label(root1, text="You just wrote on the file!!")
        #warning.place(x=250, y=460)
        #warning1.destroy()
        #warning2.destroy()
        warning1.place_forget()
        warning2.place_forget()

    if(l==2):
        print("\n Am i in 2??")

        '''succ1 = open('common.txt', 'r')
        cool = succ1.read()
        Editor1.insert(INSERT, cool)
        succ1.close()'''

        entry = Editor1.get("1.0", "end-1c")
        second = open("common.txt", 'a')
        second.write(entry)
        second.close()
        succ1 = open('common.txt', 'r')
        cool = succ1.read()
        print(cool)
        #warning = Label(root1, text="You just wrote on the file!!")
        #warning.place(x=250, y=460)
        #warning.destroy()
        #warning2.destroy()
        warning.place_forget()
        warning2.place_forget()

    if(l==3):
        print("\n Am i in 3??")

        succ1 = open('common.txt', 'r')
        cool = succ1.read()
        Editor2.insert(INSERT, cool)
        succ1.close()

        entry = Editor2.get("1.0", "end-1c")
        second = open("common.txt", 'a')
        second.write(entry)
        second.close()
        succ1 = open('common.txt', 'r')
        cool = succ1.read()
        print(cool)
        #warning2 = Label(root, text="You just wrote on the file!!")
        #warning2.place(x=250, y=460)
        #warning1.destroy()
        #warning.destroy()
        warning1.place_forget()
        warning.place_forget()

check=Button(root,text="do you want to write",command=lambda: writer(1))
check.place(x=30,y=20)

check=Button(root1,text="do you want to write",command=lambda: writer(2))
check.place(x=30,y=20)

check=Button(root2,text="do you want to write",command=lambda: writer(3))
check.place(x=30,y=20)


submit = Button(root, text="Submit", bg="white", font="bold",command=lambda: exect(1))


submit1 = Button(root1, text="Submit", bg="white", font="bold", command=lambda: exect(2))


submit2 = Button(root2, text="Submit", bg="white", font="bold", command=lambda: exect(3))


warning = Label(root, text="you cant write right now!")
warning1 = Label(root1, text="you cant write right now!")
warning2 = Label(root2, text="you cant write right now!")





root.mainloop()
root1.mainloop()
root2.mainloop()