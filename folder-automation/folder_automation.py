from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip3 install watchdog for these package to work

import os
import shutil
import time

folder_to_track = "/Users/lucassilva/Downloads"
new_destination = "/Users/tmp/content"

os.makedirs(new_destination, exist_ok=True)

def update_folder():
    for filename in os.listdir(folder_to_track):
        filename_parts = filename.split('.')
        extension = filename_parts[-1]
        is_directory = len(filename_parts) == 1
        src = folder_to_track + "/" + filename
        if (not is_directory and extension != 'app'):
            path_with_extension = new_destination + "/" + extension
            os.makedirs(path_with_extension, exist_ok=True)
            print("Creating dir: {}".format(extension))
            shutil.copyfile(src, path_with_extension + "/" + filename)

def on_modified_folder(event):
    update_folder()
    print("the folder has been modified")


if __name__ == "__main__":
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
