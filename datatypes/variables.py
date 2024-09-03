a = "string"
print(type(a))

b = 1
print(type(b))

c = 1.1
print(type(c))


x = "awesome" #Global Variable


print("Python is " + x)


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

