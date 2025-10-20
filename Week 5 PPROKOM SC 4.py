# Program mencetak pola segitiga bintang
tinggi = 5
for i in range(1, tinggi + 1):
    for j in range(i):
        print("*", end=" ")
    print()
