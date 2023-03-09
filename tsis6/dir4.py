f = open('data4.txt', 'r')
ans = 0
r = f.read()
spl = r.split("\n")

for i in spl:
    if i:
        ans += 1
print("Number of lines:", ans)