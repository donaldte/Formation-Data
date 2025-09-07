


def addition(nombre_1, nombre_2):
    # addition de deux nombre
    # une fonction retourne toujours une valeur si il ya pas de return alors c'est procedure
    return nombre_1 + nombre_2


def soustraction(nombre_1, nombre_2):
    # soustraction de deux nombre
    return nombre_1 - nombre_2

# passage par possition et par reference 
print(soustraction(nombre_1=10, nombre_2=5))
print(soustraction(nombre_2=5, nombre_1=10))