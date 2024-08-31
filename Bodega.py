class Bodega:
    def __init__(self, nombre, ubicacion, capacidadMax, productosSuministrados):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidadMax = capacidadMax
        self.productosSuministrados = productosSuministrados

    def registrarBodega():
        nombre = input("Nombre de la bodega: ")
        ubicacion = input("Ubicación de la bodega: ")
        capacidadMax = int(input("Capacidad máxima de la bodega: "))
        productosSuministrados = input("Lista de productos almacenados: ")

        print(f"Bodega registrada exitosamente.")
        
        return Bodega(nombre, ubicacion, capacidadMax, productosSuministrados)

    def agregarStock(self, Producto, cantidad):
        print(f"Agregar stock. Producto: {Producto} x{cantidad}")

    def retirarStock(self, Producto, cantidad):
        print(f"Agregar stock. Producto: {Producto} x{cantidad}")

    if __name__ == "__main__":
        registrarBodega()