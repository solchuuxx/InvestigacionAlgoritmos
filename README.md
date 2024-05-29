
### Investigación de Algoritmos de Búsqueda: Búsqueda Lineal y Búsqueda Binaria

## Búsqueda Lineal

La búsqueda lineal, como su nombre lo indica, es un método de búsqueda en el que examinamos cada elemento de una lista o conjunto de datos uno por uno, en orden secuencial. Comenzamos desde el principio y avanzamos hasta encontrar el elemento que estamos buscando o hasta que hayamos recorrido toda la lista.

#### ¿Cuándo Utilizar la Búsqueda Lineal?

La búsqueda lineal es útil en situaciones donde no tenemos información previa sobre la ubicación del elemento que buscamos. Es eficaz en listas pequeñas o cuando el elemento que buscamos está cerca del principio de la lista. También es una opción adecuada cuando necesitamos encontrar todos los elementos que coinciden con ciertos criterios y no solo el primero.

### Ejemplo sencillo:

```python
def busqueda_lineal(lista, objetivo):
    for indice, valor in enumerate(lista):
        if valor == objetivo:
            return indice
    return -1

lista = [10, 23, 45, 70, 11, 15]
objetivo = 70

resultado = busqueda_lineal(lista, objetivo)
print("Resultado de la búsqueda lineal:", resultado)

```


## Búsqueda Binaria 

La búsqueda binaria, por otro lado, es un enfoque más eficiente para buscar elementos en una lista ordenada. En lugar de examinar los elementos uno por uno en orden secuencial, la búsqueda binaria divide repetidamente la lista en dos mitades y elimina una mitad en función de la comparación con el elemento buscado. Este proceso continúa hasta que se encuentra el elemento o se determina que no existe en la lista.

#### ¿Cuándo Utilizar la Búsqueda Binaria?

La búsqueda binaria es especialmente eficiente cuando se trabaja con listas grandes o conjuntos de datos ordenados. Siempre que la lista esté ordenada y tengamos información sobre esta ordenación, la búsqueda binaria puede ser la elección más rápida y efectiva.

### Ejemplo sencillo: 

```python
def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1

lista_ordenada = [1, 3, 5, 7, 9, 11]
objetivo = 9

resultado = busqueda_binaria(lista_ordenada, objetivo)
print("Resultado de la búsqueda binaria:", resultado)

```

## Eficiencia para ambos casos

Una de las diferencias más notables entre la búsqueda lineal y la búsqueda binaria es su eficiencia. La búsqueda lineal tiene una complejidad de tiempo lineal, lo que significa que su tiempo de ejecución aumenta linealmente con el tamaño de la lista. Por otro lado, la búsqueda binaria tiene una complejidad de tiempo logarítmica, lo que la hace mucho más rápida en listas grandes.





