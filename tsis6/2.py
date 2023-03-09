s = str(input().split())
u = 0
l = 0
for i in s:
    if 65 <= ord(i) <= 90: u += 1
    if 97 <= ord(i) <= 122: l += 1

print("Lower: " + str(l))
print("Upper: " + str(u))