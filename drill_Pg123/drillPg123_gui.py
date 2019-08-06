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

import tkinter as tk
from tkinter import *

# Be sure to import our other modules
# so we can have access to them
import drillPg123_func


def load_gui(self):
    self.varDirName = StringVar()
    self.varDesName = StringVar()

    self.lblSourceDir = Label(self.master, text='Source Directory')
    self.lblSourceDir.grid(row=0, column=0, columnspan=2, padx=(20, 0), pady=(20, 0), sticky=N + W)

    self.lblDestDir = Label(self.master, text='Destination Directory')
    self.lblDestDir.grid(row=2, column=0, columnspan=2, padx=(20, 0), pady=(10, 0), sticky=N + W)

    self.lblDisplay = Label(self.master, text='')
    self.lblDisplay.grid(row=4, column=1, padx=(10, 0), pady=(10, 0), sticky=N + W)

    self.txt_dirFolder = tk.Entry(self.master, text=self.varDirName, width=65)
    self.txt_dirFolder.grid(row=1, column=1, columnspan=2, padx=(0, 0), pady=(10, 0), sticky=N + E + W)

    self.txt_desFolder = tk.Entry(self.master, text=self.varDesName, width=65)
    self.txt_desFolder.grid(row=3, column=1, columnspan=2, padx=(0, 0), pady=(10, 0), sticky=N + E + W)

    self.btnBrowseDir = tk.Button(self.master, text="Browse...", width=12, height=1,
                                  command=lambda: drillPg123_func.get_directory(self))
    self.btnBrowseDir.grid(row=1, column=0, padx=(20, 20), pady=(10, 0), sticky=N + E + W + S)

    self.btnBrowseDes = tk.Button(self.master, text="Browse...", width=12, height=1,
                                  command=lambda: drillPg123_func.get_destination(self))
    self.btnBrowseDes.grid(row=3, column=0, padx=(20, 20), pady=(10, 0), sticky=N + E + W + S)

    self.btnChkMove = tk.Button(self.master, text="Run Program", width=12, height=2, wraplength=100,
                                command=lambda: [drillPg123_func.check_files(), drillPg123_func.create_db(),
                                                 drillPg123_func.addto_db(), drillPg123_func.move_files(),
                                                 drillPg123_func.submit(self)])
    self.btnChkMove.grid(row=4, column=0, padx=(20, 20), pady=(10, 0), sticky=N + E + W + S)

    self.btnClose = tk.Button(self.master, text="Close Program", width=12, height=2,
                              command=lambda: drillPg123_func.close(self))
    self.btnClose.grid(row=4, column=2, padx=(0, 0), pady=(10, 0), sticky=E)


if __name__ == "__main__":
    pass
