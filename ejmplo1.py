'''Una transportadora requiere el desarrollo de una app que permita llevar un registro de los despachos de sus vehiculos teniendo en cuenta lo siguiente:

-Placa del vehiculo
-descripción del vehiculo
-nombre del conductor
-contacto
-ruta
-descripcion de la carga

el número de despacho se genera de forma automatica. Dicha informacion debe uedar reguisrada en un diccionario.
el sistema debe realizar:
-registro de salida y mostrar salida'''


import os
sw = True

diccionario_registros = {}
n_despacho = 0
def fnt_num_despacho():
    global n_despacho
    n_despacho += 1
    return n_despacho

def fnt_registrar(placa, descripcionv, nombre, contacto,ruta,descripcionc):
    if placa == '' or descripcionv == '' or nombre == '' or contacto == '' or ruta == '' or descripcionc == '':
        enter = input('\nDebe ingresar todos los datos <ENTER>')
    else:
        enter = input(f'\nRegistro del vehiculo {placa} realizado con éxito')
         
def fnt_selector(op):
    if op == '1':
        placa = input('Ingrese el número de la placa: ')
        descripcionv = input('Ingrese la descripción del vehiculo: ')
        nombre = input('Ingrese el nombre del conductor: ')
        contacto = input('Ingrese el número de contacto: ')
        ruta = input('Ingrese la ruta a recorrer: ')
        descripcionc = input('Ingrese la descripción de la carga: ')
    fnt_registrar(placa, descripcionv, nombre, contacto,ruta,descripcionc)


while sw == True:
    os.system('cls')
    opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    if opcion == "1":
        fnt_selector(opcion)
    elif opcion == '2':
        print('\nCantidad de registros: ',len(diccionario_registros),'\n') 
        enter = input('\nPresione <ENTER> para continuar')  
   




















