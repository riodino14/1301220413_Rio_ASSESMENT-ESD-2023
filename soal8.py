# Data produk
produk = [
    {"Nama": "TV", "Kategori": "elektronik", "Harga": 1000},
    {"Nama": "headphone", "Kategori": "elektronik", "Harga": 200},
    {"Nama": "baju", "Kategori": "fashion", "Harga": 50},
    {"Nama": "gitar", "Kategori": "musik", "Harga": 300},
    {"Nama": "sepatu", "Kategori": "olahraga", "Harga": 80},
    {"Nama": "kamera", "Kategori": "elektronik", "Harga": 600},
]

# Data pelanggan dan preferensi
data_pelanggan = {
    "Rina": {"Minat": ["elektronik", "musik"], "Beli": ["TV", "headphone"]},
    "Budi": {"Minat": ["fashion", "musik"], "Beli": ["baju", "gitar"]},
    "Hartono": {"Minat": ["olahraga", "elektronik"], "Beli": ["sepatu", "kamera"]},
}

def rekomendasi_produk(pelanggan):
    minat_pelanggan = data_pelanggan[pelanggan]["Minat"]
    produk_terpilih = []

    for p in produk:
        if p["Kategori"] in minat_pelanggan and p["Nama"] not in data_pelanggan[pelanggan]["Beli"]:
            produk_terpilih.append(p["Nama"])

    return produk_terpilih

# Contoh penggunaan
nama_pelanggan = "Rina"
hasil_rekomendasi = rekomendasi_produk(nama_pelanggan)
print(f"{nama_pelanggan}: {hasil_rekomendasi}")
