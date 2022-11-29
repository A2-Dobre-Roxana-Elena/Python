import os
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "./deMonitorizatMomentam"

    def __init__(self, fisierDeMonitorizat):
        self.observer = Observer()
        DIRECTORY_TO_WATCH = fisierDeMonitorizat

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        print(event.event_type)
        #f.write(event.event_type + '\n')
        # ASTA MERGE DOAR LA FISIERE !!!

        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print("Received created event  %s." % event.src_path)
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(dt_string + "create,  fisier,  %s." % event.src_path + "\n")

        elif event.event_type == 'moved':
            print("Received modified event - %s." % event.src_path)
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(dt_string + "moved,  fisier,  - %s." % event.src_path + "\n")

        elif event.event_type == 'modified':
            print("Received modified event - %s." % event.src_path)
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(dt_string + "modified,  fisier,  - %s." % event.src_path + "\n")

        elif event.event_type == 'deleted':
            print("Received modified event - %s." % event.src_path)
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(dt_string + "deleted,  fisier,  - %s." % event.src_path + "\n")


path_Istoric = "./Istoric"
print("Buna, te rog sa introduci calea spre locatia pe care doresti sa o monitorizez.")
path_locatiaDeMonitorizat = input()
print("Locatia aleasa este: ", path_locatiaDeMonitorizat)

print("In mod predefinit istoricul va fi salvat in fisierul ce se afla la calea: ", os.path.abspath(path_Istoric))
print("Doriti sa schimbati fisierul unde va fi salvat istoricul?")
raspuns = input()

if raspuns.lower() == "da":
    print("Va rog introduceti calea spre fisierul unde va fi salvat istoricul:")
    pathIstoric = input()
    print("Modificarile au fost salvate", pathIstoric)

print("Daca veti dori sa opriti monitorizarea apasati tasta 'Q'")
print("Din acest moment incepe monitorizarea fisierului dorit.")
f = open("./Istoric", 'w')
f.write("DATETIME    OPERATIE    TIP-ITEM    ITEM\n")
w = Watcher(path_locatiaDeMonitorizat)
w.run()

"""
while raspuns != 'Q':
    raspuns = input()
"""
