# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:26:56 2020

@author: user
"""

import tkinter as tk
window = tk.Tk()
window.title("???")
window.geometry("500x500")
menuBar=tk.Menu(window)
filemenu=tk.Menu(menuBar,tearoff=False)
filemenu.add_command(label="吃屎吧")
filemenu.add_command(label="喝尿吧")
filemenu.add_separator()
filemenu.add_command(label="Exit")
menuBar.add_cascade(label="按我",menu=filemenu)
filemenu2=tk.Menu(menuBar,tearoff=False)
filemenu2.add_command(label="吃屎")
filemenu2.add_command(label="喝尿")
menuBar.add_cascade(label="不要按我",menu=filemenu2)

filemenu3=tk.Menu(filemenu2,tearoff=False)
filemenu3.add_command(label="遊戲設定")
filemenu3.add_command(label="設定")
filemenu2.add_cascade(label="不要按我",menu=filemenu3)
window.config(menu=menuBar)

window.mainloop()