import rarfile
from Tkinter import *

#vent = Tk()
#vent.mainloop()
#vent.config


rf = rarfile.RarFile('Texto.rar')
#rf.extractall(None,None,'0')
if rf.needs_password()==True:
	print "Hi"


def main():
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


	print("Ready the pass is: "+psw)


	raw_input()



main()
