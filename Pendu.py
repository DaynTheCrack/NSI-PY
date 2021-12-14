# -*- coding: utf-8 -*-
import csv 
import random
"""Lecture de la table de donnée qui pioche un mot de la liste au hasard"""
Ouverture = open("Test1.csv")
FichierCSV = csv.reader(Ouverture)
listeX = []
listeXstr = ""
for ligne in FichierCSV:
    x = ligne[random.randint(0,len(ligne))]
    mot = "".join(x)

nbre_coups_max = 2  # Nombre de coups max et en cours de jeu
nbre_coups = 0
liste_mot_bis = [] #Liste du mot caché au file du jeu
stock = []
stockSTR = ""
NumberLettre = 0
Lettre_bonne = False

"""Création du mot_bis sous forme '------' """
mot_bis = ""       
for lettre in mot:
    mot_bis = mot_bis + "-"
for lettre_num in range(len(mot_bis)):
    liste_mot_bis.append(mot_bis[lettre_num])
print(mot_bis)
    
"""Ajoute la lettre si la lettre saisie est dans le mot"""
def Mot_encours(lettre):
    global NumberLettre
    global mot_bis
    liste_mot_bis[NumberLettre] = lettre
    mot_bis = "".join(liste_mot_bis)
           
"""Saisie d'une lettre par l'utilisateur"""
def Saisie_lettre():
    lettre=str(input("Saisissez une lettre : "))
    return lettre 

"""Stock les lettres déja jouées"""
def deja_joue(lettre):
    global stock
    global stockSTR
    stock.extend([lettre,"-"])
    stockSTR = "".join(stock)
    return stockSTR
  
"""Teste si la lettre demandÃ©e est dans le mot"""  
def lettre_mot(lettre):
    for i in range(len(mot)):
        if lettre == mot[i]:
            global NumberLettre
            global Lettre_bonne
            global stock
            NumberLettre = i
            Mot_encours(lettre)
            print(mot_bis)
            if lettre in stockSTR:
                print("Vous avez déjà joué cette lettre !\n","Lettres déjà jouées :",stockSTR)
            else:
                print("Les lettre déjà jouées:", deja_joue(lettre))
            Lettre_bonne = True
            return True
    Lettre_bonne = False
    print(mot_bis)
    if lettre in stockSTR:
        print("Vous avez déjà joué cette lettre !\n","Lettres déjà jouées :",stockSTR)
    else:
        print("Les lettre déjà jouées:", deja_joue(lettre))
    return False

"""Boucle prncipale qui permet d'arreter le programe dans le cas ou le nombre de coups max est dépassé"""
while nbre_coups < nbre_coups_max :
    print(lettre_mot(Saisie_lettre()))
    if Lettre_bonne == False:
        nbre_coups += 1
    if mot_bis == mot:
        print("Vous avez Gagné !!")
        break
if nbre_coups_max == nbre_coups:
    print("\n"+str("You lost"))

    """Ajouter un try expect pour les lettres déjà jouées et modifier le mot fixe d'entrer en input"""
