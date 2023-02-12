import csv
from random import choice
from tkinter import *
import webbrowser
from PIL import ImageTk,Image
import os
import sys

films = []
durees = []
dates = []
sites = []
flag = 0


def resource_path(relative_path):
    """ pour la compatibilité de fichiers PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    

  
with open(resource_path('liste/disney.csv'), newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:				#ON IMPORTE LES DONNEES DANS DES LISTES	
		films.append(row[1])
		durees.append(int(row[2]))
		dates.append(row[3])
		sites.append(row[4])
	
tire = choice(films)					#ON TIRE UN FILM AU SORT


#ON MET EN PLACE LE TEXTE POUR ENSUITE
film = 'FILM : '+tire
if durees[films.index(tire)] <60: #SI MOINS D'UNE HEURE
	duree = 'DUREE : '+str(durees[films.index(tire)])+'MIN'
if durees[films.index(tire)]%60 < 10: #SI MINUTES < 10
	duree = 'DUREE : '+str(durees[films.index(tire)]//60)+'H '+'0'+str(durees[films.index(tire)]%60)+'MIN'
else:
	duree = 'DUREE : '+str(durees[films.index(tire)]//60)+'H '+str(durees[films.index(tire)]%60)+'MIN'
date = 'DATE : '+dates[films.index(tire)]
site = 'SITE : '+sites[films.index(tire)]



def acceder(): #OUVRIR LE LIEN DISNEY+ (bouton tkinter : acceder)
	webbrowser.open(sites[films.index(tire)])
	
def restart(): #RETIRER AU SORT (bouton tkinter : relancer)
    python = sys.executable
    os.execl(python, python, * sys.argv)
	

x = Tk() #ON MET EN PLACE LA FENETRE
x.title('disney aleatoire')
x.resizable(width=False, height=False) #POUR QU'ON NE PUISSE PAS LA REDIMENSIONNER 

#ON IMPORTE LE TEXTE D'AUPARAVANT
Label(x,text=film).pack()
Label(x,text=duree).pack()
Label(x,text=date).pack()
Label(x,text=site).pack()


if sites[films.index(tire)] != 'AUCUN LIEN': #SI PAS DISPONIBLE SUR DISNEY+ : ON N'AFFICHE PAS LE BOUTON "ACCEDER"

	lien = Button(x,text='ACCEDER',command=acceder, bg='black', fg='red')
	lien.pack()


#ON MET EN PLACE L'AFFICHE DU FILM
photo = Image.open(resource_path("affiches/"+str(films.index(tire)+1)+".png"))
resized = photo.resize((310,420))
new_photo = ImageTk.PhotoImage(resized)
label = Label(x,image=new_photo)
label.pack(pady=20)


#BOUTON "RELANCER"
relancer = Button(x,text='RELANCER', command=restart, bg='black', fg='red')
relancer.pack()

#BOUTON "QUITTER"
quit = Button(x,text='QUITTER', command=x.quit, bg='black', fg='red')
quit.pack()

x.mainloop()
