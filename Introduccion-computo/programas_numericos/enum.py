# Ejemplo para mostrar como se puede solucionar un problema a traves de la busqueda exhaustiva o fuerza bruta

objetivo = int(input('Escoge un numero entero:'))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta +=1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tienen raíz exacta')

# test: 25, 27, 16, 108638929, 
