n = int(input())

for i in range(n, 0, -1):        # jumlah digit per baris
    for j in range(i, 0, -1):    # cetak dari i turun ke 1
        print(j, end="")
    print()                      # pindah baris
