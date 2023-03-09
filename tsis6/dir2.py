import os
p = str(input())

c1 = os.access(p, os.F_OK)
print("Exist:", c1)

c2 = os.access(p, os.R_OK)
print("Readable", c2)

c3 = os.access(p, os.W_OK)
print("Writable:", c3)

c4 = os.access(p, os.X_OK)
print("Executable:", c4)