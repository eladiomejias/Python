from Tkinter import *
from Archivo import *
import Tkinter, tkFileDialog
import tkMessageBox
import os
#Clase Interfaz,, recibe la ventana Tk(). El constructor definido en esta clase, inicializa todos los elementos de la ventana
class Interfaz:
	def __init__(self, ventana):
		ventana.geometry("325x300")
		ventana.title('HidePass - Backtracking Program')
		ventana.iconbitmap('redhat.ico')
		ventana.config(bg="#f8f8f8")
		self.text = StringVar()
		self.contra = StringVar()
		self.label1 = Label(ventana,text="Bienvenido a HidePass.", font=("Calibri",12), fg="#b81d30", bg="#f8f8f8")
		self.label1.grid(padx=0, pady=20, row=1, column=2,)
		self.label2 = Label(ventana,text="Ruta del archivo", font=("Calibri",11), bg="#f8f8f8")
		self.label2.grid(row=2,column=2)
		self.label3 = Label(ventana,text="Nombre del archivo: ",font=("Calibri",11), bg="#f8f8f8")
		self.label3.grid(row=4,column=2, pady=20, padx=15)
		self.label4 = Label(ventana, textvariable=self.text, font=("Calibri",11), bg="#f8f8f8")
		self.label4.grid(row=4,column=3)
		self.label6 = Label(ventana,text="Contrasena: ", font=("Calibri",11), bg="#f8f8f8").grid(row=5,column=2,pady=20)
		self.label5 = Label(ventana, textvariable=self.contra, font=("Calibri",11), bg="#f8f8f8")
		self.label5.grid(row=5, column=3)
		self.entry1 = Entry(ventana, width=30, bg="#f8f8f8")
		self.entry1.grid(row=3,column=2, padx=10, pady = 10)
		self.b1 = Button(ventana, text="Examinar", command = self.explorer, bd=0, bg="#e7e5d9",activebackground="#cfcec3",font=("Calibri",10))
		self.b2 = Button(ventana, text="Unrar now!", command= self.buscarContra, font=("Calibri",9))
		self.b1.grid(row=3,column=3)
		self.b2.grid(row=6,column=2, pady=5, padx=0)
		self.entry1.insert(0,"Pulsa examinar..")
		self.entry1.configure(state="readonly")

	#Meotod explorer que esta juntada con el Command de Examinar. Este metodo abre una ventana para buscar el archivo y desactiva algunas propiedades.
	def explorer(self):
		self.entry1.configure(state="normal")
		file_path = tkFileDialog.askopenfilename()
		value = os.path.basename(file_path)
		self.entry1.delete(0, END)
		self.entry1.insert(0,file_path)
		self.entry1.configure(state="readonly")
		self.text.set(value)
		self.contra.set("")
		if (value!=""):
			self.label4.configure(bg="#f8f8f8")#Testing.
			self.label5.configure(bg="#f8f8f8",fg="#b81d30")


	#Metodo buscarContra que esta con el Command de Unrar now!. Donde crea en el el objeto del tipo Archivo, pasandole el directorio.
	#Prueba en el mismo la devolucion de si el archivo es rar o no, y muestra un mensaje.
	def buscarContra(self):
		if self.entry1.get()!="Pulsa examinar..":
			dir = self.entry1.get()
			#De aqui para abajo se puede hacer orientado a objetos dividiendo esta parte.
			directorio = Archivo(dir)

			valor = directorio.validarArchivo(self.contra)

			if valor == False:
				tkMessageBox.showinfo("ERROR!!", "El archivo no es rar.")

		else:
			tkMessageBox.showinfo("ERROR!!", "Ingrese un archivo.")
