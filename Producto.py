class Producto:
    def __init__(self, nombre, descripcion, precio, stockInicial, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stockInicial = stockInicial
        self.categoria = categoria
        self.proveedores = []

    def registrarProducto():
        nombre = input("Nombre del producto: ")
        descripcion = input("Descripción del producto: ")
        precio = float(input("Precio del producto: "))
        stock_inicial = int(input("Stock inicial del producto: "))
        categoria = input("Categoría del producto: ")

        print("Producto registrado exitosamente.")

        return Producto(nombre, descripcion, precio, stock_inicial, categoria)

    def agregarStock(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad

            print(f"Se ha/n agregado {cantidad} unidad/es al stock de este producto.")
        else:
            print("Ha ingresado una cantidad inválida (debe ser de al menos x1).")

    def retirarStock(self, cantidad):
        if cantidad > 0 and cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Se han retirado {cantidad} unidades del stock. Stock actual: {self.stock}")
        elif cantidad > self.stock:
            print("Está intentando retirar una cantidad mayor a la disponible en stock.")
        elif cantidad < 0:
            print("Ha ingresado una cantidad inválida (debe ser de al menos x1).")

    def calcularValorTotal(self):
        valorTotal = self.precio * self.stock

        print(f"El valor total de este producto es: ${valorTotal:.2f}")

        return valorTotal

    if __name__ == "__main__":
        producto = registrarProducto()