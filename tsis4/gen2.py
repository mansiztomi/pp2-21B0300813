# #Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def gen1( n ):
    x = 2
    while x < n:
        yield x
        x += 2

n = input()
for i in gen1( int(n) ):
    print( i, end=', ')

