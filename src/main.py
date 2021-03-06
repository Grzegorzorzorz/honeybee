import src.cloner
import src.input_handler

print("""
Honeybee File Cloning Utility V1.1
Copyright (C) Grzegorz Ciolek
-------------------------------
""")
def run():
    confirmation = 0
    while confirmation == 0:
        target = src.input_handler.get_file()
        if target == None:
            exit()
        name_template = src.input_handler.get_naming_conv()
        copy_amount = src.input_handler.get_quantity()
        output_directory = src.input_handler.get_output_dir()
        sub_dirs = src.input_handler.get_sub_dir_quantity()
        confirmation = src.input_handler.confirmation(
            target,
            name_template,
            copy_amount,
            output_directory,
            sub_dirs
        )

    if sub_dirs != 0:
        src.cloner.make_directory(output_directory, sub_dirs)
        src.cloner.sub_dir_clone(target, output_directory, copy_amount, name_template, sub_dirs)
    else:
        src.cloner.clone(target, output_directory, copy_amount, name_template)