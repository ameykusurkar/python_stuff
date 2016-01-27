import Tkinter
import random
import time

top = Tkinter.Tk()

swap = False

def toggle():
    global swap
    swap = not swap
    if(swap):
        B.configure(text="Stop!")
    else:
        B.configure(text="Change!")
    randColour()

def randColour():
    global swap
    if(swap):
        result = random.randint(0, 0xFFFFFF)
        C.configure(bg='#{:06x}'.format(result))
        top.after(500, randColour)

C = Tkinter.Canvas(top, bg="#000000", height=500, width=500)
C.pack()
B = Tkinter.Button(top, text="Change!", command=toggle)
B.pack()

top.after(1000, randColour)
top.mainloop()

