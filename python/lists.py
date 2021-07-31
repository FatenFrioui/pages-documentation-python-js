# list mutable: je peut ajouter, modifier, supprimer
# on peut mettre plusieurs types de données
friends = ["faten", "sou", "mama"]
old = ["randa", "sarra", "fatma"]
# append ajoute element en fin de liste
friends.append("marwa")
friends.append(100)
friends.append(100.5)
friends.append(True)
friends.append(old)

print(friends)
print(friends[2])
print(friends[6])
print(friends[7])
print(friends[7][2])
print("******")
# extend() ->concatenation
a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["one", "Two"]

a.extend(b)
a.extend(c)
print(a)
print("******")
# remove()  ->supprimer la premiere indice sous le nom remove
x = ["faten", "sou", "mama", "sou", "sou"]
x.remove("sou")
print(x)
print("******")
# sort() trier en ordre decroissant
y = [1, 2, 100, 120, -10, 17, 29]
y.sort(reverse=True)
print(y)
print("******")
z = ["A", "B", "Z"]
z.sort(reverse=True)
print(z)
print("******")
# reverse
w = ["A", "B", 1, -5, "Z"]
w.reverse()
print(w)
print("------xxxxxxx")
# clear vider la liste
e = [1, 2, 3, 4]
e.clear()
print(e)
print("******")
# copy()
f = [1, 2, 3, 4, 1, 1]
g = f.copy()
print(f)  # main list
print(g)  # copied list
print("******")
# count compter
print(f.count(1))
print("******")
# index() retourne le premier indice de l'element demander
print(x.index("sou"))
print("******")
# insert() ajouter element dans l'indice donnée
f.insert(0, "test")
f.insert(-1, "test2")
print(f)
print("******")
# pop() retourne l'element d'indice donné
print(f.pop(-4))
