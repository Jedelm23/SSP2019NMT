 # PURPOSE OF THIS CODE
# Python Pset 1
# Due 6/21/19
# Jaiden Edelman

def sumList(nums):
    total = 0
    for number in range(len(nums)):
        total = total + nums[number]
    return total

print("testing sumList")
print(sumList([]))              # expected output: 0
print(sumList([3]))             # expected output: 3
print(sumList([1., 4.5, -3.2])) # expected output: 2.3

def estimatePi(n):
    total = 0
    for index in range(n):
        total = total + ((4.0/(2*index + 1))*(-1)**index)
    return total

print("testing estimatePi")
print(estimatePi(1))     # expected (approximate) output: 4.0
print(estimatePi(10))    # expected (approximate) output: 3.0418396189294032
print(estimatePi(100))   # expected (approximate) output: 3.1315929035585537
print(estimatePi(1000))  # expected (approximate) output: 3.140592653839794
print(estimatePi(10000)) # expected (approximate) output: 3.1414926535900345

def scaleVec(vec, scalar):
    product = []
    for number in range(len(vec)):
        product.append(vec[number]*scalar)
    return product

print("testing scaleVec")
vec = []
print(scaleVec(vec, 5)) # expected output: []
print(vec) # expected output: []
vec = [1]
print(scaleVec(vec, 5)) # expected output: [5]
print(vec) # expected output: [1]
vec = [-2, 1.5, 0.]
print(scaleVec(vec, 6)) # expected output: [-12., 9., 0.]
print(vec) # expected output: [-2, 1.5, 0.]
