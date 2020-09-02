import os
import src.main

# Check if the bin and dst directories are present, and if not, generate them.
if os.path.isdir(os.path.join(os.path.dirname(__file__), "bin")) == False:
    print("'bin' directory not found. Generating...")
    os.makedirs(os.path.join(os.path.dirname(__file__), "bin"))
if os.path.isdir(os.path.join(os.path.dirname(__file__), "dst")) == False:
    print("'dst' directory not found. Generating...")
    os.makedirs(os.path.join(os.path.dirname(__file__), "dst"))

# Start the program.
src.main.run()