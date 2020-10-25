# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:12:48 2020

@author: user
"""


from pytube import YouTube
import tkinter as tk
window=tk.Tk()
progress=0
def showProgress(stream,chunk,bytes_remaining):
    size=stream.filesize
    global progress
    preprogress=progress
    currentprogress=int((size-bytes_remaining)*100/size)
    progress=currentprogress
    if preprogress!=progress:
        scale.set(progress)
        window.update()
        print("目前進度:"+ (currentprogress)+"%")
    if progress ==100:
        print("下載完成")
        return
    


def onClick():
    global var
    var.set(entry.get())
    try:
      yt = YouTube(var.get(),on_progress_callback=showProgress)
      stream = yt.streams.first()
      stream.download()
    except:
        print("下載失敗")
 
    
label=tk.Label(window,text="請不要輸入Youtube網址")
label.pack()
var = tk.StringVar()

entry=tk.Entry(window,width=50)
entry.pack()

scale = tk.Scale(window,label="進度條",
                 orient=tk.HORIZONTAL,
                 length=200)
scale.pack()
window.mainloop()