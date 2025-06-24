from math import sqrt


def zipper(list_1, list_2):
    max_range = min(len(list_1), len(list_2))
    return [(list_1[i], list_2[i]) for i in range(max_range)]


def distance_zero(x, y):
    distances = []
    max_range = len(x)
    for i in range(max_range):
        distance = sqrt(x[i] ** 2 + y[i] ** 2)
        distances.append(distance)
    return distances


x = []
y = []

values = int(input('Quantos pontos você quer? '))

for i in range(values):
    values_x = float(input(f'X{i} de X: '))
    x.append(values_x)
    values_y = float(input(f'Y{i} de Y: '))
    print()
    y.append(values_y)

zipped_coordinates = zipper(x, y)
distances = distance_zero(x, y)

print("Coordenadas:", zipped_coordinates,'\n')
print("Distâncias ao Ponto Zero:", distances,'\n')
print("A menor distância até a constante 0.0 foi de", min(distances))

