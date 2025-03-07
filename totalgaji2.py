nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Pegawai Tetap/Honor): ")
golongan = input("Masukkan Golongan (A/B/C): ")

if status.lower() == "pegawai tetap":
    gaji_pokok = 1000000
    bonus = {"a": 200000, "b": 400000, "c": 550000}.get(golongan.lower(), 0)
elif status.lower() == "honor":
    gaji_pokok = 750000
    bonus = {"a": 150000, "b": 275000, "c": 480000}.get(golongan.lower(), 0)
else:
    print("Status tidak valid.")
    exit()

gaji_total = gaji_pokok + bonus

print("\n=== Rincian Gaji ===")
print(f"Nama: {nama}")
print(f"NIK: {nik}")
print(f"Status: {status}")
print(f"Golongan: {golongan}")
print(f"Gaji Pokok: Rp {gaji_pokok}")
print(f"Bonus: Rp {bonus}")
print(f"Gaji Total: Rp {gaji_total}")