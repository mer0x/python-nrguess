#!/usr/bin/python2.7
import Tkinter
import random

calculatorul_ghiceste = random.randint(1,10)
def verifica():
	utilizator_presupunere = int(txt_guess.get())
#Determina cum este numarul introdus
	if utilizator_presupunere < calculatorul_ghiceste:
		msg = "Incearca un nr. mai mare"
	elif utilizator_presupunere > calculatorul_ghiceste:
		msg = "Incearca un nr. mai mic"
	elif utilizator_presupunere == calculatorul_ghiceste:
		msg = "Ai ghicit numarul!"
	else:
		msg = "A aparut o eroare.."
		
	lbl_result["text"] = msg

	#Stergere automata date introduse
	txt_guess.delete(0, 5)
#Functia de legare a butonului "reset" + mesaj de afisare .
def reseteaza():
	global calculatorul_ghiceste
	calculatorul_ghiceste = random.randint(1,10)
	lbl_result["text"] = "Jocul a fost restartat,incearca din nou!"

#Creeaza fereastra
root = Tkinter.Tk()

#Schimbare culoare de fundal 
root.configure(bg="white")
#Blocare redimensionare fereastra
root.resizable(width=False, height=False)
#Schimbare titlu
root.title("Ghiceste Numarul")
#Schimbare dimensiuni fereastra
root.geometry("350x100")
#Creeaza butoanele/widget-uri
lbl_title = Tkinter.Label(root, text="Bine ai venit la Ghiceste Numarul", bg="white")
lbl_title.pack()

lbl_result = Tkinter.Label(root, text="(Interval numere[1-10])" ,bg="white")
lbl_result.pack()

btn_check = Tkinter.Button(root, text="Verifica", fg="green", command=verifica ,bg="white")
btn_check.pack(side="left")

btn_reset = Tkinter.Button(root, text="Resteaza", fg="red", command=reseteaza, bg="white")
btn_reset.pack(side="right")

txt_guess = Tkinter.Entry(root, width=3)
txt_guess.pack()

lbl_title = Tkinter.Label(root, text="\n Created by Mer0x Inc. ", bg="white")
lbl_title.pack()

#Pornire main events loop
root.mainloop()
root.destroy()