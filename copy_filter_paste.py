from os import listdir, path, mkdir
from os.path import isfile, join

folder = input()
parent_directory = "C:\\Users\\User\\Desktop\\"
file_directory = parent_directory + folder
new_folder = parent_directory + folder + "1"
files = []


def extract(file_path):
    text_file = open(path.join(file_directory, file_path), 'r')
    lines = [f for f in text_file.readlines() if "xpath=" in f and not any(x in f for x in ['@data-qa', '@name'])]
    open(path.join(new_folder, file_path), 'w').writelines(lines)
    print("written to : " + path.join(new_folder, file_path))


if path.exists(parent_directory):
    files = [f for f in listdir(file_directory) if isfile(join(file_directory, f))]
    if not path.exists(new_folder):
        mkdir(new_folder)
    for file in files:
        extract(file)
else:
    print("directory path is not correct.")

