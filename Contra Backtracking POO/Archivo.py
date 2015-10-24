import rarfile
import tkMessageBox
#Clase archivo, en esta clase se toma un inicializa el directorio en el constructor.
class Archivo:

    def __init__(self, dir):
        self.dir = dir

    #Metodo validarArchivo en este metodo se calcula la extension del archivo que esta en el directorio, si es un archivo RAR es valido, de resto no.
    def validarArchivo(self, contra):
        #Dividiendo el nombre
        type = self.dir.split(".")[-1]

        if type=="rar":
            self.calcularBack(contra)
        else:
            return False

    #Este metodo al ya saber que el archivo es Rar, se verifica si nesecita clave, si lo nesecita entra en un If donde se empieza a iterar la lista de claves.
    #El valor de "busco", varia entre True y False, es True si la clave fue exitosamente conseguida mediante la lista iterativa, si no, devuelve False.
    #Al caer False se ingresa en el metodo del Backtracking
    #Si no tiene clave, devuelve un aviso para el usuario.
    def calcularBack(self, contra):
        rf = rarfile.RarFile(self.dir)

    	if rf.needs_password()==True:
    		busco = self.metodoComun(rf, contra)

    		if busco==False:
    			self.metodoBacktrack(rf, contra)

    	else:
    		tkMessageBox.showwarning("Aviso", "El rar no tiene clave.")


    #Este metodo tiene una lista iterativa con las claves comunes y no comunes, para reducir el tiempo de espera para el usuario.
    def metodoComun(self, rf, contra):
    	#Lista con las claves comunes y no comunes.
    	contras = ["0000","1111","2222","3333","4444","5555","6666",
    	"7777","8888","9999","1234","1212","1004","2000","1122","6969","1313",
    	"4321","2001","1010",
    	#Claves no comunes.
    	"8557","9047","8438","0439","9539","8196","7063","6093","6827","7394",
    	"0859","8957","9480","6793","8398","0738","7637","6835","9629","8093",
    	"8068"]

    	tempo = False
    	value = ""

    	for i in range(0,len(contras)):
    		try:
    			rf.extractall(None,None,contras[i])
    			value = contras[i]
    			tempo = True
    			break
    		except rarfile.RarCRCError:
    			continue

    	if tempo==True:
    		#Cuando se consigue la clave, el valor de tempo es True, por lo tanto se manda como set al textvariable contra del label a mostrar.
    		contra.set(value)

    	return tempo

    #Metodo Backtrack. este metodo es el principal fuerza bruta, es un while infinito donde convierte el valor de un entero en String dependiendo de su cantidad
    #Para que siga en el rango de los 4 digitos.
    #Se observa tambien un If donde si es mayor a 9999, rompe el bucle de iteracion y manda un Error Fatal.
    #Se maneja un try y un except, para iterar y probar cada clave que tome var en el rango de 0 / 9999
    #El except actua cuando la clave es fallida, var incrementa en uno.
    #Si logro ingresar en alguna clave mediante try, se rompe el bucle.
    def metodoBacktrack(self, rf, contra):
        var = 0
        valido = True
        while True:
            psw = str(var)
            if len(psw) == 1:
                psw = "000"+psw
            elif len(psw) == 2:
                psw = "00"+psw
            elif len(psw) == 3:
                psw = "0"+psw

            if(var>9999):
                tkMessageBox.showerror("Error Fatal", "El rar tiene una clave mayor a 4 digitos, no se puede seguir iterando.")
                valido = False
                break

            print(psw)

            try:
                rf.extractall(None,None,psw)
                break
            except rarfile.RarCRCError:
			    var = var + 1

        if valido==True:
            contra.set(psw)
