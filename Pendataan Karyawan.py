#Projek Ujian Akhir Praktikum Dasar Pemograman dan Algoritma
#Tema: Pendataan Karyawan
#Dosen Pengampu: M. Yhogha Ismail Ibn Ibrahim, M.T.I.
#Asisten Dosen : R. Revaldo Vabiansyah 2417052021
#                Raid Fadhil Khairi    2417052004
#=====================================
#Kelompok NED
#Anggota:
#ELFRADA P NAPITUPULU	2517052019
#NUR ELIA SOFIA	        2517052027
#DEVINA ADELIA PUTRI	2517052025
#=====================================


data_karyawan = []

def simpan_ke_file():
    try:
        with open("data_karyawan.txt", "w") as f:
            for k in data_karyawan:
                baris = f"{k['id]} | {k['nama']} | {k['jabatan'}] | {k['gaji'}] \n"
                f.write(baris)
    except:
        print("Gagal menyimpan ke file"


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


def tambah_data():
    print("\n=== Tambah Data Karyawan ===")
    id = input("ID Karyawan       : ")
    nama = input("Nama Karyawan     : ")
    jabatan = input("Jabatan(CEO,Manajer,Supervisor,Staf):")
    if jabatan.upper() == "CEO":
        gaji = 25000000
        print(f"Gaji              :{gaji} ")
    elif jabatan.title() == "Manajer":
        gaji = 12000000
        print(f"Gaji              :{gaji} ")
    elif jabatan.title() == "Supervisor":
        gaji = 8000000
        print(f"Gaji              :{gaji} ")
    elif jabatan.title() == "Staf":
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

    print("Data berhasil ditambahkan!")



