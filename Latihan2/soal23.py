kotak = list(map(int, input().split()))
x, y = map(int, input().split())

hasil = kotak[x-1] + kotak[y-1]

print(hasil)
