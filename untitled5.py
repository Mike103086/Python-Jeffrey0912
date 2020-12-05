# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:46:43 2020

@author: user
"""

import tkinter as tk
window = tk.Tk()
window.title("???")
window.geometry("500x500")
tk.Label(window,text="Place").place(x=0,y=0)
tk.Label(window,text="Place").place(x=150,y=150)
tk.Label(window,text="Place").place(x=260,y=260)
tk.Label(window,text="Place").place(x=300,y=300)
window.mainloop()