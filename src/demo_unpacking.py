snack_calories = {
    "chips": 140,
    "popcorn": 80,
    "nuts": 190,
}
items = tuple(snack_calories.items())
print(items)


def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                a[i - 1], a[i] = a[i], a[i - 1]


names = ["pretzels", "carrots", "arugula", "bacon"]
bubble_sort(names)
print(names)
