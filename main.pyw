from tkinter import *
from tkinter import filedialog
from time import sleep
import os
import random

# main functions to perform tasks
def process_text(arr):
    new_arr=[]
    temp=0
    if(len(arr)==0):
        return ""
    odd_or_even=random.randint(0,1)
    if odd_or_even == 0:
        for i in range(len(arr)):
            if(arr[i]=="\n"):
                new_arr.append(arr[i])
                pass
            elif(temp%2==0):
                new_arr.append(arr[i])
            temp=temp+1
    else:
        for i in range(len(arr)):
            if(arr[i]=="\n"):
                new_arr.append(arr[i])
                pass
            elif(temp%2==1):
                new_arr.append(arr[i])
            temp=temp+1
    # print(new_arr)
    return "\n".join(new_arr)
            
def use_stones(working_dir,file):
    os.chdir(working_dir)
    with open(file,"r") as f:
        text=f.read()
        arr = text.split("\n")
        magic_text = process_text(arr)
    with open(file,"w") as f:
        # print(magic_text)
        f.write(magic_text)

def thalnos(woring_dir):
    os.chdir(woring_dir)
    current_dir=os.getcwd()
    # print(os.getcwd())
    if(len(os.listdir())==0):
        return
    filesAndFolder = os.listdir()
    for i in filesAndFolder:
        if os.path.isdir(os.path.join(current_dir,i)):
            thalnos(os.path.join(current_dir,i))
        else:
            use_stones(os.path.join(current_dir),i)
    os.chdir(current_dir)
    
def call_thalnos():
    update_status("Working...")
    current_dir=download_path.get()
    thalnos(current_dir)
    try:
        os.chdir(current_dir)
    except:
        update_status("Some Error")
        sleep(0.2)
    update_status("Task done")
    sleep(0.4)
    update_status("Ready to go")

# gui funtions 
def update_status(temp):
    statusvar.set(temp)
    sbar.update()

def select_folder():
    folder = filedialog.askdirectory()
    download_path.set(folder)
    downloads_location.set(f"Current Selected Universe :- {folder}")
    download_loacation_display.update()


# main body
if __name__=="__main__":
    root = Tk()
    # window size
    root.title("ELITE-THANOS-STONES")
    root.geometry("1000x400")
    root.minsize(1000,400)
    
    # Variables
    downloads_location=StringVar()
    statusvar = StringVar()
    download_path=StringVar()
    download_path.set(os.getcwd())
    statusvar.set("Ready to go")
    # code to download a video
    heading1=Label(root,text="ELITE AKSHAY",font="calibre 40 bold",relief=RAISED,background="cyan",padx=10,pady=9)
    heading1.pack()
    Label(root,text="",font="calibre 2 bold").pack()
    heading2=Label(root,text="THANOS STONES",font="Times 50 bold",relief=RAISED,background="cyan",padx=10,pady=9,)
    heading2.pack()
    Label(root,text="",font="calibre 2 bold").pack()
    Label(root,text="Feel the power of 6 stones",font="calibre 20 bold",relief=RAISED,background="cyan",padx=10,pady=9,).pack()
    Label(root,text="",font="calibre 2 bold").pack()

    f4=Frame()
    f4.pack(side=TOP,fill=X,expand=False)
    downloads_location.set(f"Current Selected Universe :- {download_path.get()}")
    download_loacation_display=Label(f4,textvariable=downloads_location,font="calibre 10 bold italic",relief=FLAT,padx=8,pady=3)
    download_loacation_display.pack()

    f2=Frame(root)
    f2.pack(side=TOP,fill=X,expand=False)
    Label(f2,text="",font="calibre 2 bold").pack()
    download_video_btn=Button(f2,text="Select Universe",command=select_folder,bd=5,fg="blue",font="calibre 18 bold")
    download_video_btn.pack(side = LEFT, expand = True, fill = X)
    download_playlist_btn=Button(f2,text="Use Infinity Gauntlet",command=call_thalnos,bd=5,fg="blue",font="calibre 18 bold")
    download_playlist_btn.pack(side = LEFT, expand = True, fill = X)
    
    # statusbar
    sbar = Label(root,textvariable=statusvar, relief=SUNKEN, anchor="w",padx=10,pady=7,background="cyan",fg="red",font="calibre 12 bold")
    sbar.pack(side=BOTTOM, fill=X)

    root.mainloop()