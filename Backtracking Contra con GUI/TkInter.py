from Tkinter import *
import rarfile
import Tkinter, tkFileDialog
import tkMessageBox
import os


def explorer():
	entry1.configure(state="normal")
	file_path = tkFileDialog.askopenfilename()
	value = os.path.basename(file_path)
	entry1.delete(0, END)
	entry1.insert(0,file_path)
	entry1.configure(state="readonly")
	text.set(value)
	contra.set("")
	if (value!=""):
		label4.configure(bg="#f8f8f8")#Testing.


def buscarContra():
	if entry1.get()!="Pulsa examinar..":
		dir = entry1.get()
		#De aqui para abajo se puede hacer orientado a objetos dividiendo esta parte.
		validarArchivo(dir)
	else:
		tkMessageBox.showinfo("ERROR!!", "Ingrese un archivo.")

def validarArchivo(dir):
	#Division del nombre
	type = dir.split(".")[-1]

	if type=="rar":
		calcularBack(dir)
	else:
		tkMessageBox.showinfo("ERROR!!", "El archivo no es rar..")

def calcularBack(dir):
	rf = rarfile.RarFile(dir)

	if rf.needs_password()==True:
		busco = metodoComun(rf)

		if busco==False:
			print "si"
			metodoBacktracking(rf)

	else:
		tkMessageBox.showwarning("Aviso", "El rar no tiene clave.")

def metodoComun(rf):
	#Diccionario comunes y no comunes.
	contras = ["0000","1111","2222","3333","4444","5555","6666",
	"7777","8888","9999","1234","1212","1004","2000","1122","6969","1313",
	"4321","2001","1010",
	#No comunes.
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
		#Esto npi..
		contra.set(value)

	return tempo


def metodoBacktracking(rf):
	var = 0
	while True:
		psw = str(var)
		if len(psw) == 1:
			psw = "000"+psw
		elif len(psw) == 2:
			psw = "00"+psw
		elif len(psw) == 3:
			psw = "0"+psw

		print(psw)
		try:
			rf.extractall(None,None,psw)
			break
		except rarfile.RarCRCError:
			var = var + 1



	#print("Ready the pass is: "+psw)
	#Esto no se hace por la herencia de la clase me imagino que debe ser un metodo estatico..
	contra.set(psw)



ventana = Tk()
ventana.config()
ventana.geometry("350x300")
ventana.title('Backtracking Program')
text = StringVar()
contra = StringVar()
#vent.iconbitmap('icon-short.ico')
label1 = Label(ventana,text="Bienvenido a RAR-Backtrack")#,font=('Calibri',12)
label2 = Label(ventana,text="Ruta del archivo")
label3 = Label(ventana,text="Nombre del archivo: ")
label4 = Label(ventana, textvariable=text)
label6 = Label(ventana,text="Contrasena: ")
label5 = Label(ventana,textvariable=contra)
b1 = Button(ventana, text="Examinar", command = explorer, bd=0, bg="#d7ccc8",activebackground="#837062")
b2 = Button(ventana, text="Unrar now!", command= buscarContra)
entry1 = Entry(ventana, width=30)
entry1.insert(0,"Pulsa examinar..")
entry1.configure(state="readonly")




#Como se colocaran.
label1.grid(padx=0, pady=20, row=1, column=2)
label2.grid(row=2,column=2)
entry1.grid(row=3,column=2, padx=10, pady = 10)
b1.grid(row=3,column=3)
label3.grid(row=4,column=2, pady=20, padx=15)
label4.grid(row=4,column=3)
label6.grid(row=5,column=2,pady=20)
label5.grid(row=5, column=3)
b2.grid(row=6,column=2, pady=5, padx=0)



ventana.mainloop()
