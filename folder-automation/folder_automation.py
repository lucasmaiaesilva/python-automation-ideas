from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip3 install watchdog for these package to work

import os
import shutil
import time

folder_to_track = "/Users/lucassilva/Downloads"
new_destination = "/Users/lucassilva/Developer/python/folder_automation/content"

os.makedirs("/Users/lucassilva/Developer/python/folder_automation/content", exist_ok=True)

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            filename_parts = filename.split('.')
            extension = filename_parts[-1]
            is_directory = len(filename_parts) == 1
            # print(is_directory)
            src = folder_to_track + "/" + filename
            if (not is_directory and extension != 'app'):
                shutil.copyfile(src, new_destination + "/" + filename)

event_handler = MyHandler()
Observer().schedule(event_handler, folder_to_track, recursive=True)
Observer().start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    Observer().stop()

Observer().join()
