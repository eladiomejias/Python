class Arbol:
    def __init__(self, arbol, dato):
            self.derecha = None
            self.dato = dato
            self.izquierda = None

    def agregar(self, arbol, dato):

            if arbol.dato > dato:
                self.agregarIzquierda(arbol, dato)
            elif arbol.dato < dato:
                self.agregarDerecha(arbol, dato)

    def agregarIzquierda(self, arbol, dato):
            if arbol.izquierda is None:
                arbol.izquierda = Arbol(arbol, dato)
            else:
                self.agregar(arbol.izquierda, dato)

    def agregarDerecha(self, arbol, dato):
            if arbol.derecha is None:
                arbol.derecha = Arbol(arbol, dato)
            else:
                self.agregar(arbol.derecha, dato)

    def preOrden(self, arbol):
            print(arbol.dato)
            if arbol.izquierda is not None:
                self.preOrden(arbol.izquierda)
            if arbol.derecha is not None:
                self.preOrden(arbol.derecha)

    def inOrden(self, arbol):
            if arbol.izquierda is not None:
                self.inOrden(arbol.izquierda)
            print(arbol.dato)


            if arbol.derecha is not None:
                self.inOrden(arbol.derecha)

    def postOrden(self, arbol):
            if arbol.izquierda is not None:
                self.postOrden(arbol.izquierda)
            if arbol.derecha is not None:
                self.postOrden(arbol.derecha)
            print(arbol.dato)
