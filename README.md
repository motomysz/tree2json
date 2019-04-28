# Tree2Json

*by Robert Dobrowolski*

Set of Grasshopper Components that allow to work with JavaScript Object Notation files.
Consists of four components.

1. Tree2Json
2. JsonPrettyPrint
3. JoinJsons
4. SaveJson

#### 1. Tree2Json
Main component. Converts Grasshopper Data Tree structure into JSON notation. Optionally names can be specified. If no names are supplied generic names (ie. *"Item_2"*) are made. Names should follow the structure in the hint.
Only non jagged trees can be exported. Every branch has to have an equal number of subbranches. In case of more complex tree structures **JoinJsons** component can be used.

#### 2. JsonPrettyPrint
Fomats Json string into pretty indented representation.
> Prettified string is no longer a valid notation.

#### 3. JoinJsons
Concatenates Json strings. Optionally names can be specified. If no names are given, top keys are concatenated on one level.

#### 4. SaveJson
Save the text file in the given directory.