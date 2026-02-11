FILE_BUKU = "buku.txt"


def load_buku():
    buku = []
    try:
        with open(FILE_BUKU, "r") as file:
            for line in file:
                data = line.strip().split("|")

            buku.append({
                    "id": data[0],
                    "judul": data[1],
                    "penulis": data[2],
                    "stok":
int(data[3])
                })
    except FileNotFoundError:
        pass
    return buku


def save_buku(buku):
    with open(FILE_BUKU, "w") as file:
        for b in buku:
            file.write(f"{b['id']}|{b['judul']}|{b['penulis']}|{['stok']}\n")

 # ------------------------------------
 # MENU
 # ------------------------------------

def menu():
    print("\n=== System Library ===")
    print("1. Lihat buku")
    print("2. Tambah buku")
    print("3. Update buku")
    print("4. Hapus buku")
    print("5. Pinjam buku")
    print("6. Kembalikan buku")
    print("7. Keluar")

# ----------------------------
# FITUR
# ----------------------------

def lihat_buku(buku):
    print("\nDAFTAR BUKU")
    print("-" * 40)
    for b in buku:
        print(f"ID: {b['judul']}")
        print(f"Judul: {b['judul']}")
        print(f"Penulis: {b['penulis']}")
        print(f"Stok: {b['stok']}")
        print("-" * 40)


def tambah_buku(buku):
    id_buku = input("ID Buku: ")
    judul = input("Judul: ")
    penulis = input("Penulis: ")
    stok = int(input("Stok: "))

    buku.append({
        "id": id_buku,
        "judul": judul,
        "penulis": penulis,
        "stok": stok
    })
    save_buku(buku)
    print("Buku berhasil ditambahkan")


def update_buku(buku):
    id_buku = input("Masukkan ID Buku: ")

    for b in buku:
        if b["id"] == id_buku:
            b["judul"] = input("Judul baru:")

            b["penulis"] = input("Penulis baru: ")
            
            b["stok"] = int(input("Stok baru: "))

            save_buku(buku)
            print("Buku berhasil di update")

            return
        print("Buku tidak ditemukan")

def hapus_buku(buku):
    id_buku = input("Masukkan ID Buku: ")

    for b in buku:
        if b["id"] == id_buku:
            buku.remove(b)
            save_buku(buku)
            print("Buku dihapus")
            return
        print("Buku tidak ditemukan")


def pinjam_buku(buku):
    id_buku = input("ID Buku: ")
    for b in buku:
        if b["id"] == id_buku:
            if b["stok"] > 0:
                b["stok"] -= 1
                save_buku(buku)
                print("Buku berhasil dipinjam")

            else: 
                print("Stok habis")
            return
        print("Buku tidak ditemukan")


def kembalikan_buku(buku):
    id_buku = input("ID Buku: ")
    for b in buku:
        if b["id"] == id_buku:
            b["stok"] += 1
            save_buku(buku)
            print("Buku berhasil dikembalikan")
            
            return
        print("Buku tidak ditemukan")


#--------------------------------------
# LOGIN
#--------------------------------------
def login():
    username = "admin"
    password = "123"

    for _ in range(3):
        u = input("Username: ")
        p = input("Password: ")
        if u == username and p == password:
            print("Login berhasil")
            return True
        else:
            print("Salah")
    return False


# -----------------------------
# PROGRAM UTAMA
# -----------------------------
if login():
    buku = load_buku()
    while True:
        menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_buku(buku)
        elif pilihan == "2":
            tambah_buku(buku)
        elif pilihan == "3":
            update_buku(buku)
        elif pilihan == "4":
            hapus_buku(buku)
        elif pilihan == "5":
            pinjam_buku(buku)
        elif pilihan == "6":
            kembalikan_buku(buku)
        elif pilihan == "7":
            print("Program Selesai")
            break
        else:
            print("Menu tidak valid")