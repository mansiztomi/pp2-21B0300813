import os
p = str(input())
c = os.access(p, os.F_OK)
print("Existance:", c)

if c:
    print("File Name:", os.path.basename(p))
    print("Dir Name:", os.path.dirname(p))