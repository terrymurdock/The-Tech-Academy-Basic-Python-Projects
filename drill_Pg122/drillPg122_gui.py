# Python Ver. 3.7.4
#
# Author:       Terry Murdock
#
# Purpose:      Drill Pg122
#               For this drill, you will need to write a script that creates a GUI
#               with a button widget and a text widget. Your script will also include
#               a function that when it is called will invoke a dialog modal which will
#               allow users with the ability to select a folder directory from their
#               system. Finally, your script will show the user’s selected directory
#               path into the text field.
#               - use the askdirectory() method from the Tkinter module
#               - have a function linked to the button widget so that once the button
#                 has been clicked will take the user’s selected file path retained by
#                 the askdirectory() method and print it within your GUI’s text widget
#
# Tested OS:    This code was written and tested to work with Windows 10.

import tkinter as tk
from tkinter import *

# Be sure to import our other modules
# so we can have access to them
import drillPg122_func


def load_gui(self):

    self.varDirName = StringVar()

    self.txt_selFolder = tk.Entry(self.master, text=self.varDirName, width=65)
    self.txt_selFolder.grid(row=0, column=1, padx=(0, 0), pady=(20, 0), sticky=N + E + W)

    self.btnBrowse = tk.Button(self.master, text="Browse...", width=12, height=1,
                               command=lambda: drillPg122_func.get_directory(self))
    self.btnBrowse.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky=N + E + W + S)

    self.btnClose = tk.Button(self.master, text="Close", width=12, height=1,
                              command=lambda: drillPg122_func.close(self))
    self.btnClose.grid(row=1, column=1, padx=(0, 0), pady=(10, 0), sticky=E)


if __name__ == "__main__":
    pass
