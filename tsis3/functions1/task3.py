def solve(numheads, numlegs):
    return ((numlegs-2*numheads)//2), (numheads-((numlegs-2*numheads)//2))
a = int(input())
b= int(input())
r, c = solve(a, b)
print('rabbits -', r)
print('chickens -', c)
