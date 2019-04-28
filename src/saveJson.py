# by Robert Dobrowolski

# component descriptions
ghenv.Component.Description = "Save text to file"
ghenv.Component.Params.Input[0].Description = "Toogle the saving."
ghenv.Component.Params.Input[1].Description = "File path."
ghenv.Component.Params.Input[2].Description = "Text to put in file."


import sys
import os

if save:
    f = open(file,"w+")
    f.write(contents)
    f.close()