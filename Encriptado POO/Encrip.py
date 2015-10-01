class Encrip:

	@staticmethod
	def  inicioEncrip(alphabet,texto1,clave):
		text = []
		cont = 0
		cont2 = 0
		N = len(texto1)
		text = Encrip.encripRecur(clave, texto1, text, cont, cont2, N, alphabet)
		return text

	@staticmethod
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

			return Encrip.encripRecur(clave, texto1, text, cont, cont2, N, alphabet)

		else:
			return text

