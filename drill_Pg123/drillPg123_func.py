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

import os
import time
import shutil
import sqlite3
from tkinter import messagebox
from tkinter.filedialog import askdirectory


def center_window(self, w, h):  # pass in the tkinter frame (master) reference and the w and h
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


# Browse file directories for source and set in txt_dirFolder field
def get_directory(self):
    global dirname
    dirname = askdirectory()
    if dirname:
        self.varDirName.set(dirname)


# Browse file directories for destination and set in txt_desFolder field
def get_destination(self):
    global desname
    desname = askdirectory()
    if desname:
        self.varDesName.set(desname)


# ===========================================================================================================
# Find files with .txt extension in source; move to destination; print to console; create db and record files
# ===========================================================================================================
def check_files():
    for file in os.listdir("{}".format(dirname)):
        if file.endswith(".txt"):
            file = os.path.join("{}".format(dirname), file)
            print("File ", file, "\t was modified on\t %s" % time.ctime(os.path.getmtime(str(file))))


def create_db():
    conn = sqlite3.connect('textfiles.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_filelist( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_file TEXT, \
            col_modtime \
            )")
        conn.commit()
    conn.close()

def addto_db():
    conn = sqlite3.connect('textfiles.db')
    with conn:
        cur = conn.cursor()
        for file in os.listdir("{}".format(dirname)):
            if file.endswith(".txt"):
                file = os.path.join("{}".format(dirname), file)
                cur.execute("INSERT INTO tbl_filelist(col_file, col_modtime) VALUES (?, ?)", (file,"%s" % time.ctime(os.path.getmtime(str(file)))))
        conn.commit()
    conn.close()


# Move files with .txt extension in source to destination
def move_files():
    destination = ("{}".format(desname))
    for file in os.listdir("{}".format(dirname)):
        if file.endswith(".txt"):
            file = os.path.join("{}".format(dirname), file)
            shutil.move(file, destination)


def submit(self):
    self.lblDisplay.config(text='Success!!!\n Test files printed to console, entered into database,\n and moved to'
                                ' Destination Directory.')


def close(self):
    self.master.destroy()


if __name__ == "__main__":
    pass
