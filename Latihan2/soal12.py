a, b = map(int, input().split())
c, d = map(int, input().split())

a += c
b += d

a, b = b, a

print(a, b)
