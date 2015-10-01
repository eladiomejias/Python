from __future__ import print_function
def menuRecursivo(lista):
	opc = 0
	opc = int(raw_input("Programa de Encriptacion.\n1.-Encriptar codigo.\n2.-Des-encriptar codigo.\n3.-Salir.\nIngrese opcion: "))
	if(opc==1):
		calcularCodigo(lista)
		return menuRecursivo(lista)
	elif(opc==2):
		calcularEncriptarcion(lista)
		return menuRecursivo(lista)
	elif(opc==3):
		return raw_input("Enter para salir..")
	else:
		print("Opcion no valida.\n")
		return menuRecursivo(lista)


def calcularCodigo(lista):
	#Palabras
	pals = []
	code = []
	cont = 0;
	var = raw_input("Ingrese lo que desea encriptar: ")
	pals = var.strip()
	N = len(pals)
	#print(str(N))
	#print(str(pals[0]))
	code = encripRecur(lista, pals, N, cont, code)
	print("\nEl codigo encriptado es:  ")
	imprimirLista(code)
	print("\n")


def imprimirLista(lista1):
	 for x in range(0,len(lista1)):
	 	print(str(lista1[x]), end='')

def encripRecur(lista, pals, N, cont, code):
	
	if(cont<N):
		if (lista.get(str.lower(pals[cont]))!=None):
			code.append((lista.get(str.lower(pals[cont]))))
		else:
			code.append(str.lower(pals[cont]))
		cont = cont + 1
		return encripRecur(lista, pals, N, cont, code)
	else:
		return code



def main():
	lista = {'a':"b1", 'b':"f2", 'c':"tk", 'q':"fg", 'w':"ui", 'e':"op", 'r':"yb", 't':"xc", 'y':"9k", 'u':"sa", 'i':"23", 'o':"nm", 'p':"lk",
	's':"jd", 'd':"fa", 'f':"hx", 'g':"1b", 'h':"k4", 'j':"ii", 'k':"56", 'l':"mb", 'z':"ae", 'x':"vw", 'v':"er",'n':'25','m':"12",
	'1':"pt", '2':"3r", '3':"qx", '4':"sd", '5':"yt", '6':"jk", '7':"br", '8':"oi", '9':"ca", '0':"kh",
	'?':'t2','!':"~$"}
	menuRecursivo(lista)

main()
