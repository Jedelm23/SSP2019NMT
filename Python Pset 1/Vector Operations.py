import math

def mag (vector):
    total = 0
    for index in range(len(vector)):
        total += vector[index]**2
    magnitude = math.sqrt(total)
    return magnitude

print(mag([]))
print(mag([3]))
print(mag([1,-1]))
print(mag([1,1,1,1]))

def dot (vector1,vector2):
    product = 0
    for component in range(len(vector1)):
        product += vector1[component]*vector2[component]
    return product

print(dot([],[]))
print(dot([2,5,6],[3,7,8]))
print(dot([1,-1,0],[-1,-1,5]))
print(dot([1,0,1,0],[2,2,0,2]))

def cross (vector1, vector2):
    product = []
    product.append(vector1[1]*vector2[2]-vector1[2]*vector2[1])
    product.append(vector1[2]*vector2[0]-vector1[0]*vector2[2])
    product.append(vector1[0]*vector2[1]-vector1[1]*vector2[0])
    return product

print(cross([1,0,0],[0,1,0]))
print(cross([1,0,0],[0,0,1]))
print(cross([2,5,6],[3,7,8]))

        
