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
