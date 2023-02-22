import math

#Write a Python program to convert degree to radian.
print( math.radians( 15 ))

#Write a Python program to calculate the area of a trapezoid.
def areaOfTrap( h, v1, v2):
    return h*((v1+v2)*0.5)

print( areaOfTrap( 5, 5, 6))

#Write a Python program to calculate the area of regular polygon.
def areaOfRegPol( v1, v2):
    apothem = v2 / 2*math.tan(math.pi/v1)
    return v1 * v2 * 0.5 * apothem

print( areaOfRegPol( 4, 25 ))

#Write a Python program to calculate the area of a parallelogram.
def areaOfParall( a, b):
    return a*b

print( areaOfParall( 5, 6))