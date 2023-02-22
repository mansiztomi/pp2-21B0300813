#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    while a <= b:
        yield a*a
        a += 1

a, b = 3, 6
for x in squares( a, b):
    print(x, end=' ')

