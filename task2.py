#! python3
##Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and divisible by 2.

Note:  Many languages have a problem when dealing with floating point
decimals, and python is no exception.
Sometimes, when finding the cube root of large numbers, like 729,
you may get 8.9999999999999999999998 instead of 9

----------------------------------------------------------------

i found that, according to python, 0.1 + 0.2 = 0.30000000000000004
where does the 4 come from?

----------------------------------------------------------------

To get around this, we can use the round() command
round() accepts 2 parameters, the number to be rounded, and how many decimals
a = round(3.999999999999998, 8) would round at the 8th decimal place, for example.
You don't want to round too early (ie to the nearest whole number) because that
might be too inaccurate.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a divisible by 2.
xx is only a perfect square.0.3000000000000040.300000000000004
xx is only divisible by 2.

Example:
Enter a number: 8
8 is only divisible by 2.

Enter a number: 64
64 is both a perfect square and divisible by 2.
"""
import math

input("lord beelzubub will calculate if a number is both a perfect square and divisable by 2.")
n = float(input("please now input a number: "))
y = n **0.5
x = n / 2
yf = math.floor(y)
yc = math.ceil(y)
xc = math.floor(x)
xf = math.ceil(x)

if ( yf == yc ) and ( xf == xc ):
    print("This number is both devisible by 2 and a perfect square.")
else:
    print("This number is either not divisable by 2 or not a perfect square.")
