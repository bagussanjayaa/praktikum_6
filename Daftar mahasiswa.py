daftar_mahasiswa = []

def tambah(nama):
    daftar_mahasiswa.append(nama)
    print(f"Mahasiswa dengan nama {nama} telah ditambahkan.")

def tampilkan():
    if daftar_mahasiswa:
        print("Daftar Mahasiswa:")
        for i, nama in enumerate(daftar_mahasiswa, 1):
            print(f"{i}. {nama}")
    else:
        print("Tidak ada data mahasiswa.")

def hapus(nama):
    if nama in daftar_mahasiswa:
        daftar_mahasiswa.remove(nama)
        print(f"Mahasiswa dengan nama {nama} telah dihapus.")
    else:
        print(f"Mahasiswa dengan nama{nama} tidak ditemukan.")

def ubah(nama_lama, nama_baru):
    if nama_lama in daftar_mahasiswa:
        index = daftar_mahasiswa.index(nama_lama)
        daftar_mahasiswa[index] = nama_baru
        print(f"Mahasiswa dengan nama {nama_lama} telah diubah menjadi {nama_baru}.")
    else:
        print(f"Mahasiswa dengan nama {nama_lama} tidak ditemukan.")

tambah("Coki")
tambah("Lala")
tambah("Citra")
tambah("Rizal")
tambah("Putri")
tampilkan()
hapus("Lala")
tampilkan()
ubah("Citra", "Sarah")
tampilkan()
