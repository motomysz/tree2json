# by Robert Dobrowolski

from Grasshopper import DataTree
from Grasshopper.Kernel.Data import GH_Path

# component descriptions
ghenv.Component.Description = "Helper, shows how names should be structured to match tree structure"
ghenv.Component.Params.Input[0].Description = "data tree to lookup"
ghenv.Component.Params.Output[0].Description = "Names should be structured like this tree"

# parse tree paths to a matrix
paths = [list(p) for p in data.Paths]

# assert if the tree is jagged
jagged = False
if not all([(len(l)== len(paths[0])) for l in paths]):
    hint = "The data tree is jagged. It won't work."
    jagged = True

# create new matrix
flipped = []
for index in paths[0]:
    flipped.append([])

# populate the new matrix
for path in paths:
    for i,index in enumerate(path):
        flipped[i].append(index)

# distinct items in flipped matrix
flipped = [list(set(f)) for f in flipped]

# make a tree out of flipped matrix
output = DataTree[int]()
for i,f in enumerate(flipped):
    path = GH_Path(i)
    output.AddRange(f,path)

# output
if not jagged:
    hint = output