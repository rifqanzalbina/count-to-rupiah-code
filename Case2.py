import locale
import rupiah

# Tempat menyimpan barang
daftar_barang = {'apel':20000, "jeruk":20000, "mangga":25000, "pisang":12000}

# List untuk menyimpan barang yang akan dibeli
keranjang = []

# Meminta user memasukkan barang yang dibeli dan jumlahnya
while True:
    barang = input("Masukkan Barang Yang Ingin Dibeli (ketik 'selesai' jika sudah selesai belanja) (apel, jeruk, mangga, pisang): ")
    if barang.lower() == "selesai":
        break
    elif barang not in daftar_barang:
        print("Maaf, barang tidak tersedia")
        continue
    jumlah = int(input("Masukkan jumlah barang yang dibeli : "))
    keranjang.append((barang, jumlah))

# Menghitung total belanja 
total = 0 
for barang, jumlah in keranjang:
    harga = daftar_barang[barang] * jumlah
    total += harga 

# Menampilkan struk Pembayaran 
print("=== Struk Pembayaran ===")
for barang, jumlah in keranjang:
    harga = daftar_barang[barang] * jumlah
    print(f"{barang} x {jumlah} : {harga}")
print("========================")
print(f"Total: Rp. {rupiah.rupiah_format(total)}")