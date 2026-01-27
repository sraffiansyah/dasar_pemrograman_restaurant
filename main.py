import os
import sys
import time

# Fungsi untuk membersihkan layar terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# function buat ngatur format rupiah biar rapih
def formatRupiah(angka):
    return f"Rp {angka:,},-".replace(",", ".") 

#function buat nangkep angka doang
def inputAngka(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Input tidak valid. Masukkan angka!")

def print_per_huruf(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Variabel untuk menyimpan data pesanan
sudahMemesan = False
sudahBayar = False
totalHarga = 0
totalHargaAll = 0
no = 0
uangBayar = 0
uangKembalian = 0
pesanan = []

# Perulangan utama program
while True:
    clear_screen()
    print(f"total Harga saat ini : {formatRupiah(totalHargaAll)} \n" )
    print(" ______________________________________")
    print("|              RESTAURANT              |")
    print("|--------------------------------------|")
    print("| NO  |          MENU UTAMA            |")
    print("|-----|--------------------------------|")
    print("| 1.  |  Makanan                       |")
    print("| 2.  |  Minuman                       |")
    print("| 3.  |  Struk / Pembayaran            |")
    print("| 4.  |  Keluar                        |")
    print("|______________________________________|")

    pilihan = input("Masukkan Pilihan (1/2/3/4): ")

    # Menu Makanan
    if pilihan == '1':
        if sudahBayar == True :
            clear_screen()
            print_per_huruf("Anda sudah melakukan pembayaran, tidak bisa memesan lagi!")
            print_per_huruf("Anda akan kembali ke menu utama...")
            time.sleep(2.5)
            continue

        while True:
            clear_screen()
            print(f"total Harga pesanan saat ini:  {formatRupiah(totalHargaAll)}\n")
            print(" __________________________________________________")
            print("|  NO  |        MENU MAKANAN      |     Harga      |")
            print("| -----|--------------------------|--------------- |")
            print(f"|  1.  |  {'Nasi Goreng':23} |  {formatRupiah(30000):12}  |")
            print(f"|  2.  |  {'Mie Ayam':23} |  {formatRupiah(20000):12}  |")
            print(f"|  3.  |  {'Ayam Bakar':23} |  {formatRupiah(30000):12}  |")
            print("|  4.  |  Kembali ke Menu Utama                    |")
            print("|__________________________________________________|")

            makanan = input("Masukkan Pilihan (1/2/3/4): ")
            if makanan == '1':
                jenis = "Nasi Goreng"
                harga = 30000
            elif makanan == '2':
                jenis = "Mie Ayam"
                harga = 20000
            elif makanan == '3':
                jenis = "Ayam Bakar"
                harga = 30000
            elif makanan == '4':
                break
            else:
                print("Pilihan makanan tidak tersedia.")
                print("Coba pilih lagi...")
                time.sleep(1.5)             
                continue

            jumlah = inputAngka("Masukkan Jumlah Porsi : ")

            totalHarga = jumlah * harga
            totalHargaAll = totalHargaAll + totalHarga
            sudahMemesan = True
            no += 1
            pesanan.append((no, jenis, jumlah, harga, totalHarga))
            print(f"Harga pesanan yang baru dipesan: {formatRupiah(totalHarga)} \n" )

            while True:
                beliLagi = input("Ingin memesan lagi? (y/n) : ").lower()
                if beliLagi == 'y':
                    print("silahkan pilih lagi...")
                    time.sleep(1)
                    break
                elif beliLagi == 'n':
                    print("Kembali ke menu utama...")
                    time.sleep(1.5)
                    break 
                else : 
                    print("Input tidak valid. Masukkan 'y' atau 'n'!")
                    time.sleep(1.5)
                    continue
            if beliLagi == 'n':
                break

    # ========================= MENU MINUMAN =========================
    elif pilihan == '2':
        if sudahBayar == True :
            clear_screen()
            print_per_huruf("Anda sudah melakukan pembayaran, tidak bisa memesan lagi!")
            print_per_huruf("Anda akan kembali ke menu utama...")
            time.sleep(2.5)
            continue

        while True:
            clear_screen()
            print(f"total Harga pesanan saat ini:  {formatRupiah(totalHargaAll)}\n")
            print(" __________________________________________________")
            print("|  NO  |        MENU MAKANAN      |     Harga      |")
            print("| -----|--------------------------|--------------- |")
            print(f"|  1.  |  {'Es Teh':23} |  {formatRupiah(5000):12}  |")
            print(f"|  2.  |  {'Es Jeruk':23} |  {formatRupiah(7000):12}  |")
            print(f"|  3.  |  {'Teh Anget':23} |  {formatRupiah(4000):12}  |")
            print("|  4.  |  Kembali ke Menu Utama                    |")
            print("|__________________________________________________|")

            makanan = input("Masukkan Pilihan (1/2/3/4): ")
            if makanan == '1':
                jenis = "Es Teh"
                harga = 5000
            elif makanan == '2':
                jenis = "Es Jeruk"
                harga = 7000
            elif makanan == '3':
                jenis = "Teh Anget"
                harga = 4000
            elif makanan == '4':
                break
            else:
                print("Pilihan makanan tidak tersedia.")
                print("Coba pilih lagi...")
                time.sleep(1.5)             
                continue

            jumlah = inputAngka("Masukkan Jumlah Porsi : ")

            totalHarga = jumlah * harga
            totalHargaAll = totalHargaAll + totalHarga
            sudahMemesan = True
            no += 1
            pesanan.append((no, jenis, jumlah, harga, totalHarga))
            print(f"Harga pesanan yang baru dipesan: {formatRupiah(totalHarga)} \n" )

            while True:
                beliLagi = input("Ingin memesan lagi? (y/n) : ").lower()
                if beliLagi == 'y':
                    print("silahkan pilih lagi...")
                    time.sleep(1)
                    break
                elif beliLagi == 'n':
                    print("Kembali ke menu utama...")
                    time.sleep(1.5)
                    break 
                else : 
                    print("Input tidak valid. Masukkan 'y' atau 'n'!")
                    time.sleep(1.5)
                    continue
            if beliLagi == 'n':
                break


    # ========================= STRUK PEMBAYARAN =========================
    elif pilihan == '3':
        if not sudahMemesan:
            print("Anda belum memesan apa pun!")
            time.sleep(1)
            print("Silahkan memesan terlebih dahulu")
            time.sleep(2)
            continue

        # Mulai proses pembayaran
        while True:
            clear_screen()
            print(f" _________________________________________________________________________________ ")
            print(f"|                             ***** RESTAURANT *****                              |")
            print(f"| ------------------------------------------------------------------------------- |")
            print(f"|   NO  |  Pesanan           |  Jumlah  |  Harga Satuan  |  Jumlah Harga          |")
            print(f"| ------|--------------------|----------|----------------|----------------------- |")
            for no, jenis, jumlah, harga, totalHarga in pesanan:
                print(f"| {no:^6}|  {jenis:<17} |  {jumlah:^6}  |  {formatRupiah(harga):<12}  |  {formatRupiah(totalHarga):<20}  |")
            print(f"| -------------------------------------------------------|--------------------- + |")
            print(f"|  {"Total Harga":>52}  |  {formatRupiah(totalHargaAll):<20}  |")
            if sudahBayar == True :
                print(f"|  {"Bayar":>52}  |  {formatRupiah(uangBayar):<20}  |")
                print(f"|  {"Kembalian":>52}  |  {formatRupiah(uangKembalian):<20}  |")
            print(f"|_________________________________________________________________________________|")

            if sudahBayar == False:
                bayar = inputAngka("Masukkan Jumlah Uang Pembayaran: Rp ")
                if bayar < totalHargaAll:
                    print("Uang yang Anda masukkan kurang!")
                    input("Tekan Enter untuk ulang...")
                    continue
                else:
                    print("Pembayaran Anda sedang di proses...")
                    time.sleep(3)
                    uangBayar = bayar
                    uangKembalian = uangBayar - totalHargaAll
                    sudahBayar = True  
            else :
                print("\n\nAnda sudah melakukan pembayaran.")
                input("\nTekan Enter untuk kembali ke menu utama...")
                break

    # ========================= KELUAR DARI PROGRAM =========================
    elif pilihan == '4':
        clear_screen()
        print("Terima kasih! Sampai jumpa lagi.")
        break

    # ========================= PILIHAN TIDAK VALID =========================
    else:
        print(f"Pilihan tidak ada di menu. \nSilahkan pilih lagi...")
        time.sleep(2)
        continue