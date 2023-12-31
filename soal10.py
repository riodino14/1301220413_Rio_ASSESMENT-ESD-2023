def calculate_change(total_pembayaran, total_belanja):
    pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    kembalian = total_pembayaran - total_belanja
    result = {}
    for pecahan in pecahan_uang:
        if kembalian >= pecahan:
            result[str(pecahan)] = kembalian // pecahan
            kembalian %= pecahan
    return result

total_pembayaran = int(input("Total Pembayaran: "))
total_belanja = int(input("Total Belanja: "))

result = calculate_change(total_pembayaran, total_belanja)

print(f"Kembalian yang harus diberikan adalah:")
for pecahan in result:
    print(f"{result[pecahan]} keping {pecahan} rupiah")
