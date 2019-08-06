# Python Ver. 3.7.4
#
# Author:       Terry Murdock
#
# Purpose:      Drill Description:
#               Your new script will need to provide the user with a graphical user interface that includes two
#               buttons allowing the user to browse their own system and select a source directory and a destination
#               directory. Your script should also show those selected directory paths in their own corresponding text
#               fields.
#               Next, your script will need to provide a button for the user to execute a function that should iterate
#               through the source directory, checking for the existence of any files that end with a “.txt” file
#               extension and if so, cut the qualifying files and paste them within the selected destination directory.
#               Finally, your script will need to record the file names that were moved and their corresponding
#               modified time-stamps into a database and print out those text files and their modified time-stamps to
#               the console.
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk

# Be sure to import our other modules
# so we can have access to them
import drillPg123_gui
import drillPg123_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(555, 225)  # (Height, Width)
        self.master.maxsize(555, 225)

        # This CenterWindow method will center our app on the user's screen
        drillPg123_func.center_window(self, 555, 225)
        self.master.title("Files and Folders Directory")
        self.master.configure(bg="#F0F0F0")

        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: drillPg123_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        drillPg123_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
