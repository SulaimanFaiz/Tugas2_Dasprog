n=int(input())
pola="##"
hasil=""
for i in range (n):
    hasil = hasil + pola[i % len(pola)]

print(hasil)