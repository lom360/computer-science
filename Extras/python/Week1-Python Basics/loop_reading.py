# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 23:48:55 2017

@author: Lom
NOTE: THE PROBLEMS THAT ARE COMMENTED OUT
      are infinite loops.
"""

"""Problem 1"""
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 
"""Answer 1: 0 1 2 3 4 5 'Outside of loop' 6"""

"""Problem 2"""
"""numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))"""
"""Answer 2: This will be an infinite loop."""

"""Problem 3"""
num = 10
while num > 3:
    num -= 1
    print(num)
"""Answer 4: 9 8 7 6 5 4 3"""

"""Problem 4"""
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')
"""Answer 4: 10 9 8 7 'Breaking out of loop' 'Outsde of Loop' """

"""Problem 5"""
"""num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num))"""
"""Answer 5: This will be an infinite loop."""