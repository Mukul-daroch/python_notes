print("_____________________________________________")
listx = [1,2,[3,4,[2,4]]]
print(listx)
print(listx[2])
print(listx[2][2])
print(listx[2][2][1])
# python lists Access list items
list1 = ["abc", 34, True, 40, "male"]
print("_____________________________________________")
print(f"{'list1'}         {list1} ")
print("---------------------------------------------")
print(f"{'len(list1)'}    {len(list1)}")
print(f"{'type(list1)'}   {type(list1)}")
# Access Items or Indexing/Negative Indexing
print(f"{'list1[1]'}      {list1[1]}")
print(f"{'list1[-1]'}     {list1[-1]} \n")

list2 = ["0", "1", "2", "3", "4"]
print("_____________________________________________")
print(f"{'list2'}             {list2}")
print("---------------------------------------------")
# Range of Indexes
print(f"{'>>list2[:4]'}       {list2[:4]}")
print(f"{'>>list2[2:]'}       {list2[2:]}")
print(f"{'>>list2[-4:-1]'}    {list2[-4:-1]} \n")

list3 = list(("apple", "banana", "cherry"))
print("_____________________________________________")
print(f"{'list3'}         {list3}")
print("---------------------------------------------")
# Check if Item Exists
x, y = "app", "apple"

if x in list3:
    print("Yes, ", x, " is in the fruits list")
else:
    print("no,  ", x, "  is not in the fruits list")
if y in list3:
    print("Yes, ", y, " is in the fruits list")
else:
    print("no,  ", y, "  is not in the fruits list \n")

# note  list(("a", "b", "c")) this type of list can nor be edited
