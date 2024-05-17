# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:44:09 2024

@author: Amanda Ellorda
"""


import math
a = None
b = None
c = None

while a != 0 and b != 0 and c != 0:
    a = float(input("Enter the length of side A: "))
    if a == 0:
        break
    b = float(input("Enter the length of side B: "))
    if b == 0:
        break
    c = float(input("Enter the length of side C: "))
    if c == 0:
        break

    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        A= math.sqrt(s * (s - a) * (s - b) * (s - c))
        A = round(A, 2)
        print("The area of the triangle is ", A)
    else:
        print("Error: the input values do not form a valid triangle.")