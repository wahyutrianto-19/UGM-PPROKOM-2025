# Program menghitung rata-rata nilai

jumlah_nilai = int(input("Masukkan jumlah nilai yang ingin dihitung rata-ratanya: "))
total = 0
for i in range(jumlah_nilai):
    nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
    total += nilai
rata_rata = total / jumlah_nilai
print(f"Rata-rata dari {jumlah_nilai} nilai adalah: {rata_rata}")
