from Archivo import Archivo
from Validar import Validar
from Encrip import Encrip
from Desencrip import Desencrip
import os
#Menu que realiza el procedimiento
def menuRecursivo(alphabet):
        opc = 0
        print("Programa de Encriptacion.\n1.-Encriptar codigo.\n2.-Des-encriptar codigo.\n3.-Salir.\nIngrese opcion: ")
        opc = Validar.validarCampo()
        if(opc==1):
                #Llamadas a los metodos estaticos de cada clase.
                texto1 = raw_input("Ingrese el texto a encriptar: ")
                print("Ingrese clave - 4 - digitos distintos: ")
                clave = Validar.validarCampo2()
                #Llenado de texto.
                text = Encrip.inicioEncrip(alphabet,texto1,clave)
                Archivo.escribirArch(text)
                raw_input("Se cargo al archivo")
                return menuRecursivo(alphabet)
        elif(opc==2):
                if os.path.exists("Cripto.txt"):
                        t = Archivo.leerArch()
                        print("Ingrese clave - 4 - digitos distintos: ")
                        clave = Validar.validarCampo2()
                        text = []
                        text = Desencrip.inicioDesencrip(alphabet,t,clave)
                        raw_input("Se cargo al archivo")
                        Archivo.escribirArch(text)
                else:                        
                        print("El archivo no se encuentra.")
                return menuRecursivo(alphabet)
        elif(opc==3):
                return raw_input("Enter para salir..")
        else:
                print("Opcion no valida.\n")
                return menuRecursivo(alphabet)

#Clase principal que tieneel alphanet en el mismo
class Principal:
        alphabet = []
        alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','q','w','e','r','t','y','u','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','q','w','e','r','t','y','u','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        menuRecursivo(alphabet)






