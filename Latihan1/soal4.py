n = int(input())
s = ""
for i in range(n):
    if n % 2 == 1:
        s += "#" if i % 2 == 0 else "*"
    else:
        s += "*" if i % 2 == 0 else "#"
print(s)
