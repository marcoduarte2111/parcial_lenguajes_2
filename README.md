# Resolución de Ejercicios - Segundo Parcial de Lenguajes de Programación

Este proyecto contiene la implementación en ANTLR4 de tres ejercicios del segundo parcial de la materia Lenguajes de Programación. El objetivo es diseñar gramáticas específicas y generar código en Python para resolver cada ejercicio.

## Contenido

1. [Ejercicio 1: Operaciones con Números Racionales](https://github.com/marcoduarte2111/parcial_lenguajes_2/tree/main/Gramatica_Map_Filter)
2. [Ejercicio 2: Operaciones con Iterables (Map y Filter)](https://github.com/marcoduarte2111/parcial_lenguajes_2/tree/main/Numeros_Racionales)
3. [Ejercicio 3: Transformada de Laplace](#ejercicio-3-transformada-de-laplace)

## Ejercicio 1: Operaciones con Números Racionales

En este ejercicio, se diseña una gramática para un lenguaje de programación capaz de realizar operaciones con números racionales. La gramática soporta la suma, resta, multiplicación y división de fracciones en formato `a/b`, donde `a` y `b` son números enteros.

### Ejemplo de Uso
- Entrada: `(1/3 + 2/3)`
- Salida: `1.0`

### Implementación
La gramática fue implementada en ANTLR4 con Python como lenguaje objetivo. La parte léxica y sintáctica de la gramática permite reconocer fracciones y operadores aritméticos básicos.

## Ejercicio 2: Operaciones con Iterables (Map y Filter)

Este ejercicio consiste en diseñar una gramática que permita aplicar funciones a los elementos de objetos iterables, tales como listas o tuplas. Además, se puede filtrar los elementos de un iterable basándose en una condición.

### Ejemplo de Uso
- `MAP(function, iterable)` para aplicar una función a cada elemento.
- `FILTER(condition, iterable)` para filtrar elementos según una condición.

### Implementación
Se implementó una gramática en ANTLR4 que define la sintaxis para las funciones `MAP` y `FILTER`, y se utilizó Python para generar el código. La gramática reconoce funciones aplicables a elementos de colecciones y permite definir las condiciones para la función de filtro.

## Ejercicio 3: Transformada de Laplace

Para este ejercicio, se diseñó una gramática que permite calcular la transformada de Laplace de expresiones algebraicas en función de `t`. Se incluye una tabla de pares transformados y se realizan las consideraciones necesarias para la definición de la parte léxica y sintáctica.

### Ejemplo de Uso
- Entrada: Una expresión algebraica en `t`.
- Salida: La transformada de Laplace correspondiente.

### Implementación
La gramática fue creada para reconocer expresiones algebraicas y aplicar las reglas necesarias para calcular la transformada de Laplace. El lenguaje objetivo es Python, y se usaron las capacidades de ANTLR4 para generar el código correspondiente.

## Requisitos

- [ANTLR4](https://www.antlr.org/)
- Python 3.x
- Java (para ejecutar ANTLR)

## Ejecución

1. Generar los archivos de Python a partir de la gramática:
   ```bash
   antlr4 -Dlanguage=Python3 NombreDeLaGramatica.g4
