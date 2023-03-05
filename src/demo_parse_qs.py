from urllib.parse import parse_qs

my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)

print(repr(my_values))

for item in ["red", "green", "opacity"]:
    value = my_values.get(item, [""])[0] or 0
    print(f"{item.title():<8}: {value}")

for item in ["red", "green", "opacity"]:
    value_str = my_values.get(item, [""])
    value = int(value_str[0]) if value_str[0] else 0
    print(f"{item.title():<8}: {value}")


def get_first_int(values, key, default=0):
    found = values.get(key, [""])
    if found[0]:
        return int(found[0])
    return default


for item in ["red", "green", "opacity"]:
    print(f"{item.title():<8}: {get_first_int(my_values, item)}")
