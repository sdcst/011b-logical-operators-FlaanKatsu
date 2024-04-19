#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue". Else, it is "tralse"
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""

import math
sakura = 1
ben = 0
ん = float(input("please enter an obese number: "))
ん6 = ん / 6
ん6a = math.floor(ん6)
ん6b = math.ceil(ん6)
if ん6a == ん6b:
    ben = 1
ん8 = ん / 8
ん8a = math.floor(ん8) 
ん8b = math.ceil(ん8)
if ん8a == ん8b:
    sakura = 0
if ben and sakura == 1:
    print(f"{ん} is frue.")
else:
    print(f"{ん} is tralse.")