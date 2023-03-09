import os

while True:
    command = input()

    if command == 'cd':
        kuda = input()
        if os.path.isdir(kuda) and os.path.exists(kuda):
            os.chdir(kuda)
        else:
            print('Not a directory')

    elif command == 'gdeya':
        print(f'The current directory is: {os.getcwd()}')

    elif command == 'del':
        chto = input()
        if os.path.exists(chto):
            os.remove(chto)
            print('Done')
        else:
            print('There is no such file')
    elif command == 'exit':
        break