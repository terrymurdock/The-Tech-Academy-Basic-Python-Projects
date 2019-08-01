

import os
import time

for file in os.listdir("C:\python_projects"):
    if file.endswith(".txt"):
        file = os.path.join("C:\python_projects",file)
        print("File ", file, "\t was modfied on\t %s" % time.ctime(os.path.getmtime(str(file))))
