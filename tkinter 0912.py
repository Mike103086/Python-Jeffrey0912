# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:25:19 2020

@author: user
"""

import tkinter as tk
import tkinter.messagebox
def clickMe():
    tkinter.messagebox.showinfo(title='提示',message='好痛')

window = tk.Tk()
window.title("??的第一個GUI")
window.geometry('300x300')
label = tk.Label(window,text='???????????????????',bg="#7AFEC6",fg="#00FFFF")
label.pack()
entry = tk.Entry(window,width=20)
entry.pack()
button=tk.Button(window,text="案",command = clickMe)
button.pack()
window.mainloop()

