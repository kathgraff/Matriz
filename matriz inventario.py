#Nombre de estudiante: Angie Catherine Muñoz Basante 
#programa: ingenieria en sistemas
#curso: fundamentos de programacion
#grupo: 213022_557

INVENTARIO = [
    ["001", "busos", 5, 10],
    ["002", "corsets", 4, 6],
    ["003", "faldas", 3, 8],
    ["004", "pantalones cargo", 1, 4],
    ["005", "chaquetas", 2, 5]
]

def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        cantidad = 0

        return cantidad
    
while True:
    
 print("==================================")
 print("LISTADO DE PEDIDOS DE INVENTARIO")
 print("==================================")

 for articulo in INVENTARIO:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]


    cantidad_de_pedido = calcular_pedido(stock_actual, stock_minimo)
    
    print("codigo: ", codigo)
    print("articulo: ", nombre)
    print("stock actual: ", stock_actual)
    print("stock minimo: ", stock_minimo)
    print("cantidad a pedir: ", cantidad_de_pedido)
    print("----------------------------------")


 print("\n1. Actualizar stock")
 print("2. Salir")

 opcion = int(input("Seleccione una opción: "))

 if opcion == 1:

    articulo_actualizar = int(input("Ingrese el número del artículo (1-5): "))

    if articulo_actualizar >= 1 and articulo_actualizar <= 5:

            nuevo_stock = int(input("Ingrese el nuevo stock actual: "))

            INVENTARIO[articulo_actualizar - 1][2] = nuevo_stock

            print("Stock actualizado correctamente.")

    else:

            print("Artículo no válido.")

 elif opcion == 2:

        print("Saliendo del sistema...")
        break

 else:

        print("Opción inválida.")

       
 #mientras el usuario no seleccione una opción válida, el programa seguirá solicitando una opción hasta que se ingrese una opción válida o se seleccione salir.

