import itertools

names = ["Cecilia", "Lisa", "Marie"]
counts = [len(name) for name in names]
print(counts)

longest_name = None
max_count = 0

# for i in range(len(names)):
#     count = counts[i]
#     if count > max_count:
#         longest_name = names[i]
#         max_count = count

# for i, name in enumerate(names):
#     count = counts[i]
#     if count > max_count:
#         longest_name = name
#         max_count = count

names.append("James")

for name, count in itertools.zip_longest(names, counts, fillvalue=12):
    if count > max_count:
        max_count = count
        longest_name = name
    print(f"{name}: {count}")

print(longest_name)
