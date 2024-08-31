class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

def registrar_categoria():
    nombre = input("Nombre de la categoría: ")
    return Categoria(nombre)

if __name__ == "__main__":
    categorias = []
    productos = []