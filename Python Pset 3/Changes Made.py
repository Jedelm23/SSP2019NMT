"Errors"
#There were a few errors in the first while loop. The equation giving Egeuss was incorrect
 Eguess = Eguess - (Eguess - e*sin(Eguess) - Mtrue) / (1 - e*cos(Eguess))
#Was changed to
 Eguess = Eguess - (Mtrue - (Eguess - e*sin(Eguess))) / (e*cos(Eguess)-1)
#And the the "<" sign was changed to ">", so that the while loop wouldn't only run if Mguess and Mtrue were very close

#In the second while loop, I changes it to "while(True)" and I indented the last two lines that updated the asteroid's position and trail.
#This made it so that the position continuously updated and the simulation would be animated

"Structural Changes"
#I reworked the mathematics and coordinate transformations using numpy.
#I ran through the matrix calculations once to get the starting position and then added those same calculations to the while loop so that they updated continuosly.
#This made it much easier to understand what the code was doing and easier to edit the matrices in the future.
#I also didn't have to work the matrices out by hand in order to check whether or not they were typed correctly in OrbitViz.py

#To do these calculations, I first got the cartesian coordinates, rotated to ecliptic coordinates, and finally converted to equatorial coordinates.
#Then, I created a vector where x = [0,0], y = [1,1], and z = [2,2], since those indexes contained the values calculated in the matrix multiplication

#In order to make the visualization more visually appealing/accurate, I increased the distance between the asteroid and the sun by a factor of 15

"Verification"
#In order to check whether my code was working properly, I adjusted the eccentricity to .75 and decreased the speed of the asteroid
# This made it easy to see that the asteroid was slower when it was further from the sun, which is what is predicted by Kepler's second law
