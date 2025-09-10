a, b, c, d = map(int, input().split())

# 1. Abdan Ke Arya
c += a
a = 0

# 2. Albert Ke Abdan
a += d
d = 0

# 3. Kevin Ke Abdan
a += b
b = 0

# 4. Abdan Ke Albert
d += a
a = 0

# 5. Albert Ke Arya
c += d
d = 0

print(a, b, c, d)
