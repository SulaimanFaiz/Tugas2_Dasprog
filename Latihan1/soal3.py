n = int(input())
m = int(input())

for i in range(n):
    baris = ""
    for k in range(m):
        baris += "*" if (i + k) % 2 == 0 else "#"
    print(baris)