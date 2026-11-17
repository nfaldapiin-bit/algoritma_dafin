print("======================================")
print("       APLIKASI TIKET BIOSKOP")
print("======================================")

nama = input("Masukkan nama pelanggan: ")

print("\nPILIH JENIS TIKET")
print("1. Regular  - Rp35.000")
print("2. VIP      - Rp50.000")
print("3. Premium  - Rp75.000")

pilihan = int(input("\nPilih jenis tiket (1/2/3): "))

if pilihan == 1:
    jenis_tiket = "Regular"
    harga = 35000
elif pilihan == 2:
    jenis_tiket = "VIP"
    harga = 50000
elif pilihan == 3:
    jenis_tiket = "Premium"
    harga = 75000
else:
    print("Pilihan tiket tidak tersedia!")
    exit()

jumlah = int(input("Masukkan jumlah tiket: "))

if jumlah <= 0:
    print("Jumlah tiket harus lebih dari 0!")
    exit()

total = harga * jumlah

print("\n======================================")
print("             DETAIL PESANAN")
print("======================================")
print("Nama Pelanggan :", nama)
print("Jenis Tiket    :", jenis_tiket)
print("Harga Tiket    : Rp", format(harga, ",").replace(",", "."))
print("Jumlah Tiket   :", jumlah)
print("Total Harga    : Rp", format(total, ",").replace(",", "."))

if jumlah > 3:
    diskon = total * 10 / 100
    print("Diskon 10%     : Rp", format(int(diskon), ",").replace(",", "."))
else:
    diskon = 0
    print("Diskon         : Tidak ada")

total_bayar = total - diskon

print("--------------------------------------")
print("Total Bayar    : Rp", format(int(total_bayar), ",").replace(",", "."))

print("\n======================================")
print("             PEMBAYARAN")
print("======================================")

bayar = int(input("Masukkan uang pembayaran: Rp "))

if bayar >= total_bayar:
    kembalian = bayar - total_bayar

    print("\n======================================")
    print("          STRUK PEMBELIAN")
    print("======================================")
    print("Nama Pelanggan :", nama)
    print("Jenis Tiket    :", jenis_tiket)
    print("Jumlah Tiket   :", jumlah)
    print("Total Harga    : Rp", format(total, ",").replace(",", "."))
    print("Diskon         : Rp", format(int(diskon), ",").replace(",", "."))
    print("Total Bayar    : Rp", format(int(total_bayar), ",").replace(",", "."))
    print("Uang Dibayar   : Rp", format(bayar, ",").replace(",", "."))
    print("Kembalian      : Rp", format(int(kembalian), ",").replace(",", "."))
    print("--------------------------------------")
    print("   TERIMA KASIH TELAH MEMESAN TIKET!")
    print("       SELAMAT MENONTON FILM")
    print("======================================")

else:
    print("\nUang pembayaran tidak mencukupi!")
    print("Kekurangan: Rp", format(int(total_bayar - bayar), ",").replace(",", "."))
    print("Silakan lakukan pembayaran kembali.")