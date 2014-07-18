# encoding:utf-8
__author__ = 'luowei'

#字典

d = {"duck":"eeg","water":"blue"}
print d["duck"] # eeg
print d["water"] # blue

del d["water"]
d["back"] = "rug"
print d # {'back': 'rug', 'duck': 'eeg'}

print d.keys() # ['back', 'duck']
print d.values() # ['rug', 'eeg']
print d.items() # [('back', 'rug'), ('duck', 'eeg')]

print d.has_key("duck") # True
print d.has_key("span") # False

d["man"]="gentleMan"
print d # {'man': 'gentleMan', 'back': 'rug', 'duck': 'eeg'}

del d["back"]
print d # {'man': 'gentleMan', 'duck': 'eeg'}

d.clear()
print d # {}

# dictionary的key必须是immutable(不可变)
d2 = {
    "name":"Luowei",
      "age":25,
      ("hello","world"):1,
      20:"yes",
      "flag":["red","white","blue"]
}
print d2["flag"] # ['red', 'white', 'blue']




