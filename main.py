from classVenta import Venta

venta = Venta()

venta.set_id_venta(1)
venta.set_fecha("15/10/2024")
venta.set_cliente("Joanna")

# Agregar los productos con cantidades y precios
venta.set_producto("Producto A", 2, 50.0)
venta.set_producto("Producto B", 1, 30.0)
venta.set_producto("Producto C", 3, 10.0)

venta.mostrar_detalle()


