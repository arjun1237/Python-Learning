from os import listdir, walk
from os.path import join, isdir, isfile

files = []
list_to_write = []
unique_list1 = []
unique_list2 = []
path_n = "C:\\Users\\User\\Desktop\\test\\"
file_to_write = "C:\\Users\\User\\Desktop\\Test.txt"
file_to_write_unique1 = "C:\\Users\\User\\Desktop\\unique1.txt"
file_to_write_unique2 = "C:\\Users\\User\\Desktop\\unique2.txt"
strs_to_look_for = ['search-pagecode', 'selected-record-three-dot-menu-action']
for i in range(len(strs_to_look_for)):
    strs_to_look_for[i] = strs_to_look_for[i].lower()
# open(file_to_write, 'w').close()


def load_data(path_file):
    with open(path_file, "r") as data:
        for line in data:
            line = line.strip()
            line_lower = line.lower()
            for str_search in strs_to_look_for:
                if str_search in line_lower:
                    keyword_line = line[line_lower.find(str_search):].split(' ', 1)
                    key1 = keyword_line[0]
                    key2 = keyword_line[1].strip()
                    key_combo1 = key1 + '-' + key2 + '\n'
                    key_combo2 = '\t' + key1 + '\t' + key2 + '\n'
                    if key_combo1 not in list_to_write:
                        list_to_write.append(key_combo1)
                        list_to_write.append(key_combo2)
                        unique_list1.append(key_combo2.lstrip())
                        unique_list2.append('\t' + key_combo1)


for r, d, f in walk(path_n):
    for file in f:
        if file.endswith('.robot'):
            load_data(join(r, file))

new_file = open(file_to_write, 'w')
new_file.writelines(list_to_write)
new_file.close()

unique_file1 = open(file_to_write_unique1, 'w')
unique_file1.writelines(unique_list1)
unique_file1.close()

unique_file2 = open(file_to_write_unique2, 'w')
unique_file2.writelines(unique_list2)
unique_file2.close()

print('done')
