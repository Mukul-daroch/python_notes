print("____________________________________________________0")


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(10))
print("____________________________________________________0")


def my_function(x, kids):
    print("The youngest child is " + kids[x])


my_function(0, ["Emil", "Tobias", "Linus"])
print("____________________________________________________0")

def tri_recursion(k):
    if k > 0:
        print(k)
        result = tri_recursion(k - 1) + k
        print("-----------")
        print(k)
        print(result)
    else:
        result = 0
    return result
tri_recursion(6)
print("____________________________________________________0")

def recursion(k):
    if k > 0:
        return k + recursion(k - 1)
    else:
        return 0
print(recursion(10))
