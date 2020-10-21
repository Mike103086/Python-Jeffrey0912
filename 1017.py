# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 21:01:01 2020

@author: user
"""

import tkinter as tk

window = tk.Tk()
window.title('單選按鈕')
string = tk.StringVar()

def selection():
    label.config(text="我喜歡" + string.get())
label = tk.Label(window, bg='#f00',text='尚未選擇')
label.pack()

radio1 = tk.Radiobutton(window,
                        text='Minecraft Python',
                        variable=string,value='Minecraft Python',
                        command=selection)
radio1.pack()   
 
radio1 = tk.Radiobutton(window,
                        text='Pygame',
                        variable=string,value=' Pygame',
                        command=selection)
radio1.pack()   

radio3 = tk.Radiobutton(window,
                        text='Tkinter',
                        variable=string,value='Tkinter',
                        command=selection)
radio3.pack()


window.mainloop()      
    
    
    
    