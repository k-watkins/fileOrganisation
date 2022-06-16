import files_copy
from files_copy import *

files_copy.generate_main_window()


"""
source_folder = '/Users/Kyle/Documents/test'
destination_folder = '/Users/Kyle/Documents/testtoo'

file_directory = os.listdir(source_folder)
dest_file_directory = os.listdir(destination_folder)
images = (".jpg", ".png", ".jpeg", ".bmp")
documents = (".doc", ".docx", ".txt")
sound = (".mp3", ".acc", ".wma")
video = (".mp4", ".wmv", ".avi", ".mkv")

# TODO  fileType = [(".jpg", ".png", ".jpeg", ".bmp"), (".doc", ".docx", ".txt")]
os.chdir(source_folder)

for files in file:
    while len(fileType):
        if files.endswith(fileType[i]):
            shutil.move(files, dest)
            print(f"{files} moved.")
            print(files)



# TODO loop to iterate through file types - through all indexes of the array of objects which is filetype enum
# TODO new variable to test true or false
# TODO clear directory function if true false


# reads each file in directory
for file_name in file_directory:
    # Moves documents
    if file_name.endswith(documents):
        shutil.move(file_name, destination_folder)
        print(f"{file_name} moved.")
    # Moves photos
    if file_name.endswith(images):
        shutil.move(file_name, destination_folder)
        print(f"{file_name} moved.")
    # Moves sounds
    if file_name.endswith(sound):
        shutil.move(file_name, destination_folder)
        print(f"{file_name} moved.")
    # Moves Videos
    if file_name.endswith(video):
        shutil.move(file_name, destination_folder)
        print(f"{file_name} moved.")

"""

