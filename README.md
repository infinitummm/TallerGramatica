# Análisis Sintáctico: Gramáticas, Árboles AST y Ambigüedad con ANTLR 4 y Python

**Asignatura:** Lenguajes de Programación y Traducción  
**Integrantes:** Dylan Torres - Juan Gomez - Javier Rosero  
**Entorno de Ejecución:** Python 3 + ANTLR 4 (`antlr4-python3-runtime`)

---

##  Introducción y Propósito del Taller

El análisis sintáctico (o *parsing*) es la segunda fase dentro de la arquitectura de un compilador. Su tarea principal es recibir la secuencia de componentes léxicos (*tokens*) producida por el analizador léxico y determinar si dicha secuencia cumple con las reglas estructurales de una **Gramática Libre de Contexto (GLC)**. Además de validar la sintaxis, el analizador construye una representación jerárquica en forma de árbol que servirá de base para las etapas posteriores de análisis semántico y generación de código.

En este taller se abordan tres problemas fundamentales del diseño sintáctico:
1. **Implementación de una gramática clásica para expresiones:** Construcción de un analizador sintáctico en Python utilizando ANTLR 4 y el patrón de diseño *Visitor*, evaluando rigurosamente las expresiones aceptadas y rechazadas según la especificación formal propuesta.
2. **Comprobación y contraste de formas de árboles (Parse Tree vs. AST):** Estudio de la transformación de un árbol de derivación concreto a un árbol de sintaxis abstracta, analizando el impacto de la precedencia de operadores, la asociatividad y el uso de paréntesis en la forma del árbol resultante.
3. **Identificación y demostración de ambigüedad gramatical:** Demostración práctica y matemática de cómo una gramática sin niveles de precedencia genera múltiples árboles para una misma entrada, produciendo resultados semánticos incompatibles.

---

##  Estructura del Proyecto

El repositorio se organiza de forma modular en tres carpetas independientes, acompañadas por herramientas de automatización para su compilación y ejecución:

```text
Quiz Sintactico/
├── Makefile                 # Makefile maestro para compilar o ejecutar todo el proyecto
├── run_all.py               # Script coordinador de pruebas en Python
├── Como Runear.txt          # Guía rápida de comandos de ejecución
├── README.md                # Documento explicativo unificado
│
├── Punto_1/                 # Punto 1: Gramática Diapositiva 11 (Python 3)
│   ├── Expr11.g4            # Gramática formal en ANTLR 4
│   ├── check_visitor.py     # Visitor para validación sintáctica
│   ├── main.py              # Programa validador y consola interactiva
│   ├── pruebas.txt          # Batería de pruebas (casos válidos e inválidos)
│   └── Makefile             # Automatización local del Punto 1
│
├── Punto_2/                 # Punto 2: Formas de AST (Diapositivas 12 a 14)
│   ├── Expr12.g4            # Gramática estratificada de expresiones
│   ├── ast_nodes.py         # Definición de clases de nodos del AST
│   ├── ast_builder.py       # Visitor que construye el AST desde el Parse Tree
│   ├── main.py              # Demostración y comparativa de formas de AST
│   └── Makefile             # Automatización local del Punto 2
│
└── Punto_3/                 # Punto 3: Demostración de Ambigüedad (Diapositivas 15 a 17)
    ├── AmbiguousExpr.g4     # Gramática ambigua (producción de suma previa)
    ├── AmbiguousExprAlt.g4  # Gramática ambigua (producción de producto previa)
    ├── main.py              # Demostración empírica de múltiples árboles
    └── Makefile             # Automatización local del Punto 3
```

---

##  Desarrollo ejercicios

### 🔹 Punto 1: Gramática de la Diapositiva 11 (Lenguaje Objetivo: Python)

#### Planteamiento Teórico
La diapositiva 11 presenta la estructura clásica de expresiones aritméticas con estratificación de no terminales:

$$E \to E + T \mid T$$
$$T \to T * F \mid F$$
$$F \to id \mid num \mid ( E )$$

Esta estructura define tres niveles jerárquicos:
- **Nivel $E$ (Expresión):** Maneja la suma. Al ser el nivel superior, tiene la menor precedencia.
- **Nivel $T$ (Término):** Maneja la multiplicación. Al estar subordinado a $E$, tiene mayor precedencia.
- **Nivel $F$ (Factor):** Maneja los elementos atómicos (identificadores, números literales o subexpresiones agrupadas entre paréntesis).

#### Implementación en ANTLR 4 (`Expr11.g4`)
```antlr
grammar Expr11;



root
    : expr EOF
    ;

// E -> E + T | T
expr
    : expr '+' term   # Add
    | term            # TermOnly
    ;

// T -> T * F | F
term
    : term '*' factor # Mul
    | factor          # FactorOnly
    ;

// F -> id | num | ( E )
factor
    : ID              # Id
    | NUM             # Num
    | '(' expr ')'    # Parens
    ;


ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
NUM     : [0-9]+ ('.' [0-9]+)? ;
WS      : [ \t\r\n]+ -> skip ;

```

#### Arquitectura en Python
- **`check_visitor.py`:** Implementa la clase `CheckVisitor` heredando de `Expr11Visitor`. Recorre recursivamente cada nodo del árbol asegurando que los operandos izquierdo y derecho existan y sean válidos.
- **`main.py`:** Configura un `SyntaxErrorCollector` que sustituye los manejadores por defecto de ANTLR para capturar anomalías léxicas y sintácticas sin interrumpir la ejecución. Si la cadena cumple la gramática, retorna **`ACEPTADA`**; en caso contrario, emite **`RECHAZADA`** detallando la causa exacta del fallo.

#### Análisis de Resultados de las Pruebas
Al ejecutar la batería de pruebas contra la gramática propuesta se observan los siguientes comportamientos:
1. **Casos Válidos Aceptados:**
   - `2 + 3 * 4` $\to$ **`ACEPTADA`**
   - `3 + 4 * 5` $\to$ **`ACEPTADA`**
   - `(2 + 3) * 4` $\to$ **`ACEPTADA`**
   - `x + y * 10` $\to$ **`ACEPTADA`**
2. **Observación sobre el Operador de Resta (`-`):**
   - En la diapositiva 11 se mencionan como ejemplos ilustrativos las expresiones `2 + 3 - 4` y `2 + 3 * (4 - 5)`. Sin embargo, la regla formal explícita propuesta en dicha diapositiva establece únicamente $E \to E + T \mid T$ (sin incluir el operador de resta).
   - En consecuencia, el analizador riguroso reporta **`RECHAZADA`** para cualquier expresión que contenga `-`, debido a que el símbolo no está contemplado en la regla de producción formal. Para que fuesen aceptadas, la regla formal requeriría extenderse a:
     $$E \to E ('+' \mid '-') T \mid T$$
3. **Casos Inválidos Rechazados:**
   - `2 + * 4` $\to$ **`RECHAZADA`** *(operador binario consecutivo sin operando intermedio).*
   - `(2 + 3` $\to$ **`RECHAZADA`** *(falta de paréntesis de cierre).*
   - `2 3` $\to$ **`RECHAZADA`** *(yuxtaposición de literales sin operador).*

---

### 🔹 Punto 2: Comprobación de las Formas de AST (Diapositivas 12 a 14)

#### Planteamiento Teórico
Existe una distinción fundamental entre el árbol sintáctico que genera el analizador y el árbol que utiliza el compilador:
- **Parse Tree (Árbol Sintáctico Concreto - Diapositiva 12):** Refleja de forma exhaustiva cada paso de la derivación formal. Incluye todos los símbolos no terminales ($E, T, F$) y los terminales de puntuación (paréntesis). Resulta indispensable durante el parsing, pero introduce un costo significativo de memoria y complejidad.
- **AST (Árbol de Sintaxis Abstracta - Diapositiva 13):** Es una representación sintética y compacta que descarta el ruido sintáctico. Los operadores se posicionan como nodos internos y los operandos como hojas.

#### Comprobación Práctica de Formas de Árbol

Se implementó un constructor de AST en Python (`ast_builder.py`) que transforma el Parse Tree de ANTLR en objetos `ASTNode` (`BinaryOpNode`, `NumNode`, `IdNode`). Al analizar las expresiones se comprueban los siguientes fenómenos:

1. **Caso A: Precedencia Natural (`3 + 4 * 5`)**
   - Al no existir paréntesis, la estructura de la gramática impone que `4 * 5` se reduzca primero dentro del no terminal $T$.
   - **Forma del AST:**
     ```text
     └── OpBinario ('+')
         ├── Num (3)
         └── OpBinario ('*')
             ├── Num (4)
             └── Num (5)
     ```
   - **Notación S-Expression:** `(+ 3 (* 4 5))`
   - **Evaluación:** $3 + (4 \times 5) = 23.0$.
   - **Demostración de Unicidad:** Para esta cadena, la gramática produce **exactamente un único AST**. Es imposible que el operador `*` quede en la raíz sin paréntesis, lo que confirma que la gramática de la diapositiva 12 no es ambigua.

2. **Caso B: Precedencia Forzada por Paréntesis (`(3 + 4) * 5`)**
   - Los paréntesis actúan como modificadores de jerarquía: fuerzan a que la suma se resuelva dentro del factor $F$, subordinando el operador `+` bajo el operador `*`.
   - Cabe destacar que los caracteres `(` y `)` **no se incorporan como nodos en el AST**, pues su función ordenadora queda reflejada directamente en la topología del árbol.
   - **Forma del AST:**
     ```text
     └── OpBinario ('*')
         ├── OpBinario ('+')
         │   ├── Num (3)
         │   └── Num (4)
         └── Num (5)
     ```
   - **Notación S-Expression:** `(* (+ 3 4) 5)`
   - **Evaluación:** $(3 + 4) \times 5 = 35.0$.

3. **Caso C: Asociatividad a la Izquierda (`3 + 4 + 5`)**
   - Al coincidir operadores de igual nivel, la recursión izquierda de la regla $E \to E + T$ obliga al analizador a agrupar primero los operandos situados a la izquierda.
   - **Forma del AST:** `(+ (+ 3 4) 5)` $\to$ El subárbol izquierdo contiene la primera suma `3 + 4` y el resultado se suma con `5`.

#### Eficiencia Comparativa (Parse Tree vs. AST)
Para la expresión `3 + 4 * 5`:
- **Nodos en el Parse Tree Concreto:** 15 nodos.
- **Nodos en el AST:** 5 nodos.
- **Optimización:** Reducción del **66.7%** en la cantidad de nodos en memoria, demostrando por qué las fases posteriores del compilador (análisis semántico y generación de código) operan exclusivamente sobre el AST.

---

### 🔹 Punto 3: Implementación y Demostración de Ambigüedad (Diapositivas 15 a 17)

#### Planteamiento Teórico
Una gramática libre de contexto se define formalmente como **ambigua** si existe al menos una cadena de su lenguaje que admita **dos o más árboles de derivación sintáctica distintos** (o equivalentemente, dos derivaciones por la izquierda diferentes).

La diapositiva 15 propone la siguiente gramática elemental:
$$E \to E + E$$
$$E \to E * E$$
$$E \to num$$

#### Demostración Práctica de Ambigüedad
Al procesar la cadena **`2 + 3 * 4`**, se comprueba que la gramática permite construir dos derivaciones válidas con interpretaciones semánticas completamente divergentes:

```text
       Árbol 1: (2 + 3) * 4                       Árbol 2: 2 + (3 * 4)
             *                                          +
            / \                                        / \
           +   4                                      2   *
          / \                                            / \
         2   3                                          3   4
      Resultado: 20.0                            Resultado: 14.0
```

1. **Interpretación 1 (Suma con mayor precedencia):**
   - **Derivación por la izquierda:**  
     $$E \Rightarrow E * E \Rightarrow (E + E) * E \Rightarrow (2 + 3) * 4$$
   - **Representación:** `(* (+ 2 3) 4)`
   - **Valor numérico:** **`20.0`**
2. **Interpretación 2 (Multiplicación con mayor precedencia):**
   - **Derivación por la izquierda:**  
     $$E \Rightarrow E + E \Rightarrow 2 + (E * E) \Rightarrow 2 + (3 * 4)$$
   - **Representación:** `(+ 2 (* 3 4))`
   - **Valor numérico:** **`14.0`**

#### Consecuencias en el Compilador
Dado que una computadora no puede asumir de manera determinista cuál de los dos significados pretendía el programador, una gramática ambigua es inaceptable para la construcción de lenguajes de programación. Para eliminar la ambigüedad, es obligatorio:
1. **Estratificar la gramática en niveles** (como se demostró en el Punto 1 y Punto 2), o
2. **Declarar directivas explícitas de precedencia y asociatividad** que le indiquen al generador del parser cómo resolver los empates.

---

## 4. Guía de Compilación y Ejecución

El proyecto cuenta con `Makefiles` tanto en la raíz como en cada una de las subcarpetas, permitiendo una experiencia de uso simple e intuitiva.

###  Como ejecutar
Desde la carpeta raíz `Quiz Sintactico`:

```bash
# Opción 1: Mediante el Makefile maestro
make run

# Opción 2: Ejecutando directamente el script de orquestación
python3 run_all.py
```

---

###  Limpieza de Archivos Generados
Para eliminar todos los archivos autogenerados por ANTLR (`*.tokens`, `*.interp`, archivos `.py` derivados) y cachés `__pycache__`:

```bash
# Desde la raíz (limpia los tres puntos):
make clean

# O dentro de cada subcarpeta:
cd Punto_1 && make clean
cd ../Punto_2 && make clean
cd ../Punto_3 && make clean
```

---

##  Conclusiones Generales del Laboratorio

1. **La gramática determina la corrección del analizador:** Una especificación rigurosa en ANTLR 4 debe considerar cada operador individualmente. La omisión del operador de resta en la regla formal de la diapositiva 11 demuestra que el parser solo aceptará exactamente lo que se encuentre codificado en la gramática.
2. **El AST es la estructura óptima para fases posteriores:** La comparación cuantitativa demostró que el AST preserva intacta la semántica de la expresión eliminando más del 65% de los nodos prescindibles del Parse Tree, simplificando la evaluación y optimización.
3. **La ambigüedad debe ser erradicada en el diseño:** Gramáticas recursivas como $E \to E + E \mid E * E$ no pueden diferenciar la precedencia entre suma y producto por sí solas. La solución formal consiste en estructurar la gramática en capas sucesivas de precedencia ($E \to T \to F$).
