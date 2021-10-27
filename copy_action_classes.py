import shutil, os

def find_all_files_that_match_pattern(pattern, path):
    import os, fnmatch
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(pattern):
                result.append(os.path.join(root, name))
    #find_all_files_that_match_pattern('*.txt', '/path/to/dir')
    return result

action_class_list = ["023","028","031","034","035","036","038","040","041","042","043","044","045","046","047","048","049","059","060","069","070","071","085","086","116"]


path = os.getcwd() + "/data/nturgbd_raw/nturgb+d_skeletons/"
list_files = []
for c in action_class_list:
    pattern = "A"+c+".skeleton"
    list_files.append(find_all_files_that_match_pattern(pattern, path))

dest_folder = os.getcwd() + "/data/selected_action_classes/"
for f in list_files[0]:
    shutil.copy(f,dest_folder)


print("All good!")
 