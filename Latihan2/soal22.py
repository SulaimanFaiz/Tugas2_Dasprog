rank=int(input())

if rank < 899:
    print("Bronze")
elif 899 <= rank <= 1097:
    print("Warior")
elif 1098 <= rank <= 3500:
    print("Mythic")
elif 3501 <= rank <= 4737:
    print("Legend")
else:
    print("Epic")