# Transformada de Laplace con ANTLR4 y Python

Este proyecto forma parte del segundo parcial de la asignatura de Lenguajes de Programación. El objetivo es diseñar e implementar una gramática en ANTLR para calcular la transformada de Laplace utilizando Python como lenguaje objetivo.

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

bash

    antlr4 -Dlanguage=Python3 LaplaceTransform.g4 -visitor

    Esto generará los archivos necesarios (LaplaceTransformLexer.py, LaplaceTransformParser.py, LaplaceTransformVisitor.py).

Uso

Para ejecutar el programa, utiliza el archivo main.py. Este archivo lee una expresión por consola y calcula su transformada de Laplace.

bash

python main.py

El programa solicitará que ingreses una expresión para calcular su transformada de Laplace. Por ejemplo:

css

Ingrese una expresión para calcular su transformada de Laplace: L{t^2 + 3*t + 1}

La salida será:

bash

Transformada de Laplace: 2/s^3 + 3/s^2 + 1/s

Ejemplo
Entrada

scss

L{sin(t) + 2*t + t^3}

Pasos para calcular la transformada de Laplace

    Transformada de Laplace de sin⁡(t)sin(t):
    L{sin⁡(t)}=1s2+1
    L{sin(t)}=s2+11​

    Transformada de Laplace de 2t2t:
    L{2t}=2s2
    L{2t}=s22​

    Transformada de Laplace de t3t3:
    L{t3}=6s4
    L{t3}=s46​

    Suma de las transformadas:
    L{sin⁡(t)+2t+t3}=1s2+1+2s2+6s4
    L{sin(t)+2t+t3}=s2+11​+s22​+s46​

Salida esperada

bash

Transformada de Laplace: 1/(s^2 + 1) + 2/s^2 + 6/s^4

Estructura del Proyecto

    LaplaceTransform.g4: Archivo de gramática de ANTLR4 para el lenguaje de transformada de Laplace.
    LaplaceTransformVisitorImpl.py: Implementación del visitor para calcular la transformada de Laplace.
    main.py: Archivo principal que lee la entrada del usuario y calcula la transformada de Laplace.
    README.md: Archivo de documentación (este archivo).

Funciones Soportadas

    Operaciones aritméticas básicas: suma, resta, multiplicación, división y potencias.
    Funciones trigonométricas: sin, tan.
    Expresiones polinómicas en t.

Limitaciones

    No soporta funciones complejas o compuestas no incluidas en la gramática.
    Las transformadas de funciones no estándar (como cos⁡(t2)cos(t2)) no se calculan de forma cerrada.

Consideraciones para la Gramática

La gramática debe definir tanto la parte léxica como sintáctica para manejar correctamente los operadores, funciones y transformadas. La implementación se realiza en Python utilizando el visitor generado por ANTLR4.

go


Este contenido puede ser utilizado directamente en un archivo `README.md` para documentar el proyecto de forma clara y estructurada en GitHub.


