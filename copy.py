import os

# Fungsi untuk membersihkan layar terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Variabel untuk menyimpan data pesanan
total_harga = 0
sudah_memesan = False

# Perulangan utama program
while True:
    clear_screen()
    print("===================================")
    print("   SELAMAT DATANG DI RESTORAN ")
    print("===================================")
    print("MENU UTAMA:")
    print("1. Makanan")
    print("2. Minuman")
    print("3. Struk / Pembayaran")
    print("4. Keluar")
    print("===================================")

    pilihan = input("Masukkan Pilihan (1/2/3/4): ")

    # ========================= MENU MAKANAN =========================
    if pilihan == '1':
        while True:
            clear_screen()
            print("=== MENU MAKANAN ===")
            print("1. Nasi Goreng  - Rp 30.000")
            print("2. Mie Ayam     - Rp 20.000")
            print("3. Ayam Bakar   - Rp 30.000")
            print("4. Kembali ke Menu Utama")
            print("===================================")

            makanan = input("Masukkan Pilihan (1/2/3/4): ")

            if makanan == '1':
                jumlah = int(input("Masukkan jumlah porsi: "))
                total = jumlah * 30000
            elif makanan == '2':
                jumlah = int(input("Masukkan jumlah porsi: "))
                total = jumlah * 20000
            elif makanan == '3':
                jumlah = int(input("Masukkan jumlah porsi: "))
                total = jumlah * 30000
            elif makanan == '4':
                break  # keluar dari submenu makanan
            else:
                print("Pilihan makanan tidak tersedia.")
                input("Tekan Enter untuk lanjut...")
                continue

            total_harga += total
            sudah_memesan = True
            print(f"Total sementara: Rp {total_harga:,}")
            input("Tekan Enter untuk kembali ke menu makanan...")

    # ========================= MENU MINUMAN =========================
    elif pilihan == '2':
        while True:
            clear_screen()
            print("=== MENU MINUMAN ===")
            print("1. Es Teh    - Rp 5.000")
            print("2. Es Jeruk  - Rp 7.000")
            print("3. Teh Anget - Rp 4.000")
            print("4. Kembali ke Menu Utama")
            print("===================================")

            minuman = input("Masukkan Pilihan (1/2/3/4): ")

            if minuman == '1':
                jumlah = int(input("Masukkan jumlah gelas: "))
                total = jumlah * 5000
            elif minuman == '2':
                jumlah = int(input("Masukkan jumlah gelas: "))
                total = jumlah * 7000
            elif minuman == '3':
                jumlah = int(input("Masukkan jumlah gelas: "))
                total = jumlah * 4000
            elif minuman == '4':
                break  # keluar dari submenu minuman
            else:
                print("Pilihan minuman tidak tersedia.")
                input("Tekan Enter untuk lanjut...")
                continue

            total_harga += total
            sudah_memesan = True
            print(f"Total sementara: Rp {total_harga:,}")
            input("Tekan Enter untuk kembali ke menu minuman...")

    # ========================= STRUK PEMBAYARAN =========================
    elif pilihan == '3':
        if not sudah_memesan:
            print("Anda belum memesan apa pun!")
            input("Tekan Enter untuk kembali ke menu...")
            continue

        # Mulai proses pembayaran
        while True:
            clear_screen()
            print("=== STRUK PEMBAYARAN ===")
            print(f"Total Semua Pesanan: Rp {total_harga:,}")

            print("\nPilih Metode Pembayaran:")
            print("1. Tunai")
            print("2. QRIS")
            print("3. Debit")
            print("4. eWallet (GoPay / OVO / DANA)")
            print("5. Kembali ke Menu Utama")
            metode = input("Masukkan pilihan (1/2/3/4/5): ")

            if metode == '5':
                break  # kembali ke menu utama

            # ================= TUNAI =================
            if metode == '1':
                try:
                    bayar = int(input("Masukkan jumlah uang tunai: Rp "))
                except ValueError:
                    print("Input tidak valid. Masukkan angka!")
                    input("Tekan Enter untuk ulang...")
                    continue

                if bayar < total_harga:
                    print(f"Uang Anda kurang Rp {total_harga - bayar:,}")
                    print("Silakan pilih metode pembayaran lain (QRIS / eWallet).")
                    input("Tekan Enter untuk kembali...")
                    continue
                else:
                    kembalian = bayar - total_harga
                    print(f"Kembalian Anda: Rp {kembalian:,}")
                    print("pmbayaran Tunai berhasil.")

            # ================= QRIS =================
            elif metode == '2':
                print("Silakan scan QRIS di layar kasir untuk membayar.")
                input("Tekan Enter setelah pembayaran selesai...")
                print("pembayaran QRIS berhasil.")

            # ================= DEBIT =================
            elif metode == '3':
                print("Silakan gesek kartu debit Anda di mesin EDC.")
                input("Tekan Enter setelah pembayaran selesai...")
                print("pembayaran Debit berhasil.")

            # ================= EWALLET =================
            elif metode == '4':
                print("Silakan pilih eWallet Anda (GoPay / OVO / DANA).")
                input("Tekan Enter setelah pembayaran selesai...")
                print("Pembayaran eWallet berhasil.")

            else:
                print("Metode pembayaran tiak dikenali.")
                input("Tekan Enter untuk kembali...")
                continue

            print("\n=== TERIMA KASIH SUDAH BERKUNJUNG KE RESTORAN ===")
            input("Tekan Enter untuk keluar...")
            exit()  # keluar dari program

    # ========================= KELUAR DARI PROGRAM =========================
    elif pilihan == '4':
        clear_screen()
        print("Terima kasih! Sampai jumpa lagi.")
        break

    # ========================= PILIHAN TIDAK VALID =========================
    else:
        print("Pilihan tidak ada di menu.")
        input("Tekan Enter untuk coba lagi...")