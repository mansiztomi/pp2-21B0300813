s = list(map(str, input().split()))
f = open('data5.txt', 'w')

for i in s:
    f.write(i + "\n")
f.close()