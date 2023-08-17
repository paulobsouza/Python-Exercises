import copy

from products_pkg import products

new_products = [
    {**product, 'price': round(product['price'] * 1.10, 2)}
    for product in copy.deepcopy(products)
]

sorted_products_by_name = sorted(
    copy.deepcopy(products),
    key=lambda product: product['name']
)

sorted_products_by_price = sorted(
    copy.deepcopy(products),
    key=lambda product: product['price']
)

print('PRODUTOS')
print()
print(*products, sep='\n')
print()
print('PRODUTOS COM AUMENTO DE 10%')
print()
print(*new_products, sep='\n')
print()
print('PRODUTOS ORDENADOS POR NOME')
print()
print(*sorted_products_by_name, sep='\n')
print()
print('PRODUTOS ORDENADOS POR PREÇO')
print()
print(*sorted_products_by_price, sep='\n')
