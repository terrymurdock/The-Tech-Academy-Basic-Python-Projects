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
#                 has been clicked it will take the user’s selected file path retained by
#                 the askdirectory() method and print it within your GUI’s text widget
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk

# Be sure to import our other modules
# so we can have access to them
import drillPg122_gui
import drillPg122_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(565, 100)  # (Height, Width)
        self.master.maxsize(565, 100)

        # This CenterWindow method will center our app on the user's screen
        drillPg122_func.center_window(self, 565, 100)
        self.master.title("Files and Folders Directory")
        self.master.configure(bg="#F0F0F0")

        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: drillPg122_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        drillPg122_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
