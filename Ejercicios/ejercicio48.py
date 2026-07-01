# Ejercicio 48: Inventario de Tienda
inventario = {
    "Laptop": [(800, 5)],
    "Mouse": [(15, 50)],
    "Teclado": [(25, 2)]
}

valor_total = 0
productos_bajo_stock = []
LIMITE_STOCK_BAJO = 5

for producto, datos in inventario.items():
    for precio, stock in datos:
        valor_total += precio * stock
        if stock <= LIMITE_STOCK_BAJO:
            productos_bajo_stock.append((producto, stock))

print("Valor total del inventario: $", valor_total)
for producto, stock in productos_bajo_stock:
    print("Producto con bajo stock:", producto, "(", stock, "unidades)")
