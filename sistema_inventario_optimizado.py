inventario = {} #nuestro inventario donde almacenaremos todos los productos

def nuevo_producto():
    existente =False #una variable para controlar el ciclo, para que el usuario ingrese los valores correctos
    global nombre, precio, cantidad
    while not existente:
        nombre=(input('Ingrese el nombre del Producto nuevo:  > '))
        if nombre in inventario:
            print('El Producto ya existe dentro del inventario')
            existente=False
        else:
            existente=True
        
#aqui hacemos algo similar pero para los datos numericos
    intento = False
    while not intento: 
        try:
            precio=float(input('Ingrese precio:  >'))
            cantidad=int(input('Ingrese cantidad:  >'))
            intento = True
        except:
            print('Intenta ingresar de nuevo un valor numérico para el precio y la cantidad')
        
    inventario[nombre] = (precio, cantidad)
    return nombre, precio, cantidad

def consultar_productos():
    #funcion para buscar en el inventario si el producto esta o no

    nombre=input('¿Que Producto desea buscar?  > ')
    if nombre in inventario:
        print(inventario.get(nombre))
    else:
        print('el producto no esta en el inventario')
        #retornamos un mensaje para notificar al usuario
        #lo enviará de nuevo al menú principal

def actualizar_precios():
    nombre=input('Ingrese el nombre del producto a actualizar:  > ')
    try:
        if nombre in inventario:
            inventario.pop(nombre)
            
            precio=int(input('Ingrese Precio:  > '))
            cantidad=int(input('ingrese cantidad:  > '))
            inventario[nombre] = (precio, cantidad)
        elif nombre not in inventario:
            print('El producto no esta en el inventario')
    except:
        print('producto no identificado')
        #lo enviamos de vuelta al menú principal
    
def eliminar_productos():
    nombre=input('Ingrese nombre de Producto a eliminar:  >  ')
    if nombre in inventario:
        inventario.pop(nombre)
        print('EL PRODUCTO FUE REMOVIDO EXITOSAMENTE')
    else:
        print('Producto no identificado')

def calcular_productos():
    
    valor_total = lambda inventario: sum(precio * cantidad for precio, cantidad in inventario.values())
    print(f'El valor del inventario es ${valor_total(inventario)} Pesos ')

opciones=False
while not opciones:
    print('Menu de inventario')
    print('1.- Añadir nuevos productos')
    print('2.- Consultar productos')
    print('3.- Actualiza precios ')
    print('4.- Eliminar productos ')
    print('5.- Calcular el valor total del inventario')
    print('6.- Salir')

    menu=input('\n¿Que desea realizar? > ')

    if menu == "1":
        nuevo_producto()
        
    elif menu == "2":
        consultar_productos()

    elif menu == "3":
        actualizar_precios()
        
    elif menu == "4":
        eliminar_productos()
        
    elif menu == "5":
        calcular_productos()
        
    elif menu == "6":
        break
    else:
        print('\nIntente ingresar una opcion entre 1 y 4.\n')

print('¡Gracias por usar el programa!')