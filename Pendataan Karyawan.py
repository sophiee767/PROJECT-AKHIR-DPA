# ============================
# PROGRAM PENDATAAN KARYAWAN
# ============================

data_karyawan = []

# Fungsi Menyimpan ke File 
def simpan_ke_file():
    try:
        with open("data_karyawan.txt", "w") as f:
            for k in data_karyawan:
                baris = f"{k['id']} | {k['nama']} | {k['jabatan']} | {k['gaji']} \n"
                f.write(baris)
    except:
        print("Gagal menyimpan ke file.")

def muat_dari_file():
    try:
        with open("data_karyawan.txt", "r") as f:
            for baris in f:
                if baris == "":
                    continue
                id, nama, jabatan, gaji = baris.strip().split("|")
                
                data_karyawan.append({
                    "id": id,
                    "nama": nama,
                    "jabatan": jabatan,
                    "gaji": gaji
                })
    except FileNotFoundError:
        pass 


# Fungsi Tambah Data
def tambah_data():
    print("\n=== Tambah Data Karyawan ===")
    id = input("ID Karyawan       : ")
    nama = input("Nama Karyawan     : ")
    jabatan = input("Jabatan(CEO,Manajer,Supervisor,Staf):")
    if jabatan == "CEO":
        gaji = 25000000
        print(f"Gaji              :{gaji} ")
    elif jabatan == "Manajer":
        gaji = 12000000
        print(f"Gaji              :{gaji} ")
    elif jabatan == "Supervisor":
        gaji = 8000000
        print(f"Gaji              :{gaji} ")
    elif jabatan == "Staf":
        gaji = 4500000
        print(f"Gaji              :{gaji} ")
    else:
        print("Coba Lagi")
        

    data_karyawan.append({
        "id": id,
        "nama": nama,
        "jabatan": jabatan,
        "gaji": gaji
    })

    print("✔ Data berhasil ditambahkan!")

# Fungsi Tampilkan Data
def tampilkan_data():
    print("\n=== Data Karyawan ===")
    if len(data_karyawan) == 0:
        print("Belum ada data.")
        return

    for k in data_karyawan:
        print(f"ID: {k['id']} |Nama: {k['nama']} |Jabatan: {k['jabatan']} |Gaji: {k['gaji']}")

# Fungsi Cari / Filter Data
def cari_data():
    print("\n=== Cari Data Karyawan ===")
    kata = input("Masukkan kata kunci (nama/jabatan): ").lower()

    hasil = []
    for k in data_karyawan:
        if kata in k["nama"].lower() or kata in k["jabatan"].lower():
            hasil.append(k)

    if len(hasil) == 0:
        print("Data tidak ditemukan.")
    else:
        print(f"✔ Ditemukan {len(hasil)} data:")
        for k in hasil:
            print(f"- {k['id']} | {k['nama']} | {k['jabatan']} | {k['gaji']}")

# Fungsi Edit Data
def edit_data():
    print("\n=== Edit Data Karyawan ===")
    id_cari = input("Masukkan ID yang ingin diedit: ")

    for k in data_karyawan:
        if k["id"] == id_cari:
            print("Data ditemukan. Kosongkan jika tidak ingin mengubah.")
            nama_baru = input(f"Nama baru ({k['nama']}): ")
            jabatan_baru = input(f"Jabatan baru ({k['jabatan']}): ")
            gaji_baru = input(f"Gaji baru ({k['gaji']}): ")

            if nama_baru != "":
                k["nama"] = nama_baru
            if jabatan_baru != "":
                k["jabatan"] = jabatan_baru
            if gaji_baru != "":
                k["gaji"] = gaji_baru

            print("✔ Data berhasil diperbarui!")
            return

    print("❌ ID tidak ditemukan.")

# Fungsi Hapus Data
def hapus_data():
    print("\n=== Hapus Data Karyawan ===")
    id_cari = input("Masukkan ID yang ingin dihapus: ")

    for k in data_karyawan:
        if k["id"] == id_cari:
            data_karyawan.remove(k)
            print("✔ Data berhasil dihapus!")
            return

    print("❌ ID tidak ditemukan.")

#Menu Utama
def menu():
    muat_dari_file()  

    while True:
        print("\n===== Pendataan Karyawan =====")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Cari Data")
        print("4. Edit Data")
        print("5. Hapus Data")
        print("6. Simpan ke File")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            cari_data()
        elif pilihan == "4":
            edit_data()
        elif pilihan == "5":
            hapus_data()
        elif pilihan == "6":
            simpan_ke_file()
            print("✔ Data disimpan ke file!")
        elif pilihan == "0":
            print("Program selesai. Terima kasih! hehe.")
            break
        else:
            print("❌ Pilihan tidak valid!")

menu()