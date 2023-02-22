# #Create a generator that generates the squares of numbers up to some number N.
N = 10
gen = (x*x for x in range( N ))
for i in gen:
    print( i )

 