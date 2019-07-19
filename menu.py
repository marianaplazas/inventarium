#!/usr/bin/python3
import os

tornillos = {}
herramientas = {}
materiales = {}

#def agregar():
    #return 'Seleccionó la opción 1.1'

#def retirar(self, args):
        

    #return 'Seleccionó la opción 1.2'

#def opcion_2():
   # return 'Seleccionó la opción 2.1'

#def opcion_3():
   # return 'Seleccionó la opción 2.2'

def opcion_salida():
    return 'Seleccionó salir\n¿Está seguro que desea salir? Y/N'

def opcion_error():
    print ('Seleccionó una opción no válida')

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
       os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")

while(True):
    print("1 para reportar compra")
    print("2 para reportar venta")    
    print("3 para mostrar inventario")
    print("4 para salir")
    print('Seleccione la opción: ')
    opc = input()
    borrarPantalla()
    if opc == '1':
        print("para agregar la compra escriba agregar") 
        # aquí va el codigo para reportar la compra
        # ejecutar la función agregar compra
        opc1 = input()
#        if opc1 == 'a':
 #           print(opcion1_1())
  #      elif opc1 == 'b':
  #          print(opcion1_2())
         #else:
          #  print(opcion_error())
        print('Oprima cualquier tecla para continuar...')
        input()
    elif opc == '2':
        print("Escriba vendido")
        opc2 = input()
     #else:
            #mensaje de error
      #      print(opcion_error())
        print('Oprima cualquier tecla para continuar...')
        input()
    elif opc == '3':
        print("instrucción ineccesaria")
        #codigo de show este es el unico que con solo darle debe mostrar 
    elif opc == '4':
        print("opción 4")
        print(opcion_salida())
        salir = input()
        if(salir == 'Y' or salir == 'y'):
            break;
    else:
        print(opcion_error())
    borrarPantalla()
    print()
