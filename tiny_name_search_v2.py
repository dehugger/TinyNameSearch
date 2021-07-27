from names_dataset.nd_v1 import NameDatasetV1
import string, time, os, math

start_load = time.time()

names = NameDatasetV1()
alpha_range = string.ascii_lowercase

search_dict = {}
names_dict = {}
name_num = 0
for n in names.first_names:
    skip = False
    for c in n:
        if c not in alpha_range:
            skip = True
    if not skip:
        names_dict[name_num] = n
        for i in range(1,len(n)):
            try:
                search_dict[n[:i]].append(name_num)
            except KeyError:
                search_dict[n[:i]] = [name_num]
        name_num += 1

end_load = time.time()

print('Type "exit" to close.')
print(name_num, 'first names loaded in', str(end_load - start_load)[:4], 'seconds!')

while True:
    inp_str = 'Enter name prefix: '
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
        try:
            keys = search_dict[entry]
            results = []
            for k in keys:
                results.append(names_dict[k])
            results.sort()

            max_len = 0
            for r in results:
                if len(r) > max_len:
                    max_len = len(r)

            term_width = os.get_terminal_size()[0]
            num_cols = math.floor(term_width / max_len + 1) - 2
            num_row = math.ceil(len(results) / num_cols)

            result_rows = [[]]

            active_index = 0
            last_index = results.index(results[-1])
            while active_index <= last_index:
                if len(result_rows[-1]) == num_cols:
                    result_rows.append([])
                r = results[active_index]
                r_padded = r[0].upper() + r[1:]
                while len(r_padded) < max_len:
                    r_padded = r_padded + ' '
                result_rows[-1].append(r_padded)
                active_index += 1

            for row in result_rows:
                print(' '.join(row))

        except KeyError:
            print('No Matches!')