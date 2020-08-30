import os
import src.main

if os.path.isdir(os.path.join(os.path.dirname(__file__), "bin")) == False:
    os.makedirs(os.path.join(os.path.dirname(__file__), "bin"))
if os.path.isdir(os.path.join(os.path.dirname(__file__), "dst")) == False:
    os.makedirs(os.path.join(os.path.dirname(__file__), "dst"))

src.main.run()