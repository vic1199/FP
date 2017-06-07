import tkinter
from tkinter import *
import random
from random import randrange

ventana = Tk()
ventana.geometry("720x480")
C = Canvas(ventana, width=720, height=480, bg="white")
C.pack()

def burbujas():
     for i in range (0, 5):
          x1 = random.randrange(20, 700)
          y1 = random.randrange(20, 400)
          xy= x1, y1, x1+20, y1+20
          C.create_arc(xy, start=0, extent=359, fill="black")

burbujas()
ventana.mainloop()
