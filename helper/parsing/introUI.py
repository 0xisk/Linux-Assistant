#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Linux Assistant team
# Created Date: Mon Jan 20 18:54:00 PDT 2019
# =============================================================================
"""this module provide App class, that is used to show a loading screen while loading the program
"""
# =============================================================================
# Imports
# =============================================================================

from time import sleep
from tkinter import Tk , Label
from threading import Thread

class App(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.start()

    def callback(self):
        self.cont = False;
        self.root.withdraw();   #hide the screen at end

    def run(self):
        "run the screen while changing the text content"
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.overrideredirect(1)
        self.root.geometry("600x300")
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)

        self.root.bind("<ButtonPress-1>", self.StartMove)
        self.root.bind("<ButtonRelease-1>", self.StopMove)
        self.root.bind("<B1-Motion>", self.OnMotion)
    
        self.cont = True;
        self.text = Label(self.root,text="Loading |",bg="#b5becc" , font=("Consolas",17,"bold"))
        self.text.grid(row=0,column=0,sticky="snew")
        self.startNewThread(self._changeText)
        self.root.mainloop()


    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry("+%s+%s" % (x, y))

    def _changeText(self) :
        "change the text content to be shown as a movement text"
        while self.cont : #while cont is True then repeat this changing of text
            if self.cont : self.text.configure(text="Loading /");
            sleep(0.4);
            if self.cont : self.text.configure(text="Loading -");
            sleep(0.4)
            if self.cont : self.text.configure(text="Loading \\");
            sleep(0.4);
            if self.cont : self.text.configure(text="Loading |");
            sleep(0.4)
        print("quit")

    @staticmethod
    def startNewThread(func) :
        "start a new thread"
        thread = Thread(target=func);
        thread.setDaemon(True);
        thread.start();


"""
app = App()
print('Now we can continue running code while mainloop runs!')

for i in range(100000):
    print(i)

app.callback()
Tk().mainloop();
"""