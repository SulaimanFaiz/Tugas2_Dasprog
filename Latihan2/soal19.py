x, y, z = map(int, input().split())

if x % y == 0 and x // y >= z:
    print("BISA")
else:
    print("MAAF")
