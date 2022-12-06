import os
from datetime import datetime

f = open("./Istoric", 'w')
f.write("DATETIME                   OPERATIE        TIP-ITEM        ITEM\n")
tav = "    "
id = 1
myDict = {}
DirectoryToWatch = "./deMonitorizatMomentam"
for i in os.listdir(DirectoryToWatch):
    if i not in myDict.keys():
        myDict[DirectoryToWatch + "/" + i] = [os.stat(DirectoryToWatch + "/" + i)[7], id,
                                              os.stat(DirectoryToWatch + "/" + i)[6]]
        id += 1
try:
    while 1:
        for i in os.listdir(DirectoryToWatch):
            if os.path.isdir(DirectoryToWatch + "/" + i):
                itemType = "folder"
            else:
                itemType = "fisier"
            try:
                if DirectoryToWatch + "/" + i not in myDict.keys():
                    myDict[DirectoryToWatch + "/" + i] = [os.stat(DirectoryToWatch + "/" + i)[7], id,
                                                          os.stat(DirectoryToWatch + "/" + i)[6]]
                    id += 1
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    f.write(dt_string + 3 * tav + "create" + 2 * tav + itemType + 2 * tav + os.path.abspath(
                        DirectoryToWatch + "/" + i) + "\n")
                    print(dt_string + 3 * tav + "create" + 2 * tav + itemType + 2 * tav + os.path.abspath(
                        DirectoryToWatch + "/" + i) + "\n")
                elif os.stat(DirectoryToWatch + "/" + i)[7] != myDict.get(DirectoryToWatch + "/" + i)[0]:
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    f.write(dt_string + 3 * tav + "access" + 2 * tav + itemType + 2 * tav + os.path.abspath(
                        DirectoryToWatch + "/" + i) + "\n")
                    print(dt_string + 3 * tav + "access" + 2 * tav + itemType + 2 * tav + os.path.abspath(
                        DirectoryToWatch + "/" + i) + "\n")
                    if os.stat(DirectoryToWatch + "/" + i)[6] > myDict.get(DirectoryToWatch + "/" + i)[2]:
                        now = datetime.now()
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        f.write(dt_string + 3 * tav + "write " + 2 * tav + itemType + 2 * tav + os.path.abspath(
                            DirectoryToWatch + "/" + i) + "\n")
                        print(dt_string + 3 * tav + "write " + 2 * tav + itemType + 2 * tav + os.path.abspath(
                            DirectoryToWatch + "/" + i) + "\n")
                    myDict.update(
                        {DirectoryToWatch + "/" + i: [os.stat(DirectoryToWatch + "/" + i)[7], id,
                                                      os.stat(DirectoryToWatch + "/" + i)[6]]})
            except FileNotFoundError:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                f.write(dt_string + 3 * tav + "delete" + 2 * tav + itemType + 2 * tav + os.path.abspath(
                    DirectoryToWatch + "/" + i) + "\n")
                print(dt_string + 3 * tav + "delete" + 2 * tav + itemType + 2 * tav + os.path.abspath(
                    DirectoryToWatch + "/" + i) + "\n")
                myDict.pop(DirectoryToWatch + "/" + i)
except:
    print("S-a incheiat monitorizarea")
