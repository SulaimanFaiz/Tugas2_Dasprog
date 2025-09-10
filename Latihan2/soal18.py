x, y, z = map(int, input().split())

if (x + z) % y == 0:
    print("BISA")
else:
    print("MAAF")
