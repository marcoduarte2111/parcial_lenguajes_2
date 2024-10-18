# Transformada de Laplace con ANTLR4 y Python

Diseñar e implementar una gramática en ANTLR para calcular la transformada de Laplace utilizando Python como lenguaje objetivo.

## Descripción del Proyecto

El proyecto consiste en diseñar una gramática para un lenguaje de programación que permita calcular la transformada de Laplace de funciones algebraicas. La gramática debe ser capaz de reconocer expresiones en función de `t` y aplicar las transformadas correspondientes para obtener la función en términos de `s`.

## Requisitos

- Python 3.x
- ANTLR4
- SymPy (para el cálculo simbólico)

## Instalación

1. **Instalar SymPy**:

   ```bash
   pip install sympy

Generar los archivos de ANTLR:

Ejecuta el siguiente comando para generar el lexer, parser y visitor en Python:

```bash

    antlr4 -Dlanguage=Python3 LaplaceTransform.g4 -visitor

```

Esto generará los archivos necesarios (LaplaceTransformLexer.py, LaplaceTransformParser.py, LaplaceTransformVisitor.py).

**Uso**

Para ejecutar el programa, utiliza el archivo main.py. Este archivo lee una expresión por consola y calcula su transformada de Laplace.

```bash

python main.py
```
El programa solicitará que ingreses una expresión para calcular su transformada de Laplace. Por ejemplo:

```css

Ingrese una expresión para calcular su transformada de Laplace: L{t^2 + 3*t + 1}
```
La salida será:

```bash

Transformada de Laplace: 2/s^3 + 3/s^2 + 1/s
```
