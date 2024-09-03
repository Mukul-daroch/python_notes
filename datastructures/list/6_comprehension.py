print("________________________________________________")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list = []
for x in fruits:
    if "a" in x:
        list.append(x)
print(fruits)

print(list, "\n", "________________________________________________")
# note list = [expression for item in iterable if condition == True]
list = [x for x in fruits if "a" in x]
print(list, "\n", "________________________________________________")
list = [x for x in fruits if x != "apple"]
print(list, "\n", "________________________________________________")
list = [x for x in fruits]
print(list, "\n", "________________________________________________")
list = [x for x in range(10)]
print(list, "\n", "________________________________________________")
list = [x for x in range(10) if x < 5]
print(list, "\n", "________________________________________________")
list = [x.upper() for x in fruits]
print(list, "\n", "________________________________________________")
list = ["hello" for x in fruits]
print(list, "\n", "________________________________________________")
list = [x if x != "banana" else "orange" for x in fruits]
print(list, "\n", "________________________________________________")
