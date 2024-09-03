import random

# Python Numbers Types

# int
# float
# complex

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a, type(a))
print(b, type(b))
print(c, type(c))

print(random.randrange(1, 10))

print("Built-in Functions for Integers")

print(abs(-5))  # Output: 5
print(bin(10))  # Output: '0b1010'
print(hex(255))  # Output: '0xff'
print(oct(8))  # Output: '0o10'

print(int("1010", 2))  # Output: 10
print(max(1, 5, 3))  # Output: 5
print(min(1, 5, 3))  # Output: 1
print(pow(2, 3))  # Output: 8
print(pow(2, 3, 3))  # Output: 2 (2^3 % 3)
print(round(3.14159, 2))  # Output: 3.14
print(sum([1, 2, 3, 4]))  # Output: 10
print(divmod(10, 3))  # Output: (3, 1)
print(isinstance(5, int))  # Output: True


print("abs(x) ")
print("Returns the absolute value of a number. ")
print(abs(-5))  # Output: 5

print("bin(x)")
print("Converts an integer to a binary string.")
print(bin(10))  # Output: '0b1010'

print("hex(x)")
print("Converts an integer to a hexadecimal string.")
print(hex(255))  # Output: '0xff'

print("oct(x)")
print("Converts an integer to an octal string.")
print(oct(8))  # Output: '0o10'

print("int(x, base=10)")
print(
    "Converts a number or string to an integer. The base parameter specifies the base of the number (default is 10)."
)
print(int("1010", 2))  # Output: 10

print("max(iterable, *[, key, default])")
print(
    "Returns the largest item in an iterable or the largest of two or more arguments."
)
print(max(1, 5, 3))  # Output: 5

print("min(iterable, *[, key, default])")
print(
    "Returns the smallest item in an iterable or the smallest of two or more arguments."
)
print(min(1, 5, 3))  # Output: 1

print("pow(x, y[, z])")
print(
    "Returns x to the power of y; if z is present, returns x to the power of y, modulo z."
)
print(pow(2, 3))  # Output: 8
print(pow(2, 3, 3))  # Output: 2 (2^3 % 3)

print("round(number[, ndigits])")
print("Rounds a number to a specified number of decimal places.")
print(round(3.14159, 2))  # Output: 3.14

print("sum(iterable, /, start=0)")
print("Sums the items of an iterable from left to right and returns the total.")
print(sum([1, 2, 3, 4]))  # Output: 10

print("divmod(a, b)")
print("Returns a tuple containing the quotient and remainder when dividing a by b.")
print(divmod(10, 3))  # Output: (3, 1)

print("isinstance(object, classinfo)")

print("Checks if an object is an instance or subclass of a class or tuple of classes.")
print(isinstance(5, int))  # Output: True
