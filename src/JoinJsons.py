# by Robert Dobrowolski

import json

# component descriptions
ghenv.Component.Description = "Join one or more JSON files. Optipnally assign new keys"
ghenv.Component.Params.Input[0].Description = "JSON strings as list"
ghenv.Component.Params.Input[1].Description = "[optional keys]"
ghenv.Component.Params.Output[0].Description = "joined JSON strings"

# check if names are to be used and if they are correct
named = True if names else False
if named:
    matches = len(names)==len(jsons)

# load parts as dictionaries
datadicts = [json.loads(d) for d in jsons]

output = {}

# join dictinaries, using names or by the topmost key
if named and matches:
    for s,n in zip(datadicts,names):
        output[n]=s
    
else:
    for s in datadicts:
        for k,v in s.items():
            output[k] = v

# outputs
if named and not matches:
    JSON = "data and names are not matching"
else:
    JSON = json.dumps(output)