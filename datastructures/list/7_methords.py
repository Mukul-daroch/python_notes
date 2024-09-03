#_Short Lists_______________________________________________________________________________________________
print("________________________________________________")
list1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list1.sort()
print(list1, "\n________________________________________________")
list1 = [100, 50, 65, 82, 23]
list1.sort()
print(list1, "\n________________________________________________")
list1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list1.sort(reverse=True)
print(list1, "\n________________________________________________")
list1 = [100, 50, 65, 82, 23]
list1.sort(reverse=True)
print(list1, "\n________________________________________________")
def myfunc(n):
    return abs(n - 50)
list1 = [100, 50, 65, 82, 23]
list1.sort(key=myfunc)
print(list1, "\n________________________________________________")
list1 = ["banana", "Orange", "Kiwi", "cherry"]
list1.sort()
print(list1, "\n________________________________________________")
list1 = ["banana", "Orange", "Kiwi", "cherry"]
list1.sort(key=str.lower)
print(list1, "\n________________________________________________")
list1 = ["banana", "Orange", "Kiwi", "cherry"]
list1.reverse()
print(list1, "\n________________________________________________")

#_Copy Lsits _______________________________________________________________________________________________
list2 = ["apple", "banana", "cherry"]
list3 = list2.copy()
print(list3, "\n________________________________________________")
list2 = ["apple", "banana", "cherry"]
list3 = list2[:]
print(list3, "\n________________________________________________")
list2 = ["apple", "banana", "cherry"]
list3 = list(list2)
print(list3, "\n________________________________________________")

#_Join Lists_______________________________________________________________________________________________
list4, list5  = ["a", "b", "c"],[1, 2, 3]
list6 = list4 + list5
print(list6, "\n________________________________________________")
list7 = [1, 2, 3]
list8 = [1, 2, 3]
list7.extend(list8)
print(list7, "\n________________________________________________")

#_List Methods_______________________________________________________________________________________________

#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

