# by Robert Dobrowolski

import json
from operator import getitem
from GhPython import Component

# component descriptions
ghenv.Component.Description = "Create JSON object from data tree"
ghenv.Component.Params.Input[0].Description = "data tree to dump to JSON"
ghenv.Component.Params.Input[1].Description = "tree of keys for the JSON. {depth}(index)"
ghenv.Component.Params.Output[0].Description = "ready JSON as string"

def tree2list(tree):
    '''convert tree to list of lists'''
    out = []
    for branch in tree.Branches:
        thisbranch = []
        for item in branch:
            thisbranch.append(item)
        out.append(thisbranch)
    return out

def createNames(tree):
    '''create names based on tree paths'''
    
    # get the paths
    paths = [list(p) for p in tree.Paths]
    
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
    
    # create names from the paths
    allNames = []
    for f in flipped:
        allNames.append(["Item_"+str(i) for i in f])
    
    return allNames

def getFromDict(dataDict, mapList):
    '''get item from a nested dict using list of keys'''
    return reduce(getitem, mapList, dataDict)

def setInDict(dataDict, mapList, value):
    '''set item in a nested dict using list of keys'''
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value

#parse names
if names.DataCount == 0:
    parsednames = createNames(data)
else:
    parsednames = tree2list(names)

# prepare empty dict
output = {}

# map names or newnames to paths of the data tree
adresses = []
for path in data.Paths:
    adress = []
    for depth,index in enumerate(list(path)):
        adress.append(parsednames[depth][index])
    
    adresses.append(adress)

# create empty output dictionary
for adress in adresses:
    o = output
    for part in adress:
        o = o.setdefault(part,{})

# populate output dictionary
for path in data.Paths:
    adress = []
    for depth,index in enumerate(list(path)):
        adress.append(parsednames[depth][index])
    thisData = data.Branch(path)
    setInDict(output,adress,list(data.Branch(path)))

# dump output dict as a json
JSON = json.dumps(output)