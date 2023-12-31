from collections import Counter

def find_naughty_children(names):
    counts = Counter(names)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    if all(value == 1 for value in counts.values()):
        return "Semuanya anak baik"
    
    naughty_children = [name for name, count in sorted_counts if count > 1]
    
    if len(naughty_children) == 1:
        return f"{naughty_children[0]} Nakal"
    else:
        return f"{' dan '.join(naughty_children)} Nakal"


inputs = [
    ["Bagas", "Dimas", "Bagas", "Bagas", "Indra", "Gilang", "Gilang", "Hana", "Fajar", "Fajar"],
    ["Bagas", "Dimas", "Fajar", "Bagas","Indra","Gilang","Gilang","Bagas","Fajar","Fajar"],
    ["Aisyah","Bagas","Dewi","Dimas","Eka","Fajar","Gilang",
    	"Hana","Indra",
    	"Jihan"]
]

for names in inputs:
    print(find_naughty_children(names))
