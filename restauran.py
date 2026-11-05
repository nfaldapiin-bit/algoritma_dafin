print("<==============================>")
print("       Agam Denai")

total = 0
nama = input("Masukkan Nama: ")
print("\nhalo selamat datang",nama)

while True:
    print("\n<=====MENU MAKANAN=====>")
    print("1. Mie Gomak        - Rp16.000")
    print("2. Martabak Royal  - Rp15.000")
    print("3. Ayam Geprek      - Rp22.000")
    print("4. Taichan         - Rp30.000")
    print("5. Mie Bangladesh  - Rp13.000")
    print("0. Selesai Memilih")

    pilihan = int(input("Pilih menu (0-5): "))

    if pilihan == 0:
        break

    elif pilihan == 1:
        harga = 16000
        nama_menu = "Mie Gomak"

    elif pilihan == 2:
        harga = 15000
        nama_menu = "Martabak Royal"

    elif pilihan == 3:
        harga = 22000
        nama_menu = "Ayam Geprek"

    elif pilihan == 4:
        harga = 30000
        nama_menu = "Taichan"

    elif pilihan == 5:
        harga = 13000
        nama_menu = "Mie Bangladesh"

    else:
        print("Pilihan tidak tersedia!")
        continue

    jumlah = int(input("Masukkan jumlah pesanan: "))

    if jumlah <= 0:
        print("Jumlah pesanan harus lebih dari 0!")
        continue

    subtotal = harga * jumlah
    total = total + subtotal

    print("\nPesanan berhasil!")
    print("Menu:", nama_menu)
    print("Harga:", harga)
    print("Jumlah:", jumlah)
    print("Subtotal:", subtotal)
    print("Total sementara:", total)

if total > 200000:
    persen_diskon = 20
    diskon = total * 0.20
else:
    persen_diskon = 0
    diskon = 0
total_bayar = total - diskon

print("\n================================")
print("       STRUK PEMBAYARAN")

print("Total Belanja :Rp",total)
print("Diskon        :", str(persen_diskon) + "%")
print("Diskon        :Rp",diskon)
print("================================")
print("Total Bayar   :Rp",total_bayar)

print("================================")
print("       TERIMA KASIH")
print("   selamat menikmati kak",nama)