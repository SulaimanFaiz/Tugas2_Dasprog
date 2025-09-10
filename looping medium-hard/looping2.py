n = int(input())
hasil = 0

for i in range(n):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        hasil += 1

print(hasil)
