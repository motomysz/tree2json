# by Robert Dobrowolski

from GhPython import Component
from json import loads

# component descriptions
ghenv.Component.Description = "Pretty Print Json string."
ghenv.Component.Params.Input[0].Description = "Json string to format"
ghenv.Component.Params.Output[0].Description = "Formatted Json string."

# global variable to store depth of dictionary for printing
DEPTH = 0

# global variable to store if currently inside of value
VALUE = False

# function that returns pretty representation of a dictionary
def dprint(dictionary):
    ''' returns a pretty representation of a dictionary '''
    global DEPTH
    global VALUE
    out = ""
    if not (isinstance(dictionary,dict) or isinstance(dictionary,list)):
        return str(dictionary)
    for letter in str(dictionary):
        out += letter
        if letter == "{" or letter == "[":
            DEPTH += 1
            out += "\n"
            out += "    "*DEPTH
        elif letter == "}" or letter == "]":
            out = out[:-1]
            DEPTH -= 1
            out += "\n"
            out += "    "*DEPTH
            out += letter
        elif letter == "," and not VALUE:
            out += "\n"
            out += "    "*DEPTH
        elif letter == "\'":
            VALUE = not VALUE
    return out

PPrint = dprint(loads(JSON))