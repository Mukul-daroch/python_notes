# Loop Through a Tuple
print("_____________________________________________")
tuple1 = ("apple", "banana", "cherry")
for x in tuple1:
    print(x)
print("_____________________________________________")
tuple1 = ("apple", "banana", "cherry")
for i in range(len(tuple1)):
    print(tuple1[i])
print("_____________________________________________")
tuple1 = ("apple", "banana", "cherry")
i = 0
while i < len(tuple1):
    print(tuple1[i])
    i = i + 1
print("_____________________________________________")

# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
print("_____________________________________________")
tuple1 = ("a", "b" , "c")
mytuple = tuple1* 2
print(mytuple)
print("_____________________________________________")

#Tuple Methods

#Method	Description
#count()	Returns the number of times a specified value occurs in a tuple
tuple4 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = tuple4.count(5)
print(x)
#index()	Searches the tuple for a specified value and returns the position of where it was found
tuple4 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = tuple4.index(8)
print(x)
