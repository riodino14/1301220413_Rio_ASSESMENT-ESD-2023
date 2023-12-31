menu = {
    "Ayam Goreng Krispi": {"tipe": "Makanan", "harga": 15000},
    "Ayam Puk Puk": {"tipe": "Makanan", "harga": 13000},
    "Ayam Bakar": {"tipe": "Makanan", "harga": 20000},
    "Es Teh": {"tipe": "Minuman", "harga": 5000},
    "Es Jeruk": {"tipe": "Minuman", "harga": 7000}
}

def hitung_biaya(pesanan):
    total = 0
    for item, jumlah in pesanan.items():
        item_info = menu.get(item)
        if item_info:
            subtotal = item_info["harga"] * jumlah

            if item_info["tipe"] == "Makanan":
                subtotal *= 1.05  
            elif item_info["tipe"] == "Minuman":
                subtotal *= 1.03  

            total += subtotal

    total *= 1.15  
    return total

rehan_pesanan = {"Ayam Bakar": 2, "Es Teh": 1}
amba_pesanan = {"Ayam Puk Puk": 1, "Es Teh": 3}
faiz_pesanan = {"Ayam Goreng Krispi": 1, "Ayam Puk Puk": 1, "Ayam Bakar": 1, "Es Teh": 1, "Es Jeruk": 1}


biaya_rehan = hitung_biaya(rehan_pesanan)
biaya_amba = hitung_biaya(amba_pesanan)
biaya_faiz = hitung_biaya(faiz_pesanan)


print("Biaya Rehan Whangsap: Rp", biaya_rehan)
print("Biaya Amba Roni: Rp", biaya_amba)
print("Biaya Faiz Ngawi: Rp", biaya_faiz)
