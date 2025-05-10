import random
import json

#Accès au fichier contenant les scores
try:
    with open("Leaderboard.json", "r") as file:
        leadb = json.load(file)
except FileNotFoundError:
    leadb = {}

#Trier le tableau et affichage des 3 meilleurs joueurs
def leaderboard_calling():
    sorted_lb = sorted(leadb.items(), key=lambda x: x[1])
    print('TOP 3 PLAYERS')
    for position, (nom, score) in enumerate(sorted_lb[:3], start=1):
        print(f"{position}. {nom} : {score}")

#Niveaux de difficulte
def hardness(lvl):
    difficulte = {
        1:50,
        2:100,
        3:200,
        4:500
    }
    return difficulte.get(lvl)

#Mecanique du jeu
def le_jeu():
    global score
    while True:
        try:
            ask = int(input("Entrez un nombre:"))
        except ValueError:
            print(f"\n"
                  f"ON A DIT UN NOMBRE {nom} TU SAIS PAS LIRE !?"
                  f"\n")
            continue
        if ask < nombre_secret:
            print("Trop petit !")
            score += 1
        elif ask > nombre_secret:
            print("Trop grand!")
            score += 1
        else:
            print(f"Bravo {nom}! Vous avez réussi en {score} coups !")
            if nom not in leadb or leadb[nom] > score:
                leadb[nom] = score
            else:
                print(f"Votre meilleur score est de {leadb[nom]}")
            with open("Leaderboard.json", "w") as file:
                json.dump(leadb, file)
                break

def recommencer():
    while True:
        print(f"Voulez-vous recommencer une partie ? y/n")
        reponse = str(input())
        if reponse == "y":
            return True
        elif reponse == "n":
            print("Merci d'avoir joué !")
            return False
        else:
            print("Merci d'écrire 'n' ou 'y'")

#gestion d'erreur
def erreur_de_typo():
    print(f"\n"
          f"Choisissez le niveau par son chiffre: 1, 2, 3 ou 4"
          f"\n")

#Introduction
leaderboard_calling()
nom = str(input("Entrez votre nom:"))

while True:
    try :
        choix = int(input((f"Choisissez le niveau de difficulté : \n"
          f"1- Facile (0-50)\n"
          f"2- Moyen (0-100)\n"
          f"3- Difficile (0-200)\n"
          f"4- HARDCORE (0-500) \n"
                       f"Votre choix :")))
    except ValueError:
        erreur_de_typo()
        continue
    if hardness(choix) is None:
        erreur_de_typo()
        continue
    nombre_secret = random.randint(0, hardness(choix))
    print(f"Bonjour {nom}, votre objectif est de deviner le nombre entre 0 et {nombre_secret} !")
    print("C'est parti !")

    score = 0

    #Début du jeu
    le_jeu()
    if not recommencer():
        break