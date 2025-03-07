dataPegawai = []

while True :
    print("\033c", end="")  
    print(6*"=" + " Menu " + "="*6)
    print("1. Masukkan Data Pegawai")
    print("2. Tampilkan Daftar Pegawai")
    print("3. Hitung Gaji Pegawai")
    print("4. Keluar")
    menu = input("Pilih menu (1-4) : ")

    if menu == "1" :
        print("\033c", end="")
        print("Menginput Data Pegawai")

        nama = input("Masukkan Nama : ")  
        nik = input("Masukkan NIK : ")  
        status = input("Masukkan Status (Tetap/Honor) : ").capitalize()  
        golongan = input("Masukkan Golongan (A/B/C) : ").upper()  
        
        gaji_bonus = {
            "Tetap": {"Gaji": 1_000_000, "Bonus": {"A": 200_000, "B": 400_000, "C": 550_000}},
            "Honor": {"Gaji": 750_000, "Bonus": {"A": 150_000, "B": 275_000, "C": 480_000}}
        }

        if status not in gaji_bonus or golongan not in gaji_bonus[status]["Bonus"]:
            print("Input status atau golongan tidak valid! Coba lagi.")
            input("Tekan enter untuk melanjutkan...")
            continue  

        gaji = gaji_bonus[status]["Gaji"]
        bonus = gaji_bonus[status]["Bonus"][golongan]

        dataPegawai.append({
            "Nama": nama,
            "NIK": nik,
            "Status": status,
            "Golongan": golongan,
            "Gaji": gaji,
            "Bonus": bonus
        })

        print("Data berhasil disimpan!\n")
        input("Tekan tombol enter untuk melanjutkan...")

    elif menu == "2" :
        print("\033c", end="")
        print("Daftar Pegawai")
        if not dataPegawai:
            print("Belum ada data pegawai.")
        else :
            for peg in dataPegawai :
                print(f"Nama : {peg['Nama']}, NIK : {peg['NIK']}, Status : {peg['Status']}, Golongan : {peg['Golongan']}")
        input("Tekan tombol enter untuk melanjutkan...")

    elif menu == "3" :
        print("\033c", end="")
        print("Hitung Gaji Pegawai")
        cariNIK = input("Masukkan NIK Pegawai : ")
        found = False
        
        for peg in dataPegawai :
            if peg["NIK"] == cariNIK :
                total_gaji = peg["Gaji"] + peg["Bonus"]
                print(f"Gaji Pegawai {peg['Nama']} (NIK : {peg['NIK']}) adalah Rp{total_gaji:,}".replace(",", "."))
                found = True
                break

        if not found:
            print("Pegawai dengan NIK tersebut tidak ditemukan.")

        input("Tekan enter untuk kembali ke menu...")

    elif menu == "4":
        print("Keluar dari program.")
        break

    else:
        input("Menu yang Anda pilih tidak valid! Tekan enter untuk pilih kembali (1-4)")
