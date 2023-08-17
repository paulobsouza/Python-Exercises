from itertools import zip_longest


def zipper(list_1, list_2):
    max_range = min(len(list_1), len(list_2))
    return [(list_1[i], list_2[i]) for i in range(max_range)]


cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA', 'SP', 'MG', 'RJ']

print(zipper(cities, states))

# also

print(list(zip(cities, states)))
print(list(zip_longest(cities, states, fillvalue='No city')))
