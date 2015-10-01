import os
def menuRecursivo():
	opc = 0
	print("Programa de Encriptacion.\n1.-Encriptar codigo.\n2.-Des-encriptar codigo.\n3.-Salir.\nIngrese opcion: ")
	opc = validarCampo()
	if(opc==1):
		calculandoDatos()
		os.system("cls")
		return menuRecursivo()
	elif(opc==2):
		calcularEncriptacion()
		os.system("cls")
		return menuRecursivo()
	elif(opc==3):
		return raw_input("Enter para salir..")
	else:
		print("Opcion no valida.\n")
		return menuRecursivo()

def validarCampo():
    while True:
        try:
            var = int(raw_input(""))
            break;
        except ValueError:
            print("Ingrese solo numeros enteros.")
    return var

def validarCampo2():
	#Validacion para que la clave sea solamente sea de 4 caracteres
    var = 0
    var = raw_input("")

    if(len(var))==4:
    	return var
    else:
    	print("Debe ser solamente 4 digitos.\nIngrese de nuevo:")
    	return validarCampo2()

def calculandoDatos():
	alphabet = []
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','q','w','e','r','t','y','u','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','q','w','e','r','t','y','u','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
	texto1 = raw_input("Ingrese el texto a encriptar: ")
	print("Ingrese clave - 4 - digitos distintos: ")
	clave = validarCampo2()
	text = []
	cont = 0
	cont2 = 0
	N = len(texto1)
	#Se envia a la funcion de Encriptacions
	text = encripRecur(clave, texto1, text, cont, cont2, N, alphabet)
	cont = 0
	fi = open("Cripto.txt", "w")
	fi.writelines(text)
	fi.close()

def encripRecur(clave, texto1, text, cont, cont2, N, alphabet):
	if(cont2<N):
		if(cont == 4):
			cont = 0

		r = int(clave[cont])

		if(texto1[cont2] in alphabet):
			pos = alphabet.index(texto1[cont2])
			#sprint(alphabet[pos+r])

			if pos+r > len(alphabet):
				sitio = (pos+r)-len(alphabet)
				text.append(alphabet[sitio])
			else:
				text.append(alphabet[pos+r])

		else:
			text.append(texto1[cont2])

		cont = cont + 1
		cont2 = cont2 + 1

		return encripRecur(clave, texto1, text, cont, cont2, N, alphabet)

	else:
		return text



def calcularEncriptacion():
	if os.path.exists("Cripto.txt"):
		fi = open("Cripto.txt","r+")
		alphabet = []
		alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','q','w','e','r','t','y','u','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
		t = fi.read()
		fi.close()
		print("Ingrese clave - 4 - digitos: ")
		clave = validarCampo2()
		text  = []
		cont = 0
		cont2 = 0
		N = len(t)
		text = desenRecur(clave, t, text, cont, cont2, N, alphabet)
		fi = open("Cripto.txt","w")
		fi.writelines(text)
		fi.close()
		raw_input("\nListo su cambio, mire el archivo para el desencripto.")

	else:

		raw_input("No existe el archivo.. Presione Enter para continuar.")



def desenRecur(clave, t, text, cont, cont2, N, alphabet):

	if(cont2<N):
		if(cont==4):
			cont = 0

		r = int(clave[cont])

		if(t[cont2] in alphabet):

			pos = alphabet.index(t[cont2])
			#print(pos-r)
			sitio = pos - r

			if sitio<0:
				tam = len(alphabet)
				text.append(alphabet[tam+sitio])
			else:
				text.append(alphabet[pos-r])
		else:
			text.append(t[cont2])

		cont = cont + 1
		cont2 = cont2 + 1

		return desenRecur(clave, t, text, cont, cont2, N, alphabet)

	else:

		return text;



#Inesecario.
def escribirArch(text, N, fi, cont):
	if cont<N:
		fi.write(text[cont])
		cont = cont + 1
		return escribirArch(text, N, fi, cont)



menuRecursivo()
