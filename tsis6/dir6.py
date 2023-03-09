import os
while True:
    command = input()
    if command == 'create':
        for i in range(65, 65+26):
            filename = chr(i)+'.txt'
            with open(chr(i) + ".txt", "w") as file:
                file.writelines(chr(i))
    elif command == 'delete':
        for i in range(65, 65+26):
            os.remove(chr(i) + ".txt")
    elif command == 'exit':
        break