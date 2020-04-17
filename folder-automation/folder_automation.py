import os
import shutil

folder_to_track = "/Users/lucassilva/Downloads"
new_destination = "/Users/lucassilva/Developer/python/folder_automation/content"

os.makedirs("/Users/lucassilva/Developer/python/folder_automation/content", exist_ok=True)

for filename in os.listdir(folder_to_track):
    filename_parts = filename.split('.')
    extension = filename_parts[-1]
    is_directory = len(filename_parts) == 1
    # print(is_directory)
    src = folder_to_track + "/" + filename
    if (not is_directory and extension != 'app'):
        shutil.copyfile(src, new_destination + "/" + filename)
