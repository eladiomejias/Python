def calculoFactorial(num):
	if num==0:
		return 1;
	else:
		return num*calculoFactorial(num-1)


def main():
	num = int(raw_input("Ingrese el numero:  "))
	fact = calculoFactorial(num)
	print("El factorial es: "+str(fact))
	raw_input()

main()