"""
A simple die roller

Author: Kyle Gortych
Date: 2/23/2021
"""

import random

first = 1
last = 6

roll = random.randint(first,last)
print("Choosing a number between %s and %d." %(first,last))
print ("The number is %d." % roll)