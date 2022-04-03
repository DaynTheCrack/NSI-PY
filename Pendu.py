"""Programme du Pendu python voir chap #17 python OpenClassRoom"""
import random
import os
def clear(): # création d'une fonction clear
    os.system("cls")
nbr_try = 8 # nombre d'essaies maximum
already_use_letter = [] # liste qui contienr les lettres utilisées

liste_mots = [ # liste des mots
    "poisson",
    "bateau",
    "baton",
    "canard",
    "poubelle",
    "chocolat",
    "arbre",
    "voiture",
    "spatule",
    "bonbon",
    "tarte",
    "café",
    "herbe",
    "plante",
    "train",
    "poisson",
    "parent",
    "tartine"
]
def pendu(liste,alrady_use,nbr_try):
    mot_mystere = [lettre for lettre in liste_mots[random.randint(0,len(liste_mots)-1)]] # on pique un mot au hazard et on décompose le mot

    mot_list = ["-" for nbr in range(len(mot_mystere))] # on présente le mot sans montrer quelles sont les lettres
    mot = "".join(mot_list)
    print("Mot à deviner :\n",mot) # on écrit le mot à deviner
    while nbr_try > 0: # répétition des actions jusqu'à var nombre try < 0
        lettre = str(input("Quel lettre voulez vous choisir ?\nLettres déjà utilisées : " + ", ".join(already_use_letter) + "\n"))
        if lettre in mot_mystere: # si la lettre est dans le mot alors on lance la recherche
            for num in range(len(mot_mystere)): # on relève le numéro des éléments de la liste 
                if mot_mystere[num] == lettre: # si la lettre du numéro de la liste est la meme que la lettre on remplace "-" par la lettre
                    mot_list[num] = lettre # on remplace le '-' de l'emplacement de la lettre par la lettre
        if "".join(mot_list) == "".join(mot_mystere): # si les deux mots sont identiques alors c'est gagné
            clear() # on efface tout
            print("Vous avez gagné le mot était bien {0}!".format("".join(mot_mystere))) # on remplace {} par le mot à deviner
            break # on stop le programme
        if lettre not in mot_list:
            nbr_try -= 1 # si la lettre n'est pas dans le mot alors on enlève 1 essai
            if nbr_try == 0: # si le nombre d'essaie est = 0 alors le joueur a perdu
                clear() # on efface tout
                print("Vous avez perdu le mot était {0}!".format("".join(mot_mystere)))
                break # on stop le programme
        mot = "".join(mot_list)
        if lettre not in already_use_letter: # si la lettre a déjà étée entrée on ne la rajoute pas dans la liste des lettres utilisées
            already_use_letter.append(lettre)
        clear()
        print(mot," Try restant :",nbr_try)
    
pendu(liste_mots,already_use_letter,nbr_try)

