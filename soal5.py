import itertools

name = "naiplovyu"
max_length = 6

combinations = []
for i in range(1, max_length + 1):
    combinations += list(itertools.combinations(name, i))

print(f"Jumlah kombinasi username yang mungkin adalah {len(combinations)}.")