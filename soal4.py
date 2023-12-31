def cek_duplikat(data):

    set_data = set(data)
    
    return len(set_data) != len(data)


data_input = [20, 1, 3, 2, 4, 6, 8, 5, 7, 9, 11, 13, 15, 10, 12, 14, 16, 18, 20, 17, 19]
output = cek_duplikat(data_input)


print("Input:", data_input)
print("Output:", output)
