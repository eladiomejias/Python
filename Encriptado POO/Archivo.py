class Archivo:

	@staticmethod
	def escribirArch(text):
		fi = open("Cripto.txt", "w")
		fi.writelines(text)
		fi.close()

	@staticmethod
	def leerArch():
		fi = open("Cripto.txt","r+")
		t = fi.read()
		fi.close()
		return t
