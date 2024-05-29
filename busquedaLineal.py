'''Consiste en ir recorriendo todos los elementos de la lista, uno a uno, hasta encontrar aquel que estamos buscando, en este caso, estamos buscando el menor de la lista'''

def busca_menor(lista):
    """Busca el elemento menor de una lista"""

    # El elemento menor será el primero, para empezar
    menor = 0

    for i in range(len(lista)):
        if lista[i] < lista[menor]:
            menor = i

    return menor


lista = [
    75, 13, 92, 99, 19, 33, 40, 42, 85, 17,
    44, 63,  8, 87, 72, 51, 46, 87, 35, 53
    ]

menor = busca_menor(lista)

print(f'El menor elemento está en la posición {menor}')
print(f'Su valor es {lista[menor]}')

