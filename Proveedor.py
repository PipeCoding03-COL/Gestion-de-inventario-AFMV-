class Proveedor:
    def __init__(self, nombre, direccion, telefono, productosSuministrados):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productosSuministrados = productosSuministrados

    def registrar_proveedor():
        nombre = input("Nombre del proveedor: ")
        direccion = input("Dirección del proveedor: ")
        telefono = input("Teléfono del proveedor: ")
        productosSuministrados = input("Lista de productos que suministra separados por comas: ")

        print(f"Proveedor registrado exitosamente")
        
        return Proveedor(nombre, direccion, telefono, productosSuministrados)
        
    if __name__ == "__main__":
        registrar_proveedor()