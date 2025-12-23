a = [11, 7, 1, 13, 21, 3, 7, 3]
freq_a = {}

for item in a:
    freq_a[item] = freq_a.get(item, 0) + 1

b = [1, 3, 7]
freq_b = {}

for item in b:
    freq_b[item] = freq_b.get(item, 0) + 1

# check
is_subset = True

for key in freq_b:
    if key not in freq_a:
        is_subset = False
        break
    elif freq_a[key] < freq_b[key]:
        is_subset = False
        break

if is_subset:
    print("b is a subset of a")
else:
    print("b is not a subset of a")
