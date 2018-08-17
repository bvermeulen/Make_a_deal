from tkinter import ttk
import tkinter as tk #fixed typo in here
from tkinter.ttk import Frame, Style, Scrollbar
w=tk.Tk()
style=ttk.Style()
style.configure("B.TFrame", background='yellow')
f=ttk.Frame(w, width=500, height=300, style='B.TFrame')
f.grid(row=0, column=0)
style.configure("A.TFrame", background='green')
g=ttk.Frame(w, width=800, height=500, style='A.TFrame')
g.grid(row=0, column=1)
style.configure("C.TFrame", background='grey')
h=ttk.Frame(w, width=800, height=500, style='C.TFrame')
h.grid(row=0, column=2)


def onscrollx(*args):
    a.xview(*args)
    b.xview(*args)

def onscrolly(*args):
    a.yview(*args)
    b.yview(*args)

yscrollbar = Scrollbar(h, orient='vertical', command=onscrolly)
yscrollbar.pack(side='right', fill='y', expand='yes')
xscrollbar = Scrollbar(h, orient='horizontal', command=onscrollx)
xscrollbar.pack(side='bottom', fill='x', expand='yes')

a=tk.Canvas(f, width=200, height=200, bg="blue", scrollregion=(0,0,800, 800),
            yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
a.pack()
b=tk.Canvas(f, width=200, height=200, bg="yellow", scrollregion=(0,0,800, 800),
            yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
b.pack()
c=tk.Canvas(h, width=200, height=200, bg="pink")
c.pack(expand='yes')

a.create_rectangle(100, 100, 150, 150, fill='orange')
b.create_rectangle(150, 100, 200, 150, fill='orange')



w.mainloop()
