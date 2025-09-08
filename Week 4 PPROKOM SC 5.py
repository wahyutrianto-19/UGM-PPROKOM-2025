siswa = []
for i in range(5):
    nama = input(f"Masukkan nama siswa ke-{i+1}:")
    nilai = int(input(f"Masukkan nilai {nama}:"))
    siswa.append((nama, nilai))
    
print("\n=== Hasil Kelulusan Siswa===")
for nama,nilai in siswa:
    if nilai >= 70:
        print(f"{nama} : Lulus (nilai = {nilai})")
    else:
        print(f"{nama} : Tidak Lulus (nilai = {nilai})")