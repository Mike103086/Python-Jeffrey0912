# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:19:22 2020

@author: user
"""
import threading
import tkinter as tk
from pytube import YouTube

window=tk.Tk()

window.title("YouTube下載器")
window.geometry('500x150')
window.resizable(False,False)
def showProgress(stream,chunk,bytes_remaining):
    size=stream.filesize
    global progress
    preprogress=progress
    currentprogress=int((size-bytes_remaining)*100/size)
    progress=currentprogress
    
    if progress == 100:
        print("下載完成")
        return
    if preprogress!=progress:
        scale.set(progress)
        window.update()
        print("目前進度:"+ str(currentprogress)+"%")
def thread():
    threading.Thread(target=onClick).start()
def onClick():
    global var
    var.set(entry.get())
    button.config(state=tk.DISABLED)
    try:
      yt = YouTube(var.get(),on_progress_callback=showProgress)
      if onlyMusic.get():
          stream=yt.streams.filter(only_audio=True).first()
          stream.download()
      else:
          stream = yt.streams.first()
          stream.download()
    except:
        print("下載失敗")
    button.config(state=tk.NORMAL)
     
entry=tk.Entry(window,width=50)
entry.pack()
onlyMusic = tk.BooleanVar()
check = tk.Checkbutton(window,text = "只有音樂",variable = onlyMusic,
                       onvalue = True, offvalue = False)
check.pack()

button=tk.Button(window,text="案",command = thread)
button.pack()
scale = tk.Scale(window,label="進度條",
                 orient=tk.HORIZONTAL,
                 length=200)
scale.pack()

window.mainloop()