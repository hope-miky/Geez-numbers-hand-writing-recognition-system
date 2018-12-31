# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 02:17:01 2018

@author: Tesfamichael Molla
"""

from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import ImageGrab


class Paint(object):

    DEFAULT_PEN_SIZE = 50
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='save', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=2)

        self.choose_size_button = Scale(self.root, from_=1, to=80, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=3)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=4)

        self.count = 0

        self.setup()
        self.root.mainloop()


    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        #self.activate_button(self.pen_button)
        s = str(self.count) + '.jpg'
        #self.c.postscript(file=s,colormode='color')

        x=self.root.winfo_rootx()+ self.c.winfo_x()
        y=self.root.winfo_rooty()+ self.c.winfo_y()
        x1= x + self.c.winfo_width()
        y1= y + self.c.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(s)
        self.count = self.count + 1
        self.c.delete('all')

    def use_brush(self):
        self.activate_button(self.brush_button)

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = 50
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()
