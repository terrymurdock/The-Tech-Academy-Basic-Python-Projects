import os


def writeData():
    data = '\nHello world!'
    with open('test_Pg98.txt', 'a') as f:
        f.write(data)
        f.close()


def openFile():
    with open('test_Pg98.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()




if __name__ == "__main__":
    writeData()
    openFile()
