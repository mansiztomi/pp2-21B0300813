#Implement a generator that returns all numbers from (n) down to 0.
def generator( n ):
    x = n
    while x >= 0:
        yield x
        x -= 1

n = 12
for i in generator( n ):
    print( i )