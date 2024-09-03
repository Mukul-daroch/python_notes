# Python Arithmetic Operators
x, y = 4, 5
print("_____________________________")
print("# Python Arithmetic Operators")
print("-----------------------------")

print(f"+  Addition:       {x + y} \n")
print(f"-  Subtraction:    {x - y} \n")
print(f"*  Multiplication :{x * y} \n")
print(f"/  Division:       {x / y} \n")
print(f"%  Modulus:        {x % y} \n")
print(f"** Exponentiation: {x ** y} \n")
print(f"// Floor division: {x // y} \n")


print("_____________________________")
print("# Python Assignment Operators")
print("-----------------------------")


print("=	x = 5   	x = 5 \n")
print("+=	x += 3  	x = x + 3 \n")
print("-=	x -= 3  	x = x - 3 \n")
print("*=	x *= 3  	x = x * 3 \n")
print("/=	x /= 3  	x = x / 3 \n")
print("%=	x %= 3  	x = x % 3 \n")
print("//=	x //= 3 	x = x // 3 \n")
print("**=	x **= 3 	x = x ** 3 \n")
print("&=	x &= 3  	x = x & 3 \n")
print("|=	x |= 3  	x = x | 3 \n")
print("^=	x ^= 3  	x = x ^ 3 \n")
print(">>=	x >>= 3 	x = x >> 3 \n")
print("<<=	x <<= 3 	x = x << 3 \n")
print()
print(":=	print(x := 3)	x = 3 \n")

print("_____________________________")
print("# Python Comparison Operators")
print("-----------------------------")



print(f"==	Equal	                  x == y {x == y} \n")
print(f"!=	Not equal                 x != y {x != y} \n")
print(f">	Greater than           	  x > y  {x > y} \n")
print(f"<	Less than                 x < y  {x < y} \n")
print(f">=	Greater than or equal to  x >= y {x >= y} \n")
print(f"<=	Less than or equal to	  x <= y {x <= y} \n")

print("_____________________________")
print("# Python Membership Operators ")
print("-----------------------------")
#Membership operators are used to test if a sequence is presented in an object:
print("in       Returns True if a sequence with the specified value is present in the object	    x in y ")
print("not in   Returns True if a sequence with the specified value is not present in the object	x not in y ")

print("_____________________________")
print("# Python Bitwise Operators ")
print("-----------------------------")

#Bitwise operators are used to compare (binary) numbers:

print(f"& 	AND	Sets each bit to 1 if both bits are 1	x & y \n")
print(f"|	OR	Sets each bit to 1 if one of two bits is 1	x | y \n")
print(f"^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y \n")
print(f"~	NOT	Inverts all the bits	~x \n")
print(f"<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off x << 2 \n")
print(f">>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> \n")

print("_____________________________")
print("# The precedence order       ")
print("-----------------------------")

print("()       	                                    Parentheses ")
print("**                                               Exponentiation ")
print("+x  -x  ~x                                       Unary plus, unary minus, and bitwise NOT ")
print("*  /  //  %                                      Multiplication, division, floor division, and modulus ")
print("+  -                                             Addition and subtraction ")
print("<<  >>                                           Bitwise left and right shifts ")
print("&                                                Bitwise AND ")
print("^                                                Bitwise XOR ")
print("|                                                Bitwise OR ")
print("==  !=  >  >=  <  <=  is  is not  in  not in     Comparisons, identity, and membership operators ")
print("not                                              Logical NOT ")
print("and                                              AND ")
print("or                                               OR ")



