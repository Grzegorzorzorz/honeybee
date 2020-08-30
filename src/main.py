import cloner
import input_handler
import output_handler

print("""
Honeybee File Cloning Utility V1.0
Copyright (C) Grzegorz Ciolek
-------------------------------
""")

confirmation = 0

while confirmation == 0:
    target = input_handler.get_file()
    name_template = input_handler.get_naming_conv()
    copy_amount = input_handler.get_quantity()
    output_directory = input_handler.get_output_dir()
    sub_dirs = input_handler.get_sub_dir_quantity()
    confirmation = input_handler.confirmation(
        target,
        name_template,
        copy_amount,
        output_directory,
        sub_dirs
    )

if sub_dirs != 0:
    cloner.make_directory(output_directory, sub_dirs)
    cloner.sub_dir_clone(target, output_directory, copy_amount, name_template, sub_dirs)
else:
    cloner.clone(target, output_directory, copy_amount, name_template)