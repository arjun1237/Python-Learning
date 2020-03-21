# traversing a path and finding all files in it without using os.walk

def traverse_file(path_name):
    for file in listdir(path_name):
        file_fold = join(path_name, file)
        if isdir(file_fold):
            traverse_file(file_fold)
        elif isfile(file_fold):
            print(path_name + '\\' + file)


traverse_file(path_n)
