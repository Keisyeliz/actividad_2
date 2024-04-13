import os
sw = True
pedidos = {}
def fnt_registrar_pedido():
    print('\n---Registro de Pedido---\n')

    nombre_cliente = input('Nombre del cliente: ')
    direccion = input('Dirección: ')
    contacto = input('Contacto: ')
    sexo = input('Sexo (M/F): ')
    descripcion_lugar = input('Descripción del lugar: ')
    nombre_producto = input('Nombre del producto: ')
    referencia = input('Referencia: ')
    cantidad = int(input('Cantidad: '))

    pedido = {
        'Nombre del cliente': nombre_cliente,
        'Dirección': direccion,
        'Contacto': contacto,
        'Sexo': sexo,
        'Descripción del lugar': descripcion_lugar,
        'Nombre del producto': nombre_producto,
        'Referencia': referencia,
        'Cantidad': cantidad
    }
    pedidos[len(pedidos) + 1] = pedido

    print('\nPedido registrado exitosamente.')
    enter = input('\nPresione <ENTER> para continuar...\n')

def fnt_ver_pedidos():
    
    print('---Pedidos Registrados---')

    if not pedidos:
        print('No hay pedidos registrados.')
        enter = input('Presione <ENTER> para continuar...')
    else:
        for num_pedido, pedido in pedidos.items():
            print(f"\nPedido {num_pedido}:")
            for k, v in pedido.items():
                print(f"{k}: {v}")

while sw ==True:
    os.system('cls')
    opcion = input('---Menú---\n1. Registrar\n2. Mostrar\n3. Salir\n-> ')
    
    if opcion == '1':
        os.system('cls')
        fnt_registrar_pedido()
    elif opcion == '2':
        os.system('cls')
        fnt_ver_pedidos()

    elif opcion == '3':
        print('¡Hasta luego!')
        sw = False
    else:
        print('Opción inválida. Intente de nuevo.')
        enter = input('\nPresione <ENTER> para continuar...\n')