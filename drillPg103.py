

import sqlite3

# Create database
conn = sqlite3.connect('drillPg103.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filelist( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('drillPg103.db')

#Add .txt files to dB, then comment out so it does not add them again
"""
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    for file in fileList:
        if file.endswith(".txt"):
            cur.execute("INSERT INTO tbl_filelist(col_file) VALUES (?)", (file,))
    conn.commit()
conn.close()
"""

#Print to console
conn = sqlite3.connect('drillPg103.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_filelist")
    varFile = cur.fetchall()
    for file in varFile:
        print(file)
