a = 0b10111011
b = 0xC5F
print("Binary is %d, hex is %d" % (a, b))

pantry = [
    ("avocados", 1.25),
    ("bananas", 2.5),
    ("cherries", 15),
]
for i, (item, count) in enumerate(pantry):
    print("#%d: %-10s = %d" % (i + 1, item.title(), round(count)))

for i, (item, count) in enumerate(pantry):
    print(f"#{i+1}: {item.title():<10} = {round(count)}")
