# Trigonometry
# Python Pset 3
# Jaiden Edelman
# 6/29/19
import math as m
# a function to determine the quadrant of an angle based on its sine and cosine (in radians)
# returns the angle in the correct quadrant (in radians)
def findQuadrant(sine, cosine):
    if cosine > 0 and sine > 0: #1
        return m.asin(sine)

    if cosine < 0 and sine > 0: #2
        return m.acos(cosine)

    if cosine < 0 and sine < 0: #3
        return pi - m.asin(sine)

    if cosine > 0 and sine < 0: #4
        return 2*pi + m.asin(sine)

def radian(angle):
    return (angle/180) * m.pi
def degree(angle):
    return (angle/m.pi)*180

# a function that given the values (in radians) of two sides and the included angle of a spheical triangle
# returns the values of the remaining side and two angles (in radians)
def SAS(aDeg, BDeg, cDeg):
    a = radian(aDeg)
    B = radian(BDeg)
    c = radian(cDeg)
    
    b = m.acos(m.cos(a)*m.cos(c)+m.sin(a)*m.sin(c)*m.cos(B))
    A = m.asin((m.sin(B)*m.sin(a))/m.sin(b))
    C = m.asin((m.sin(B)*m.sin(c))/m.sin(b))
    
    A = findQuadrant(m.sin(A),m.cos(A))
    C = findQuadrant(m.sin(C),m.cos(C))
    
    bDeg = degree(b)
    ADeg = degree(A)
    CDeg = degree(C)
    
    return bDeg, ADeg, CDeg

# YOUR CODE HERE (part b)
print(SAS(106, 114, 42))

