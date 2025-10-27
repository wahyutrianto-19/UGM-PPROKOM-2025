#a
matrix = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
for row in matrix:
    print(row)

#b
n = int(input("Masukkan ukuran matriks identitas: "))

matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

for row in matrix:
    print(row)
