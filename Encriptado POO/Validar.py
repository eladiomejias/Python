class Validar:

	#Validacion para que la clave sea solamente  de 4 caracteres
	@staticmethod
	def validarCampo2():
                
                var = 0
                var = raw_input("")

                if(len(var))==4:
                        return var
                else:
                        print("Debe ser solamente 4 digitos.\nIngrese de nuevo:")
                        return Validar.validarCampo2()



        #Validacion para el campo numerico del menu.
        @staticmethod
        def validarCampo():
                while True:
                        try:
                                var = int(raw_input(""))
                                break;
                        except ValueError:
                                print("Ingrese solo numeros enteros.")
                return var

