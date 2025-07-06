# Tienes dos listas: lista1 = [1, 5, 3, 7, 2] y lista2 = [5, 8, 2, 9, 1].
    # Crea una nueva lista llamada lista_unica que contenga todos los elementos de lista1 y lista2 sin elementos duplicados, 
    # y conservando el orden de aparición original de los elementos. Por ejemplo, 
    # si un elemento aparece primero en lista1 y luego en lista2, debe mantener su posición relativa de la primera aparición.
    # Imprime lista_unica. (Pista: Puedes usar un bucle y una condición if 
    # para verificar si un elemento ya está en la nueva lista antes de añadirlo).
    # Lista unica = 1,5,3,7,2,8,9
'''   


#for j in lista2:
    
 #   if j not in lista_unica:
 #       lista_unica.append(j)
#print(lista_unica)

def suma(num1, num2):
    resultado = num1 + num2
    print (resultado)
    

num1 = int(input('ingresar numero : > '))
num2 = int(input('ingresar numero : > '))

suma(num1, num2)


numero1 = int(input('Ingrese un numero: > '))
numero2 = int(input('Ingrese un numero: > '))
suma(f'numero1, numero2')
'''
lista1 = [1,5,3,7,2]
lista2 = [5,8,2,9,1]
lista_unica = []

lista1.extend(lista2)

for i in lista1:
    
    if i not in lista_unica:
        lista_unica.append(i)
        
print(lista_unica)