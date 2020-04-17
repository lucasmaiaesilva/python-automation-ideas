from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip3 install watchdog for these package to work

import os
import shutil
import time

folder_to_track = "/Users/lucassilva/Downloads"
new_destination = "/Users/lucassilva/Developer/python/folder_automation/content"

os.makedirs("/Users/lucassilva/Developer/python/folder_automation/content", exist_ok=True)


if __name__ == "__main__":
    def update_folder():
        for filename in os.listdir(folder_to_track):
            filename_parts = filename.split('.')
            extension = filename_parts[-1]
            is_directory = len(filename_parts) == 1
            src = folder_to_track + "/" + filename
            if (not is_directory and extension != 'app'):
                shutil.copyfile(src, new_destination + "/" + filename)

    def on_modified_folder(event):
        update_folder()
        print("the folder has been modified")

    event_handler = FileSystemEventHandler()
    event_handler.on_modified = on_modified_folder
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
