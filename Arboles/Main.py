import os
from Arbol import *
#Validacion numerica.
def validarCampo():
    while True:
        try:
            var = int(raw_input(""))
            break;
        except ValueError:
            print("Ingrese solo numeros enteros.")
    return var

def submenuRecorrer(arbol):
    if(arbol==None):
        raw_input("ERROR: No se ha creado ningun arbol, porfavor crealo en el menu principal.\nEnter para volver al menu..")
        os.system("cls")
        return menuRecursivo(arbol)
    else:
        opc = 0
        print("Ingrese un tipo de recorrido.\n1.-Recorrer en Pre Orden.\n2.-Recorrer en In Orden.\n3.-Recorrer en Post Orden.\n4.-Volver al menu.\n5.-Salir\nIngrese opcion: ")
        opc = validarCampo()

        if(opc==1):
            print("El arbol recorrido en Pre Orden es: ")
            arbol.preOrden(arbol)
            raw_input("\nPresione cualquier tecla para continuar..")
            os.system("cls")
            return submenuRecorrer(arbol)

        elif(opc==2):
            print("El arbol recorrido en In Orden es: ")
            arbol.inOrden(arbol)
            raw_input("\nPresione cualquier tecla para continuar..")
            os.system("cls")
            return submenuRecorrer(arbol)

        elif(opc==3):
            print("El arbol recorrido en Pre Orden es: ")
            arbol.postOrden(arbol)
            raw_input("\nPresione cualquier tecla para continuar..")
            os.system("cls")
            return submenuRecorrer(arbol)

        elif(opc==4):
            os.system("cls")
            return menuRecursivo(arbol)
        elif(opc==5):
            raw_input("Enter para cerrar..")
            os.system('exit')
        else:
            print("Numero no valido, ingrese de nuevo: ")
            return submenuRecorrer(arbol)


def menuRecursivo(arbol):
    opc = 0;
    print("Programa de creacion de Arboles.\n1.-Crear arbol.\n2.-Agregar elemento.\n3.-Recorrer y mostrar\n4.-Salir.\nIngrese opcion: ")
    opc = validarCampo()
    if(opc==1):
        arbol = 0
        print("Ingrese nodo padre: ")
        padre = validarCampo()
        arbol = Arbol(None,padre)
        os.system("cls")
        return menuRecursivo(arbol)

    elif(opc==2):
        if(arbol==None):
            raw_input("ERROR, debe crear un arbol primero. Enter para volver al menu.")
            os.system("cls")
        else:
            print("Ingrese el elemento: ")
            element = validarCampo()
            arbol.agregar(arbol,element)
            raw_input("Se agrego un elemento al arbol.\nEnter para continuar..")
            os.system("cls")
        return menuRecursivo(arbol)

    elif(opc==3):
        os.system("cls")
        submenuRecorrer(arbol)

    elif(opc==4):
        raw_input("Enter para salir..")
        os.system("cls")

    else:
        raw_input("Numero no valido.\nEnter para seguir..")
        return menuRecursivo(arbol)


#Llamadas.
global arbol
arbol = None
menuRecursivo(arbol)
