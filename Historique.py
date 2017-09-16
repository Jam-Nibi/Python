import random
resultat = random.randint(0, 100)
reponse = None
historique = []
while reponse != resultat:
    reponse = int(input('Tapez un nombre: '))
    historique.append(reponse)
    if reponse < resultat:
        print("Le nombre est plus haut!")
    elif reponse > resultat:
        print("Le nombre est pls bas")
print("Vous avez gagné !")

taille = len(historique)
print("Vous avez gagné en", taille, "coups !")

for coup in historique:
    print(' -', coup)