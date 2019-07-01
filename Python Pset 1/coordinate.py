#Converting Astronomical Coordinate Systems
# Python Pset 1 - Exercise 2
# 6/21/19
# Jaiden Edelman

from math import pi, radians, degrees, sin, cos, asin, acos

def changeCoordsOne (RA, dec, longitude, latitude, year, month, day, UT):
    #Finding the hour angle
    jZero = 367*year - int((7.0*(year + int((month+9)/12)))/4.0)+int((275.0*month)/9.0)+ day + 1721013.5
    varJ = (jZero-2451545.0)/36525
    thetaZero = 100.46061837 + 36000.77053608*varJ + (3.87933*(10**-4)*(varJ**2))-(varJ**3)/(3.871*(10**7))
    thetaG = thetaZero + 360.985647366*(UT/24)
    theta = thetaG + longitude
    theta = theta - 360*int(theta/360.0)
    hourAngle = theta - RA
    #Converting Paramters to Radians
    hourAngleR = (hourAngle/360.0)*2*pi
    latitudeR = (latitude/360.0)*2*pi
    decR = (dec/360.0)*2*pi
    #Calculating alt and Azimuth
    altR = asin(sin(latitudeR)*sin(decR)+cos(latitudeR)*cos(decR)*cos(hourAngleR))
    azimuthR = acos((sin(decR)-sin(altR)*sin(latitudeR))/(cos(altR)*cos(latitudeR)))
    #Converting alt and Azimuth to degrees
    alt = (altR/(2*pi))*360
    print(hourAngle)
    azimuth = (azimuthR/(2*pi))*360
    if sin(-hourAngleR) < 0:
        azimuth = abs(azimuth - 360)
    return alt, azimuth
# Your function should have parameters for 
# > RA and dec in decimal degrees
# > longitude and latitude of the observer in decimal degrees
# > year, month, day, and UT in decimal hours
# note: to have a function return two values, just do: return value1, value2

print("testing RA/Dec to Alt/Az")
print(changeCoordsOne(156.65116, 24.90443, 253.08608, 34.0727, 2019, 6, 12, 5))
print(changeCoordsOne(238.40339, -19.19939, 253.08608, 34.0727, 2019, 7, 12, 5))
# test cases (Etscorn) --> expected results (approx.)
# RA: 156.65116, dec: 24.90443, longitude: 253.08608, latitude: 34.0727, year: 2019, month: 6, day: 12, UT: 5
# approximate expected result: altitude: 28.17247, azimuth: 282.38397
# RA: 238.40339, dec: -19.19939, longitude: 253.086083, latitude: 34.0727, year: 2019, month: 7, day: 12, UT: 5
# approximate expected result: altitude: 33.58536, azimuth: 202.22719

# DEFINE FUNCTION CONVERTING EQUATORIAL TO RECTANGULAR ECLIPTIC HERE
# note: to have a function return two values, just do: return value1, value2
def changeCoordsTwo (RA, dec):
    #convert parameters to radians
    RAR = (RA/360.0)*2*pi
    decR = (dec/360.0)*2*pi
    obliquity = (23.4358/360.0)*2*pi
    x = cos(RAR)*cos(decR)
    y = sin(RAR)*cos(decR)*cos(obliquity)+ sin(decR)*sin(obliquity)
    z = -sin(RAR)*cos(decR)*sin(obliquity) + sin(decR)*cos(obliquity)
    return x, y, z
print("testing equatorial to rectangular ecliptic")
# INCLUDE TEST CASES FROM HOMEWORK
print(changeCoordsTwo(213.1604166, 23.81055555556))
print(changeCoordsTwo(90.0,0.00))
