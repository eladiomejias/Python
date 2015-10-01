class Desencrip:

	@staticmethod
	def  inicioDesencrip(alphabet,t,clave):
		text = []
		cont = 0
		cont2 = 0
		N = len(t)
		text = Desencrip.desenRecur(clave, t, text, cont, cont2, N, alphabet)
		return text


	@staticmethod
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

			return Desencrip.desenRecur(clave, t, text, cont, cont2, N, alphabet)

		else:

			return text;
