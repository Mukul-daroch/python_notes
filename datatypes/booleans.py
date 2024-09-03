#Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
   
#The following will return True:
print(bool(1))
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.

#The following will return False:
print(bool())
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
