def menuRecursivo():
	opc = 0
	opc = int(raw_input("Bienvenido.\n1.-Calcular pares.\n4.-Salir.\nIngrese: "))
	if opc == 4:
		return raw_input("Enter para salir...")
	elif opc==1:
		cont = 0
		total = 0
		num = int(raw_input("Ingrese numero: "))
		total = calcularPar(num, cont)
		print("El total de cantidad de pares es: "+str(total))
		raw_input("Enter para salir..")
	else:
		print("No valido.")
		return menuRecursivo()


def calcularPar(num,cont):
	r = 0
	if num == 0:
		return cont
	else:
		r = num % 10
		num = num / 10
		if(r%2==0):
			cont = cont + 1

		return calcularPar(num,cont)




menuRecursivo()
