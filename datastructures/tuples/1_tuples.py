print("________________________________________________")
tuple1 = ('a','b','c','d','e')
tuple2 = tuple((1, 5, 7, 9, 3))
print(tuple1)
print(tuple2)
print("________________________________________________")
print(type(tuple1))
print("________________________________________________")
print(len(tuple1))
print("________________________________________________")
print("________________________________________________")
tuple3 = (1,2,(3,4,(2,4)))
print(tuple3)
print(tuple3[2])
print(tuple3[2][2])
print(tuple3[2][2][1])
# python lists Access list items
tuple4 = ("abc", 34, True, 40, "male")
print("_____________________________________________")
print(f"{'tuple4'}         {tuple4} ")
print("---------------------------------------------")
print(f"{'len(tuple4)'}    {len(tuple4)}")
print(f"{'type(tuple4)'}   {type(tuple4)}")
# Access Items or Indexing/Negative Indexing
print(f"{'tuple4[1]'}      {tuple4[1]}")
print(f"{'tuple4[-1]'}     {tuple4[-1]} \n")

tuple5 = ("0", "1", "2", "3", "4")
print("_____________________________________________")
print(f"{'tuple5'}             {tuple5}")
print("---------------------------------------------")
# Range of Indexes
print(f"{'>>tuple5[:4]'}       {tuple5[:4]}")
print(f"{'>>tuple5[2:]'}       {tuple5[2:]}")
print(f"{'>>tuple5[-4:-1]'}    {tuple5[-4:-1]} \n")
print("_____________________________________________")

# Unpacking a Tuple
tuple6 = ( "0","1", "2")
(a , b, c) = tuple6
print(a)
print(b)
print(c)
print("_____________________________________________")
# Using Asterisk*
tuple6 = ( "0","1", "2","3", "4")
(a , b, *c) = tuple6
print(a)
print(b)
print(c)
print("_____________________________________________")
tuple6 = ( "0","1", "2","3", "4")
(a , *b, c) = tuple6
print(a)
print(b)
print(c)
print("_____________________________________________")
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
print("_____________________________________________")
