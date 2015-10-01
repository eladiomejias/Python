

#lista = []
#lista2 = []
#var = raw_input("Ingrese lo que sea:  ")
#aux = var.strip()
#lista =  aux.split()
#print(str(len(lista)))
#print("\n"+str(lista[0]))
#lista2 = lista[0]
#print("\n"+str(lista2[0]))

def menu():
	opc = 0
	opc = int(raw_input("Programa de Encriptacion.\n1.-Encriptar codigo.\n2.-Des-encriptar codigo.\n3.-Salir.\nIngrese opcion: "))
	if(opc==1):
		calcularEncriptacion()
		return menu()
	elif(opc==2):
		calcularCodigo()
		return menu()
	elif(opc==3):
		return raw_input("Enter para salir..")
	else:
		print("Opcion no valida.\n")
        return menu()

















#Llamada principal.
menu()

