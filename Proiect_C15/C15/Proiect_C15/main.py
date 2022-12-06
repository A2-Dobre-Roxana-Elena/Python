import os
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "./deMonitorizatMomentam"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(10)
                while 1:
                    for i in os.listdir("./deMonitorizatMomentam"):
                        if "./deMonitorizatMomentam" + "/" + i not in myDict.keys():
                            myDict["./deMonitorizatMomentam" + "/" + i] = os.stat("./deMonitorizatMomentam" + "/" + i)[7]
                        elif os.stat("./deMonitorizatMomentam" + "/" + i)[7] != myDict.get(
                                "./deMonitorizatMomentam" + "/" + i):
                            if os.path.isdir("./deMonitorizatMomentam" + "/" + i):
                                itemType = "folder"
                            else:
                                itemType = "fisier"
                            now = datetime.now()
                            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                            f.write(dt_string + 3 * tav + "access" + 2 * tav + itemType + 2 * tav + os.path.abspath(
                                "./deMonitorizatMomentam" + "/" + i) + "\n")
                            print(dt_string + 3 * tav + "access" + 2 * tav + itemType + 2 * tav + os.path.abspath(
                                "./deMonitorizatMomentam" + "/" + i) + "\n")
                            myDict.update(
                                {"./deMonitorizatMomentam" + "/" + i: os.stat("./deMonitorizatMomentam" + "/" + i)[7]})
        except:
            self.observer.stop()

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):

        itemType = "ceva"
        if os.path.isdir(event.src_path) and event.is_directory:
            itemType = "director"
        elif os.path.isfile(event.src_path) and not event.is_directory:
            itemType = "fisier"
        elif itemType == "ceva":
            if '.' in event.src_path:
                itemType = "fisier"
            else:
                itemType = "director"

        if event.event_type == 'created':
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(dt_string + 3*tav + "create" + 2*tav + itemType + 2*tav + os.path.abspath(event.src_path) + "\n")
            print(dt_string + 3*tav + "create" + 2*tav + itemType + 2*tav + os.path.abspath(event.src_path) + "\n")

        elif event.event_type == 'moved':
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(dt_string + 3*tav + "moved" + 2*tav + itemType + 2*tav + os.path.abspath(event.src_path) + "\n")
            print(dt_string + 3*tav + "moved" + 2*tav + itemType + 2*tav + os.path.abspath(event.src_path) + "\n")

        elif event.event_type == 'modified':
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(dt_string + 3*tav + "write" + 2*tav + itemType + 2*tav + os.path.abspath(event.src_path) + "\n")
            print(dt_string + 3*tav + "write" + 2*tav + itemType + 2*tav + os.path.abspath(event.src_path) + "\n")

        elif event.event_type == 'deleted':
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(dt_string + 3*tav + "delete" + 2*tav + itemType + 2*tav + os.path.abspath(event.src_path) + "\n")
            print(dt_string + 3*tav + "delete" + 2*tav + itemType + 2*tav + os.path.abspath(event.src_path) + "\n")


f = open("./Istoric", 'w')
f.write("DATETIME                   OPERATIE        TIP-ITEM        ITEM\n")
tav = "    "
myDict = {}
for i in os.listdir("./deMonitorizatMomentam"):
    if i not in myDict.keys():
        myDict["./deMonitorizatMomentam"+"/"+i] = os.stat("./deMonitorizatMomentam"+"/"+i)[7]
w = Watcher()
w.run()
