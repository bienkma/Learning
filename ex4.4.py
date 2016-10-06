"""
Exercise 4.4 Can you think of a way to swap the values of two variables that does not
need a third variable as a temporary storage? In the code block below, try to implement
the swapping of the values of a and b without using a third variable. To help you out, the
first step to do this is already given. You just need to add two more lines of code.
a = 17
b = 23
print( "a =", a, "and b =", b )
a += b
# add two more lines of code here to cause swapping of a and b
print( "a =", a, "and b =", b )
"""
a = 17
b = 23
print("a =", a, "and b=", b)
a += b
b = a - b
a -= b
print("Swap a =", a, "and b =", b)
