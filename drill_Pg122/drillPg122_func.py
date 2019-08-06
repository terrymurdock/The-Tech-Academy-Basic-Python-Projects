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

import os
from tkinter import messagebox
from tkinter.filedialog import askdirectory


def center_window(self, w, h):  # pass in teh tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    center_geo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return center_geo


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

# ====================================================================


def get_directory(self):
    dirname = askdirectory()
    if dirname:
        self.varDirName.set(dirname)


def close(self):
    self.master.destroy()


if __name__ == "__main__":
    pass
