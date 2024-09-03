next = "----------------------"
nextx = "--X--X--X--X--X--X--X--X--X--X--X--"
b = "Hello, World!"
# ------------------------------------------
print("""string\n""")

hello = """p\n./rint(r"h34/\")"""
h = r"\'\\\bf\oooOctal value\xhh"
# h = "\'\\\bf\oooOctal value\xhh" -- will give error
# hello = r"print(r"h34/\")" -- will give error
# ------------------------------------------
print("Escape Character")
# "The escape character allows you to use double quotes when you normally would not be allowed:"

txt = 'We are the so-called "Vikings" from the north.'
print(txt)

r"""

Other escape characters used in Python:

Code	Result	Try it
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

"""
# ------------------------------------------
print(next)
# ------------------------------------------

print("print the character at position 1")
print(b, "=", b[1], "\n")

# ------------------------------------------
print(next)
# ------------------------------------------

for x in "banana":
    print(x)
print()

# ------------------------------------------
print(next)
# ------------------------------------------

txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)
# or
if "free" in txt:
    print("Yes, 'free' is present.\n")

# ------------------------------------------
print(next)
# ------------------------------------------

print(b, "=", "\n")
print()
print("len(var)", "=", len(b))
print()
print("[:5]", "=", b[:5])
print()
print("[2:]", "=", b[2:])
print()
print("[2:5]", "=", b[2:5])
print()
print("[-5:-2]", "=", b[-5:-2])
print()

# ------------------------------------------
print(next)
# ------------------------------------------
text = "hello world"

print("str.capitalize()")
print("Capitalizes the first character of the string.")
print(text.capitalize())  # Output: Hello world

print("str.casefold()")
print("Converts the string to lowercase, more aggressive than lower().")
print(text.casefold())  # Output: hello world


print("str.center(width[, fillchar])")
print(
    "Centers the string within the given width, optionally using fillchar as the padding character."
)
print(text.center(10, "*"))  # Output: **hello***

print("str.count(sub[, start[, end]])")
print("Returns the number of non-overlapping occurrences of sub in the string.")
print(text.count("o"))  # Output: 2

print("str.encode(encoding='utf-8', errors='strict')")
print("Encodes the string using the specified encoding.")
print(text.encode())  # Output: b'hello'

print("str.endswith(suffix[, start[, end]])")
print("Returns True if the string ends with the specified suffix.")
print(text.endswith("world"))  # Output: True

print("str.find(sub[, start[, end]])")
print("Returns the lowest index in the string where sub is found, or -1 if not found.")
print(text.find("world"))  # Output: 6

print("str.format(*args, **kwargs)")

print("Formats the string using placeholders.")
print(text.format("world"))  # Output: Hello, world!

print("str.isalnum()")
print("Returns True if all characters in the string are alphanumeric.")
print(text.isalnum())  # Output: True

print("str.isalpha()")
print("Returns True if all characters in the string are alphabetic.")
print(text.isalpha())  # Output: True

print("str.isdigit()")
print("Returns True if all characters in the string are digits.")
print(text.isdigit())  # Output: True

print("str.join(iterable)")
print("Joins the elements of the iterable with the string as a separator.")
separator = ", "
words = ["hello", "world"]
print(separator.join(words))  # Output: hello, world

print("str.lower()")
print("Converts all characters in the string to lowercase.")
print(text.lower())  # Output: hello world

print("str.replace(old, new[, count])")
print("Returns a copy of the string with all occurrences of old replaced by new.")
print(text.replace("world", "Python"))  # Output: hello Python

print("str.split(sep=None, maxsplit=-1)")
print("Splits the string at the specified separator and returns a list of substrings.")
print(text.split())  # Output: ['hello', 'world']

print("str.strip([chars])")
print("Removes leading and trailing characters (or whitespace by default).")
print(text.strip())  # Output: hello world

print("str.upper()")
print("Converts all characters in the string to uppercase.")
print(text.upper())  # Output: HELLO WORLD


"""
String Methods

https://www.w3schools.com/python/python_strings_methods.asp

capitalize()	Converts the first character to upper case
casefold()  	Converts string into lower case
center()    	Returns a centered string
count()  	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()      	Searches the string for a specified value and returns the position of where it was found
format()    	Formats specified values in a string
format_map()	Formats specified values in a string
index()     	Searches the string for a specified value and returns the position of where it was found
isalnum()   	Returns True if all characters in the string are alphanumeric
isalpha()   	Returns True if all characters in the string are in the alphabet
isascii()   	Returns True if all characters in the string are ascii characters
isdecimal()  	Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()   	Returns True if all characters in the string are lower case
isnumeric() 	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()   	Returns True if all characters in the string are whitespaces
istitle()   	Returns True if the string follows the rules of a title
isupper()   	Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()     	Returns a left justified version of the string
lower()     	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	    Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()  	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()  	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip() 	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title() 	Converts the first character of each word to upper case
translate()	Returns a translated string
upper() 	Converts a string into upper case
zfill() 	Fills the string with a specified number of 0 values at the beginning
"""
# ------------------------------------------
print(nextx)
print("Built-in Functions ")
print(nextx)
# ------------------------------------------
text = "hello"

print("len()")
print("Returns the length of the string.")
print(len(text))  # Output: 5

print("max()")
print("Returns the largest character in the string.")
print(max(text))  # Output: o

print("min()")
print("Returns the smallest character in the string.")
print(min(text))  # Output: e

print("sorted()")
print("Returns a sorted list of the characters in the string.")
print(sorted(text))  # Output: ['e', 'h', 'l', 'l', 'o']
# ------------------------------------------

# ------------------------------------------
price = 59
txt = f"The price is {20 * 59} {price:.3f} {price} {"hellow"} dollars"
# txt = f "The price is {price} {"hellow"} dollars" --error
print(txt)
