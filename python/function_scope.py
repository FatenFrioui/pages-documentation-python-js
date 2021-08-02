
x = 1  # global scope


def one():
    global x
    x = 2
    print(f"print variable from function scope {x}")


def two():
    x = 4  # si on l'ellimine la fonction prend valeur de global scope x déclarer dans la fonction ONE()
    print(f"print variable from function scope {x}")


print(f"print variable from global scope {x}")
one()
# => il prend le global scope déclarer au fonction ONE() puisque on a fait l'affichage après l'appel de fonction ONE()
print(f"print variable from global scope  {x}")
two()
#  =>chaque fonction prend le valeur de x déclarer dans leur propre fonction
print(f"print variable from global scope after ONE function is called {x}")
# print variable from global scope after ONE function is called 2
# elle prend le valeur correspond à global x déclarer dans la fonction ONE puisque on a appeler après ONE()
