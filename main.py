from noeud import Noeud


deux = Noeud(valeur = 2)
y = Noeud(valeur = "y")
plus = Noeud(valeur = "+")

plus.ajouter(deux)
plus.ajouter(y)

exp = Noeud(valeur = "exp")
exp.ajouter(plus)

print(exp.affichage_polonais())