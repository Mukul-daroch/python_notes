a, b, c = 12, 14, 21
# Short Hand If
print("A") if a > b else print("B")
# Short Hand If ... Else
print("A") if a > b else print("=") if a == b else print("B")
# And
# The and keyword is a logical operator, and is used to combine conditional statements:
if a > b and c > a:
    print("Both conditions are True")
# or
# The or keyword is a logical operator and is used to combine conditional statements:
if a > b and c > a:
    print("Both conditions are True")

# Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
if not a > b:
    print("a is NOT greater than b")
# Nested If
# if statements inside if statements, this is called nested if statements.
if a > 10:
    print("Above ten,")
    if a > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
if b > a:
    pass
