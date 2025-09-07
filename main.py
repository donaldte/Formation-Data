# python 
# vscode 


# les variable en python 

"""  
ensemble des nombre entier representer par N 
ensemble des nombre decimal representer par D 
ensemble des nombre complexe representer par C( i au carré = -1 )
racine caree 
""" 

nom = "jean"
text = "nombre d'article vendu"

nombre_de_vente = 10 
nombre_decimal = 10.5
nombre_complexe = 3 + 5j

# pour afficher une variable on utilise print

print(nom, nombre_de_vente, nombre_decimal, nombre_complexe)

# pour executer le code python nom du fichier.py

# les function predefinie ou builtin function (don't repeat yourself)

# type des donnees
print(type(nom), type(nombre_de_vente), type(nombre_decimal), type(nombre_complexe))


# operation arithmetique 
nombre_de_vente = 50 
prix_unitaire = 1000 

prix_total_des_ventes = nombre_de_vente * prix_unitaire

nombre_de_vente_date_1 = 10 
nombre_de_vente_date_2 = 20
nombre_de_vente_total = nombre_de_vente_date_1 + nombre_de_vente_date_2

total_des_vente_semaine_1 = 1000000
prix_unitaire_semaine_1 = 1000
nombre_daticle_semaine_1 = total_des_vente_semaine_1 / prix_unitaire_semaine_1

print('addition : ', nombre_de_vente_total)
print('soustraction : ', nombre_de_vente_total - nombre_de_vente_date_1)
print('multiplication : ', nombre_de_vente_total * nombre_de_vente_date_1)
print('division : ', nombre_de_vente_total / nombre_de_vente_date_1)
print('division entiere : ', nombre_de_vente_total // nombre_de_vente_date_1)

""" 
difference entre / et //
/ division classique 
// division entiere
"""


# les function 

# print, type, int, float, str, input , len, max, min, sum, round, abs, pow, sqrt, ceil, floor, random, range, enumerate, zip, reversed, sorted, any, all, sum, map, filter, zip_longest, enumerate,

nombre_float = 10.5 

arrondir = round(nombre_float, 1)
# convertir un float en int
nombre_entier = int(nombre_float)

# taille d'une chaine de caractere
nom = 'jean'
taille = len(nom)

# structure donnees 
liste = ['jean', 'marc', 'philippe', 'jean', 2, 3.5]
liste_des_notes = [10, 20, 30, 40, 50, 60]
max_liste = max(liste_des_notes)




