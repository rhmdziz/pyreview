t = int(input('input tinggi: '))

for i in range(t):
    print('_'*i, end='')

    for j in range(t-i, 0, -1):
        print(j, end='')

    print()
