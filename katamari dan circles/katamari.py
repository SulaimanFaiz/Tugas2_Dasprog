import math

n = int(input())
k = int(math.log(n+1,2))

a = (2**(k+1))-1
b = 2**k-1

selisihbawah = n - b
selisihatas  = a - n

if n == b or n == b:
    print("It's the perfect amount, nice!")
elif selisihbawah <= selisihatas:
    print(f"Maybe it's better to remove {selisihbawah} fences, just to be perfect")
else:
    print(f"Maybe it's better to add {selisihatas} fences, just to be perfect")
