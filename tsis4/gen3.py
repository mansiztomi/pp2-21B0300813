

#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def gen2():
    x = 1
    while True:
        if x % 3 == 0 and x % 4 == 0:
            yield x
        x += 1

def function( n ):
    gen = gen2()
    for i in gen:
        print( i )
        if i >= n:
            gen.close()

function( 40 )

