# In dumps function what are the parameters that 
# we have and what do they do, explain with small program

# Dumps() function: If you have a Python object, 
# you can convert it into a JSON string by using the json.dumps() method.

# In Dumps() function has various parameter

# 1. USE the indent parameter to define the numbers of indents:
# use four indents to make it easier to read the result:
# 2. USE the separators is used to separates the key form values 
# by using separator symbol . space separate the objects
# space = space separate the keys from their values.
# 3. Use the sort_keys parameter to specify if the result should be sorted or not:
# sort the result alphabetically by keys:

import json

x = {
  "name":"Yuvraj",
  "age":23,
  "married":False,
  "pets":None,
  "food":[
    {"a": "Buger", "b": "shake", "c" : "momos"}
  ]
}

print(json.dumps(x, indent=4,separators=(". ", " = "),sort_keys=True))