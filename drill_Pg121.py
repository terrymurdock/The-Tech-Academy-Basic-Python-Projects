# Python Ver. 3.7.4
#
# Author:       Terry Murdock
#
# Purpose:      Drill Pg 121
#
# Tested OS:    This code was written and tested to work with Windows 10.

import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(400,175))
        self.master.title('Check files')
        
        self.varEntry1 = StringVar()
        self.varEntry2 = StringVar()

        self.txtEntry1 = Entry(self.master,text=self.varEntry1, font=("Helvetica", 16), fg='black', bg='white')
        self.txtEntry1.grid(row=0, column=1, padx=(0,0), pady=(40,0), sticky=NSEW)

        self.txtEntry2 = Entry(self.master,text=self.varEntry2, font=("Helvetica", 16), fg='black', bg='white')
        self.txtEntry2.grid(row=1, column=1, padx=(0,0), pady=(10,0), sticky=NSEW)

        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1, command=self.browse1)
        self.btnBrowse1.grid(row=0, column=0, padx=(20,20), pady=(40,0), sticky=NSEW)

        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1, command=self.browse2)
        self.btnBrowse2.grid(row=1, column=0, padx=(20,20), pady=(10,0), sticky=NSEW)

        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2, command=self.check)
        self.btnCheck.grid(row=2, column=0, padx=(20,20), pady=(10,0), sticky=NSEW)

        self.btnClose = Button(self.master, text="Close Program", width=12, height=2, command=self.close)
        self.btnClose.grid(row=2, column=1, padx=(0,0), pady=(10,0), sticky=E)

    def browse1(self):
        b1 = self.varEntry1.get()

    def browse2(self):
        b2 = self.varEntry2.get()

    def check(self):
        b1 = self.varEntry1.get()
        b2 = self.varEntry2.get()

    def close(self):
        self.master.destroy()




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
