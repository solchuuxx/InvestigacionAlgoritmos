'''Este algoritmo tendrá dos índices, inicio y final. Uno apunta al comienzo de la lista y otro al final de la lista. Estos índices se actualizarán a medida que conozcamos qué parte de la lista puede contener al elemento buscado'''

def busqueda_binaria(lista, buscado):
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio] == buscado:
            return medio
        elif lista[medio] < buscado:
            inicio = medio + 1
        else:
            final = medio - 1

    return None


lista = [
    8, 13, 17, 19, 33, 35, 40, 42, 44, 46,
    51, 53, 63, 72, 75, 85, 87, 89, 92, 99
    ]
buscado = 8

resultado = busqueda_binaria(lista, buscado)

if resultado == None:
    print(f'El elemento {buscado} no se encuentra en la lista')
else:
    print(f'El elemento {buscado} se encuentra en la posición {resultado}')