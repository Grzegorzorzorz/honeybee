import os
import src.main

if os.path.isdir(os.path.join(os.path.dirname(__file__), "../bin")) == False:
    os.makedirs("bin")
if os.path.isdir(os.path.join(os.path.dirname(__file__), "../dst")) == False:
    os.makedirs("dst")

src.main.run()