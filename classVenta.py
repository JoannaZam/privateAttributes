class Venta:
    __id_venta = None
    __fecha = None
    __cliente = None
    # Diccionario para los productos
    __productos = {
        "Producto A": {"cantidad": 0, "precio_unitario": 0.0},
        "Producto B": {"cantidad": 0, "precio_unitario": 0.0},
        "Producto C": {"cantidad": 0, "precio_unitario": 0.0}
    }
    __total = 0.0

    # Getters para acceder a los atributos privados
    def get_id_venta(self):
        return self.__id_venta

    def get_fecha(self):
        return self.__fecha

    def get_cliente(self):
        return self.__cliente

    def get_productos(self):
        return self.__productos

    def get_total(self):
        return self.__total

    # Setters para modificar los atributos privados
    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_producto(self, nombre_producto, cantidad, precio_unitario):
        if nombre_producto in self.__productos:
            self.__productos[nombre_producto]["cantidad"] = cantidad
            self.__productos[nombre_producto]["precio_unitario"] = precio_unitario
        else:
            print(f"Error: El producto {nombre_producto} no está permitido.")

    # Metodo para calcular el total
    def calcular_total(self):
        self.__total = 0.0
        for producto, detalles in self.__productos.items():
            self.__total += detalles["cantidad"] * detalles["precio_unitario"]

    def set_total(self):
        self.calcular_total()

    # Metodo para mostrar los detalles de la venta
    def mostrar_detalle(self):
        self.calcular_total()
        print(f"ID Venta: {self.__id_venta}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente}")
        print("Productos:")
        for producto, detalles in self.__productos.items():
            if detalles["cantidad"] > 0:
                print(f"- {producto}: {detalles['cantidad']} unidades a ${detalles['precio_unitario']} c/u")
        print(f"Total: ${self.__total:.2f}")
