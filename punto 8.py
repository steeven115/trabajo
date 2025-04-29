facturacion_total = 0
litros_articulo1 = 0
facturas_mas600 = 0

for i in range(5):
    codigo = input(f"Factura {i+1} - Código del artículo: ")
    litros = float(input(f"Factura {i+1} - Cantidad vendida en litros: "))
    precio_litro = float(input(f"Factura {i+1} - Precio por litro: "))
    
    total_factura = litros * precio_litro
    facturacion_total += total_factura
    
    if codigo == '1':
        litros_articulo1 += litros
    if total_factura > 600:
        facturas_mas600 += 1

print(f"Facturación total: {facturacion_total}")
print(f"Litros vendidos del artículo 1: {litros_articulo1}")
print(f"Facturas de más de 600: {facturas_mas600}")
