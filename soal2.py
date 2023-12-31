def cek_palindrom(teks):

    teks = teks.lower().replace(" ", "")


    if teks == teks[::-1]:
        return "eureeka!"
    else:
        return "suka blyat"


input_strings = ["Aku Suka Kamu", "Ibu Ratna antar ubi"]

for teks in input_strings:
    hasil = cek_palindrom(teks)
    print(f"{teks}: {hasil}")
