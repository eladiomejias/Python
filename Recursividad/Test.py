from __future__ import print_function

a = []
a = raw_input("Ingrese string:  ")
l = []
l = raw_input("Ingrese clave 4 digitos distintos: ")

text = []
#text.append(ord(a[0])+ord(l[0]))

#print(chr(2))
#print(chr(text[0]))
cont = 0
for x in range(0,len(a)):

	if cont==4:
		cont = 0

	suma = ord(a[x]) + ord(l[cont])

	text.append(suma)

	cont = cont + 1

print("Tu codigo encriptado es:  ")


for  x in range(0,len(text)):
	print(text[x],end='')



raw_input()
