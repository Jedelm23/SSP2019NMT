from vpython import *
import numpy as np
import math as m

a = 2.773017979589484
#e = 0.1750074901308245
e = .75
T = radians(336.0050001501443)
Oprime = radians(108.032597191534)
iprime = radians(16.34548466739393)
wprime = radians(74.95130563682554)

def solvekep(M):
    Eguess = M
    Mguess = Eguess - e*sin(Eguess)
    Mtrue = M
    while abs(Mguess - Mtrue) > 1e-004: #Changed so that the while loop would actually run
        Mguess = Eguess - e*sin(Eguess)
        Eguess = Eguess - (Mtrue - (Eguess - e*sin(Eguess))) / (e*cos(Eguess)-1)#Equation was incorrect
    return Eguess

k = 0.01720209895 #Changed variable name to k
mu = sqrt(k**2)
time = 0
dt = 1
period = sqrt(4*pi**2*a**3/mu)
r1ecliptic = vector(0, 0, 0)
#Added ecliptic value
obliquity = radians(23.4358)
Mtrue = 2*pi/period*(time) + T
Etrue = solvekep(Mtrue)


#Broke up this math, first finding x,y, and z in cartesian coordinates
position = []

xCartesian = a*cos(Etrue)-a*e
yCartesian = a*(sqrt(1-e**2))*sin(Etrue)
zCartesian = 0

position.append(xCartesian)
position.append(yCartesian)
position.append(zCartesian)
xyz = np.array(position)

#Created Arrays to make the math easier
array1 = np.array([[m.cos(Oprime),-m.sin(Oprime), 0],
                  [m.sin(Oprime),m.cos(Oprime),0],
                  [0,0,1]])

array2 = np.array([[1,0,0],
                  [0,m.cos(iprime),-m.sin(iprime)],
                  [0,m.sin(iprime),m.cos(iprime)]])

array3 = np.array([[m.cos(wprime),-m.sin(wprime),0],
                  [m.sin(wprime),m.cos(wprime),0],
                  [0,0,1]])

eclipticPos = np.multiply(np.multiply(np.multiply(array1, array2), array3), xyz)

#Converted to equatorial
array4 = np.array([[1,0,0],
                   [0,cos(obliquity),-sin(obliquity)],
                   [0, sin(obliquity),cos(obliquity)]])

equatorialPos = np.multiply(array4,eclipticPos)
print(equatorialPos)
r1ecliptic = vector(equatorialPos[0,0],equatorialPos[1,1],equatorialPos[2,2])


#r1ecliptic.x = (cos(wprime)*cos(Oprime) - sin(wprime)*cos(iprime)*sin(Oprime))*(a*cos(Etrue)-a*e) - (cos(wprime)*cos(iprime)*sin(Oprime) + sin(wprime)*cos(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
#r1ecliptic.y = (cos(wprime)*sin(Oprime) + sin(wprime)*cos(iprime)*cos(Oprime))*(a*cos(Etrue)-a*e) + (cos(wprime)*cos(iprime)*cos(Oprime) - sin(wprime)*sin(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
#r1ecliptic.z = sin(wprime)*sin(iprime)*(a*cos(Etrue)-a*e) + cos(wprime)*sin(iprime)*(a*sqrt(1-e**2)*sin(Etrue))

#asteroid = sphere(pos=r1ecliptic*150, radius=(15), color=color.white)
#asteroid.trail = curve(color=color.white)
#sun = sphere(pos=vector(0,0,0), radius=(50), color=color.yellow)

asteroid = sphere(pos=r1ecliptic*150, radius=(15), color=color.white) #Changed variables
asteroid.trail = curve(color=color.white)
sun = sphere(pos=vector(0,0,0), radius=(50), color=color.yellow)

while (True): #One does not always equal one
    rate(20)
    time = time + dt
    Mtrue = 2*pi/period*(time) + T
    Etrue = solvekep(Mtrue)

    position = []
    xCartesian = a*cos(Etrue)-a*e
    yCartesian = a*(sqrt(1-e**2))*sin(Etrue)
    zCartesian = 0

    position.append(xCartesian)
    position.append(yCartesian)
    position.append(zCartesian)
    xyz = np.array(position)
    
    eclipticPos = np.multiply(np.multiply(np.multiply(array1, array2), array3), xyz)
    equatorialPos = np.multiply(array4,eclipticPos)
    r1ecliptic = vector(equatorialPos[0,0],equatorialPos[1,1],equatorialPos[2,2])
    #r1ecliptic.x = (cos(wprime)*cos(Oprime) - sin(wprime)*cos(iprime)*sin(Oprime))*(a*cos(Etrue)-a*e) - (cos(wprime)*cos(iprime)*sin(Oprime) + sin(wprime)*cos(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
    #r1ecliptic.y = ((cos(wprime)*sin(Oprime) + sin(wprime)*cos(iprime)*cos(Oprime))*(a*cos(Etrue)-a*e)) + (cos(wprime)*cos(iprime)*cos(Oprime) - sin(wprime)*sin(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
    #r1ecliptic.z = sin(wprime)*sin(iprime)*(a*cos(Etrue)-a*e) + cos(wprime)*sin(iprime)*(a*sqrt(1-e**2)*sin(Etrue))\
    r1ecliptic *= 15
    asteroid.pos = r1ecliptic*150 #Indented two lines that weren't updating continuously
    asteroid.trail.append(pos=asteroid.pos)  
