# **Metodo MAP y Metodo FILTER**
**Requisitos:** Para ejecutar este proyecto se debe tener instalado Antlr v4.13 y Python3.

1. Clonar el repositorio 'enlace del github'

2. Desde la consola acceder a la ruta donde se clono el proyecto

3. Compilar el proyecto con el comando antlr4 -visitor -Dlanguage=Python3 nombredelarchivo.g4

4. Ejecutar el Test.py con el comando python3 Test.py o python3 Test.py archivo.txt si se quiere leer un archivo de texto externo


## **Pruebas**
Para hacer unas pruebas verificando el funcionamiento de la funcion Map y la funcion Filter se necesita compilar el archivo.g4 y su python con su respectivo .txt, dentro del txt se encontrara:

```
map(lambda x: x.upper(), ["a", "b", "c", "d"])
map(lambda x: x.upper(), ["perro", "foca", "leon", "sapo"])
map(lambda y: y+9, [2, 3, 4, 5])
filter(lambda hola: hola % 2 == 0 and hola > 2, [4, 5, 2, 17])
map(lambda x: x * 2, [1, 2, 3, 4])
filter(lambda x: x % 3 == 0, [9, 12, 15, 18])
map(lambda x: x ** 2, [1, 2, 3, 4])
filter(lambda x: len(x) > 5, ["apple", "banana", "orange", "grape", oil])
map(lambda x: x.capitalize(), ["hello", "world", "how", "are", "you"])
map(lambda x: len(x), ["cat", "dog", "elephant", "giraffe"])
map(lambda x: x[0], ["apple", "banana", "cherry", "date"])
filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5])
```

y como resultado se obtendra:

```
['"A"', '"B"', '"C"', '"D"']
['"PERRO"', '"FOCA"', '"LEON"', '"SAPO"']
[11, 12, 13, 14]
[4]
[2, 4, 6, 8]
[9, 12, 15, 18]
[1, 4, 9, 16]
['"apple"', '"banana"', '"orange"', '"grape"']
['"hello"', '"world"', '"how"', '"are"', '"you"']
