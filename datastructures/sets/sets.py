# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
print("________________________________________________")
set1 = {"a", "b", "c", "a", "b"}
print(set1)
print("________________________________________________")
print(type(set1))
print("________________________________________________")
print(len(set1))
print("________________________________________________")

print("________________________________________________")
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
print("________________________________________________")
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("________________________________________________")
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)
print("________________________________________________")
#________________________________________________________________________________________________
print("________________________________________________")
thisset = {"a", "b", "c"}
thisset.add("1")
print(thisset)
print("________________________________________________")
thisset = {"a", "b", "c"}
tropical = {"1", "2", "3"}
thisset.update(tropical)
print(thisset)
print("________________________________________________")
thisset = {"a", "b", "c"}
mylist = ["1", "2"]
thisset.update(mylist)
print(thisset)
print("________________________________________________")
#________________________________________________________________________________________________
print("________________________________________________")
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
print("________________________________________________")
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
print("________________________________________________")
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
print("________________________________________________")
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
print("________________________________________________")
#________________________________________________________________________________________________
print("________________________________________________")
# Loop Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
print("________________________________________________")
