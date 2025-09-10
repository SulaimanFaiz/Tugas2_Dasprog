n, m = map(int, input().split())

for i in range(n):
    pola = []
    for j in range(m):
        if (i + j) % 2 == 0:
            pola.append('*')
        else:
            pola.append('#')
    print(''.join(pola))
