# Elementos básicos de python

## Literales

Literales de entero, flotante, cadena, booleano

## Operadores

- Suma + 
- Resta -
/ * % ** = ==

### Ejemplos:

```[python]
1 + 2
5 / 'hola'
5 * 'hola'

# Para imprimir información en la consola
print('Hola mundo')
```
## Objetos, expresiones y tipos númericos

Lo objetos son valores en memoria y son de diferentes tipos (Enteros, coordenadas, persona, estudiante), son escalares y no escalares.

```[python]
my_int = 1

type(my_int)
```
## Asignación de variables

## Cadenas y estradas

Las cadenas son inmutables, en realidad se reasignan

```[python]
my_str = 'hola'

len(my_str)
print(my_str[0])
print(my_str[1:3]


name = input('Cual es tu nombre?)
num = int(input('Escribe un número'))
```

## Programas ramificados

```[python]
num_1 = int(input('Escribe un numero entero:')
num_2 = int(input('Escribe un numero entero:')

if num_1 > num_2:
  print('El primer numero es mayor')
elif num_1 < num_2:
  print('El segundo numero es mayor')
else:
  print('Los dos numeros son iguales')
```

## Iteraciones

```python
count = 0

while count < 10:
  print(count)
  count += 1
```

## funciones

```python
def suma(a, b):
    """ Suma dos valores a y b.

    param int a culaquier entero
    param int b cualquier entero
    return la sumatoria de a y b
    """

    total = a + b
    return total
```

## funciones como objetos

Argumentos de otras funciones

```python
def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
```

```terminal
>>> nums = [1, 2, 3]
>>> aplicar_operacion(multiplicar_por_dos, nums)
[2, 4, 6]

>>> aplicar_operacion(sumar_dos, nums)
[3, 4, 5]


Funciones en expresiones

```python
sumar = lambda x, y: x + y
```


```terminal
>>> sumar(2, 3)
5
```

Funciones en estructuras de datos

```python
def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado
```

## Listas

```python
my_list = list(range(100))
double = [i * for i in my_list]
pares = [i for i in my_list if i% 2 == 0]
```
