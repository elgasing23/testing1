
def add_data():
    while True:
        npm = input("Masukkan NPM mahasiswa: ")
        if npm in data_mahasiswa:
            print("NPM sudah terdaftar, silahkan coba lagi.")
            continue
        elif not npm.isalpha:
            print("NPM harus berupa angka, silahkan coba lagi.")

        list_minat = []
        while True:
            minat = input("Masukkan minat mahasiswa ('exit' untuk keluar): ")
            if minat == 'exit':
                break
            elif minat in list_minat:
                continue
            else:
                list_minat.append(minat)
        data_mahasiswa[npm] = list_minat
        print("Data mahasiswa berhasil ditambahkan.")
        break
    



def erase_data():
    while True:
        npm = int(input("Masukkan NPM mahasiswa yang ingin dihapus: "))
        if npm in data_mahasiswa:
            del data_mahasiswa[f"{npm}"]
            print("Data mahasiswa berhasil dihapus.")
            break
        elif npm not in data_mahasiswa:
            print("NPM tidak ditemukan dalam daftar, silahkan coba lagi.")


def list_mahasiswa():
    if len(data_mahasiswa) == 0:
        print("Belum ada data mahasiswa yang terdaftar.")
    else:
        for npm, minat_list in data_mahasiswa.items():
            print(f"NPM: {npm}, Minat: {', '.join(minat_list)}")


def list_seluruh_minat():
    if len(data_mahasiswa.values()) == 0:
        print("Belum ada data minat yang terdaftar.")
    else:
        for npm, minat_list in data_mahasiswa.items():
            print(f"Daftar seluruh minat mahasiswa: {', '.join(minat_list)}")
           









def main():
    global data_mahasiswa
    data_mahasiswa = {}
    while True:
        print("""===== Main Menu ===== 
1. Menambah data mahasiswa 
2. Menghapus data mahasiswa 
3. List seluruh mahasiswa 
4. List seluruh minat 
5. Keluar""")
        pilihan = int(input("Pilihan: "))
        
        if pilihan == 1:
            add_data()
        elif pilihan == 2:
            erase_data()
        elif pilihan == 3:
            list_mahasiswa()
        elif pilihan == 4:
            list_seluruh_minat()
        elif pilihan == 5:
            break
            
        
if __name__ == "__main__":
    main()
