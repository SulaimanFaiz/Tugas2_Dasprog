import sys
t = int(input())  

for i in range(t):
    n = int(input())
    hasil = []
    for i in range(n):
        l = list(map(int, input().split()))
        hasil.append(l)
        if len(hasil[i]) != i+1:
            print("Formatnya salah nigga")
            sys.exit()
            
    for j in range(n-2, -1, -1):  
        for k in range(len(hasil[j])):
            hasil[j][k] += max(hasil[j+1][k], hasil[j+1][k+1])

    print(hasil[0][0])
