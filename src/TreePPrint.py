# by Robert Dobrowolski

from GhPython import Component

# component descriptions
ghenv.Component.Description = "Pretty Print a Data Tree"
ghenv.Component.Params.Input[0].Description = "data tree to format"
ghenv.Component.Params.Output[0].Description = "formatted data tree"

output = ""

for p,b in zip(tree.Paths,tree.Branches):
    output += "_"*6
    output += str(p)
    output += "\n"
    for item in b:
        output += str(item)
        output += "\n"
pretty = output