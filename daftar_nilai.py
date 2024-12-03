'''Inisialisasi daftar mahasiswa'''
daftar_mahasiswa = []

'''Fungsi untuk menambah data mahasiswa'''
def tambah(nama, nim, jurusan, nilai):
    mahasiswa = {'nama': nama, 'nim': nim, 'jurusan': jurusan, 'nilai': nilai}
    daftar_mahasiswa.append(mahasiswa)
    print(f"Mahasiswa dengan nama {nama} telah ditambahkan.")

'''Fungsi untuk menampilkan data mahasiswa'''
def tampilkan():
    if not daftar_mahasiswa:
        print("Tidak ada data mahasiswa.")
    else:
        for i, mahasiswa in enumerate(daftar_mahasiswa, start=1):
            print(f"{i}. Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}, Jurusan: {mahasiswa['jurusan']}, Nilai: {mahasiswa['nilai']}")

'''Fungsi untuk menghapus data mahasiswa berdasarkan nama'''
def hapus(nama):
    global daftar_mahasiswa
    daftar_mahasiswa = [mahasiswa for mahasiswa in daftar_mahasiswa if mahasiswa['nama'] != nama]
    print(f"Mahasiswa dengan nama {nama} telah dihapus.")

'''Fungsi untuk mengubah data mahasiswa berdasarkan nama'''
def ubah(nama, nama_baru=None, nim_baru=None, jurusan_baru=None, nilai_baru=None):
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa['nama'] == nama:
            if nama_baru:
                mahasiswa['nama'] = nama_baru
            if nim_baru:
                mahasiswa['nim'] = nim_baru
            if jurusan_baru:
                mahasiswa['jurusan'] = jurusan_baru
            if nilai_baru:
                mahasiswa['nilai'] = nilai_baru

            print(f"Data mahasiswa dengan nama {nama} telah diubah.")
            return
    print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

'''Contoh penggunaan fungsi'''
tambah("Coki", "1223", "Teknik Informatika", "80")
tambah("Lala", "1224", "Teknik Informatika", "95")
tambah("Citra", "1225", "Teknik Informatika", "90")
tambah("Rizal", "1226", "Teknik Informatika", "88")
tambah("Putri", "1227", "Teknik Informatika", "92")
tampilkan()
hapus("Lala")
tampilkan()
ubah("Citra", nama_baru="Sarah", nim_baru="1228", jurusan_baru="Teknik Informatika", nilai_baru="94")
tampilkan()
