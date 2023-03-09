import os
pa = str(input())
p = os.listdir(pa)
print("Only Directories:")
for i in p:
  if os.path.isdir(i):
    print(i)

print("Only Files:")
for i in p:
    if not os.path.isdir(i):
        print(i)

print("All directories and Files")
for i in p:
    print(i)