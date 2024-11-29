from datetime import datetime

from clases import producto


class Venta:
    def __init__(self, cliente, lista_de_productos):
        self.cliente = cliente
        self.lista_de_productos = lista_de_productos
        self.fecha = (
            datetime.now()
        )  # la fecha se registra en el momento que se intancie
        self.total = self.calcular_total()

    def calcular_total(self):
        return sum(producto.precio for producto in self.lista_de_productos)

    def registrar_venta(self):
        self.cliente.registrar_compra(self)
        return f"Venta Registrada: {self.mostrar_informacion()}"

    def mostrar_informacion(self):
        productos = ", ".join([producto.nombre for producto in self.lista_de_productos])
        # uno los productos con la , y los nombres los saco de la lista de los productos
        return f"Cliente: {self.cliente.nombre}, Productos:{productos}, Total: {self.total}"
