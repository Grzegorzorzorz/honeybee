import os
import shutil

import output_handler

def clone(file_path, file_destination, quantity, name_template):
    print("Cloning files: \n \n \n")
    for x in range(0, quantity):
        name = name_template
        name = name.replace("%D", str(x))
        name = name.replace("%H", (hex(x).split("x")[-1]).upper())
        print(output_handler.full_bar(100, x + 1, quantity, name))
        shutil.copy2(file_path, os.path.join(file_destination, name))
    print("\nDone!")

def sub_dir_clone(file_path, file_destination_root, quantity, name_template, sub_directory_amount):
    print("Cloning files: \n \n")
    current_folder = 0
    for file_number in range(0, quantity):
        file_destination = os.path.join(file_destination_root, str(current_folder))
        name = name_template
        name = name.replace("%D", str(file_number))
        name = name.replace("%H", (hex(file_number).split("x")[-1]).upper())
        print(output_handler.full_bar(100, file_number + 1, quantity,  str(current_folder) + "/" + name))
        shutil.copy2(file_path, os.path.join(file_destination, name))
        if current_folder + 1 == sub_directory_amount:
            current_folder = 0
        else:
            current_folder = current_folder + 1
    print("\nDone!")

def make_directory(file_destination, quantity):
    print("Creating folders: \n \n")
    for x in range(0, quantity):
        name = str(x)
        print(output_handler.full_bar(100, x + 1, quantity, name))
        try:
            os.makedirs(os.path.join(file_destination, name))
        except:
            pass
            # Don't throw an exception if the file is already present
    print()