from names_dataset.nd_v1 import NameDatasetV1
import string

names = NameDatasetV1()
alpha_range = string.ascii_lowercase
sorted_names = {}
for x in alpha_range:
    sorted_names[x] = {}
    for y in alpha_range:
        sorted_names[x][y] = {}
        for z in alpha_range:
            sorted_names[x][y][z] = []

name_count = 0

for name in names.first_names:
    skip = False
    for c in name:
        if c not in alpha_range:
            skip = True
    if len(name) < 3:
        skip = True
    if not skip:
        sorted_names[name[0]][name[1]][name[2]].append(name)
        name_count+=1

for x in alpha_range:
    for y in alpha_range:
        for z in alpha_range:
            sorted_names[x][y][z].sort()

print('Type "exit" to close.')
print(name_count, 'first names loaded!')

while True:
    inp_str = 'Enter three characters: '
    entry = input(inp_str)
    if entry == 'exit':
        exit()
    while len(entry) != 3:
        inp_str = 'Enter *exactly* three characters: '
        entry = input(inp_str)
        entry = entry.lower()
        if entry == 'exit':
            exit()
            
    invalid = False
    for c in entry:
        if c not in alpha_range:
            invalid = True

    if invalid:       
        print('Only alpha characters are allowed.')

    if not invalid:

        results = sorted_names[entry[0]][entry[1]][entry[2]]

        max_len = 0
        for r in results:
            if len(r) > max_len:
                max_len = len(r)

        results_sorted = [[]]
        for r in results:
            if len(results_sorted[-1]) >= 4:
                results_sorted.append([])
            r_padded = r[0].upper() + r[1:]
            while len(r_padded) < max_len:
                r_padded = r_padded + ' '
            results_sorted[-1].append(r_padded)

        for rs in results_sorted:
            print(' '.join(rs))