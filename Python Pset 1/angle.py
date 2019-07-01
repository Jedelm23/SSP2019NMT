# Converting to Decimal Degrees
# Python Pset 1 - 1a
# 6/21/19
# Jaiden Edelman

import math

def convertAngle(degrees, minutes, seconds, radians, normalize):
    float(degrees)
    # handle a negative angle
    sign = math.copysign(1, degrees)
    if sign < 0:
        minutes = minutes * -1
        seconds = seconds * -1
    # perform angle conversion
    decimal_min = (minutes/60.0)
    decimal_sec = (seconds/3600.0)
    end_deg = degrees + decimal_min + decimal_sec
    if normalize == True and abs(end_deg) > 360:
        end_deg = end_deg - 360*int(end_deg / 360)
    if normalize == True and sign < 0:
        end_deg = end_deg + 360
    if radians == True:
        end_deg = (end_deg/360.0)*2*math.pi
    # return result
    return end_deg



# test cases for part a
#print(convertAngle(90, 6, 36)) # should print 90.11
#print(convertAngle(-90, 6, 36)) # should print -90.11
#print(convertAngle(-0.0, 30, 45)) # should print -0.5125

# test cases for part b (uncomment these, comment out previous tests)
#print(convertAngle(90, 6, 36, True)) # should print 1.57271618897
#print(convertAngle(-90, 6, 36, True)) # should print -1.57271618897
#print(convertAngle(90, 6, 36, False)) # should print 90.11
#print(convertAngle(-90, 6, 36, False)) # should print -90.11

# these are the test cases you will demonstrate when getting this homework checked off
# test cases for part c (uncomment these, comment out previous tests)
print(convertAngle(90, 6, 36, False, False)) # should print 90.11
print(convertAngle(90, 6, 36, True, False)) # should print 1.57271618897
print(convertAngle(90, 6, 36, False, True)) # should print 90.11
print(convertAngle(90, 6, 36, True, True)) # should print 1.57271618897
print(convertAngle(-90, 6, 36, False, False)) # should print -90.11
print(convertAngle(-90, 6, 36, True, False)) # should print -1.57271618897
print(convertAngle(-90, 6, 36, False, True)) # should print 269.89
print(convertAngle(-90, 6, 36, True, True)) # should print 4.71046911821
print(convertAngle(540, 0, 0, False, True)) # should print 180.0
print(convertAngle(-0.0, 30, 45, False, False)) # should print -0.5125
