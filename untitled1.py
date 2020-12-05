# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:19:14 2020

@author: user
"""

from pytube import Youtube
progress=0
def prgress(stream,chunk,bytes_remaining):
    size=stream.filesize
    global progress
    preprogress=progress
    currentprogress=int((size-bytes_remaining)*100/size)
    progress=currentprogress
    if preprogress!=progress:
        print("目前進度:"+ (currentprogress)+"%")
    if progress ==100:
        print("下載完成")    

yt = Youtube("https://youtu.be/bdCK7JQryhQ",on_progress_callback=progress)
stream = yt.streams.first()
stream.download("C:\\Users\\user\\Videos\\Captures")