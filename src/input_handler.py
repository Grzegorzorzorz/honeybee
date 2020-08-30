import sys
import os

def get_file():
    # Ask user to place file in bin directory
    print("File loading:")
    sys.stdout.write("    Please place the file to be cloned in the bin \
directory, then press enter.")
    input()
    # Get the bin path and write the names to a variable
    bin_path = (
        os.path.join(os.path.dirname(__file__), "../bin")
    )
    bin_files = os.listdir(bin_path)
    print(f"    {len(bin_files)} files were found!")
    print("    Make a selection from the files below.")
    # Display all files found in the bin directory.
    for x in range(0, len(bin_files)):
        print(f"        {x}.    {bin_files[x]}")
    print()
    file_index = int(input(" > "))
    target_file = os.path.join(bin_path, bin_files[file_index])
    print(f"Selected '{bin_files[file_index]}'. \n")
    return target_file

def get_naming_conv():
    print("""Name formatting:
    Please enter a name format for all of the copies, where %N is the number of
    the copy i.e.
    
    If you were to input 'output-%N.txt', the 56th copy would be called \
'output-55.txt'

    Placeholder tags:
    %D -- The current iteration in denary (base 10)
    %H -- The current iteration in hex (base 16)

    Please don't use any characters which aren't permitted by your file system,
    since this will cause the program to fail.
    
    Leave blank for the default: 'output-%H'.
    """)
    name_template = input(" > ")
    print()
    if name_template == "":
        name_template = "output-%H"
    return name_template

def get_quantity():
    print("Quantity management")
    print("    Input number of copies.")
    print()
    quantity = int(input(" > "))
    print()
    return quantity

def get_output_dir():
    print("Output location:")
    print("    Please enter the output directory.")
    print("    Do not use shorthand such as '~/'")
    print("    Leave blank for default directory.")
    print()
    output_path = input(" > ")
    if output_path == "":
        output_path = os.path.join(os.path.dirname(__file__), "../dst")
    return output_path

def get_sub_dir_quantity():
    print("Sub directories:")
    print("    Type the amount of sub directories needed.")
    print("    If none are needed, type 0.")
    print()
    amount = int(input(" > "))
    print()
    return amount

def confirmation(target_file, name_template, quantity, output_path, sub_directories):
    print(f"""Confirmation:
    Source file:        {target_file}
    Name template:      {name_template}
    No. of copies:      {quantity}
    Output folder:      {output_path}
    Sub directories:    {sub_directories}
    """)
    user_input = input("Are all details correct? (Y/n)> ")
    if user_input.upper() != "N":
        return 1
    else:
        return 0 