class NodoGrafo:
    def __init__(self, nombre, nodos, conexiones):
         self.nombre=nombre
         self.nodos = nodos
         self.conexiones = conexiones

    def mostrar(self):
         print(f'Nombre: {self.nombre}, Nodos: {self.nodos}, Conexiones: {self.conexiones}')



nuevo = NodoGrafo('hola', ['nodo1','nodo2','nodo4','nodo3'], [['nodo1','nodo2'],['nodo1','nodo4'],['nodo2','nodo4']])

         

