nama_teman = []
for i in range(5):
    nama = input(f"Masukkan nama teman ke-{i+1}: ")
    nama_teman.append(nama)

print("\nDaftar nama teman:")
for i in range(len(nama_teman)):
    print(f"Indeks {i}: {nama_teman[i]}")

indeks = int(input("\nIngin mengganti nama pada indeks ke berapa? "))
nama_baru = input("Masukkan nama penggantinya: ")

nama_teman[indeks] = nama_baru

print("\nDaftar nama teman setelah diperbarui:")
for i in range(len(nama_teman)):
    print(f"Indeks {i}: {nama_teman[i]}")

