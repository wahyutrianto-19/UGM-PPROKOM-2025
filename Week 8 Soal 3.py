from array import array
angka = array('i', [10, 20, 30, 40, 50])

print("Isi array :", angka)
print("Panjang array:", len(angka))

total = sum(angka)
print("Jumlah total elemen:", total)

rata_rata = total / len(angka)
print("Nilai rata-rata:", rata_rata)
