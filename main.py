# coding: utf-8
from utils import *
from fltk import *
import sys

def affiche_image(file_path):
	'''
	fonction qui affiche le fichier specifie en parametre
	au format ppm
	'''
	# recuperation des donnees du fichier
	data = parsing(file_path)

	# definition de la taille de l image a afficher
	size = ((data['width'], data['height']))
	
	# creation de la fenetre de la taille de l image

	cree_fenetre(size[0], size[1])
	pixel = 0
	for i in range(0, size[0]):
		for j in range(0, size[1]):
			# affichage du pixel avec la couleur correspondante
			ligne(j, i, j+1, i, hex_conversion((data['pixels'][pixel]), data['max'])) 
			pixel += 1

	attend_ev()
	ferme_fenetre()


if __name__ == '__main__':
	if (len(sys.argv) == 1):
		f = input("Veuillez entrer un nom de fichier : ")
		affiche_image(f)
	else:
		affiche_image(sys.argv[1])