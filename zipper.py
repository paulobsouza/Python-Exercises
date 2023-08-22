from itertools import zip_longest


def zipper(list_1, list_2):
    max_range = min(len(list_1), len(list_2))
    return [(list_1[i], list_2[i]) for i in range(max_range)]


x = ['a', 'b', 'c']
y = ['1', '2', '3', '4']

print(zipper(x, y))

# also

print(list(zip(x, y)))
print(list(zip_longest(x, y, fillvalue='Null value.')))
