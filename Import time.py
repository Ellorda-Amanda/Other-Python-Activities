# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:44:09 2024

@author: Amanda Ellorda
"""

hour = int(input("Enter hour between 1 and 12: "))
maridiem = int(input("am (1) or pm (2)?: "))
hours = int(input("How many hours ahead?: "))

if maridiem == 2 and hour != 12:
    hour += 12
elif maridiem == 1 and hour == 12:
    hour = 0

new_hour = (hour + hours) % 24

if new_hour == 0:
    new_hour = 12
    maridiem = 2
elif new_hour > 12:
    new_hour -= 12
    maridiem = 2
else:
    maridiem = 1

if maridiem == 1:
    print("New hour: ",new_hour, "am")
else:
    print("New hour: ",new_hour, "pm")
