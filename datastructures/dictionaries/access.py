# ________________________________________________________________________________________________
# Accessing Items
# ------------------------------------------------------------------------------------------------
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# ------------------------------------------------------------------------------------------------
# .get()
# ____________________________
print("____________________________________________________0")
dicts = {"A": "sting", "B": 2, "C": True}
dicts["D"] = "___"
print(dicts.get("A"))
# ------------------------------------------------------------------------------------------------
# keys()
# ____________________________
print("____________________________________________________1")
dicts = {"A": "sting", 1: "B", "C": True}
print(dicts.keys())
# ------------------------------------------------------------------------------------------------
# values()
# ____________________________
print("____________________________________________________2")
dicts = {"A": "sting", "B": 1, "C": True}
print(dicts.values())
# ------------------------------------------------------------------------------------------------
# items()
# ____________________________
# will return each item in a dictionary, as tuples in a list.
print("____________________________________________________3")
dicts = {"A": "sting", "B": 1, "C": True}
print(dicts.items())
# ________________________________________________________________________________________________
# if Key Exists
# ____________________________
#
print("____________________________________________________4")
dicts = {"brand": "Ford", "model": "Mustang", "year": 1964}
if "model" in dicts:
    print("Yes, 'model' is one of the keys")
print("_______________________________________________")

