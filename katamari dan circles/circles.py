import math

x1, y1, r1 = map(float, input().split())
x2, y2, r2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1
d = math.hypot(dx, dy)

if d > r1 + r2 or d < abs(r1 - r2):
    print("Amang ges")

elif abs(d - (r1 + r2)) < 1e-9 or abs(d - abs(r1 - r2)) < 1e-9:
    print("Fyuh, hampir saja")
    a = (r1**2 - r2**2 + d**2) / (2*d)
    x3 = x1 + a * dx / d
    y3 = y1 + a * dy / d
    print(f"{x3:.2f} {y3:.2f}")


else:
    print("Tidaaaaaak, airnya muncrat!")
    a = (r1**2 - r2**2 + d**2) / (2*d)
    h = math.sqrt(r1**2 - a**2)
    x3 = x1 + a * dx / d
    y3 = y1 + a * dy / d

    xa = x3 + h * dy / d
    ya = y3 - h * dx / d
    xb = x3 - h * dy / d
    yb = y3 + h * dx / d

    total = xa + ya + xb + yb
    print(f"{total:.2f}")
