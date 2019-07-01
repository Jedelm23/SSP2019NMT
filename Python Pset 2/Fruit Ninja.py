
# starter code for exercise 0 on programming homework 2

import numpy as np

fruits = np.array([["Apple","Banana","Blueberry","Cherry"],
["Coconut","
 ,"Orange","Tangerine","Pomegranate"],
["Lemon","Raspberry","Strawberry","Tomato"]])

print(fruits[3,3])

print(fruits[1:3,1:3])

print(fruits[0::2])

print(fruits[2:0:-1,2:0:-1])

fruits2 = np.copy(fruits)
fruits[::,0] = fruits2[::,3]
fruits[::,3] = fruits2[::,0]
print(fruits)

w = [["Sliced" for x in fruits[:]] for line in fruits]
print(w)

    
