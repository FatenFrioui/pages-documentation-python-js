# on ne peut pas changer sur le tuple
mytuple = ("faten", "sou")
mytuple2 = "faten", "sou"
print(mytuple)
print(mytuple2)
print(type(mytuple))
print(type(mytuple2))
print("******")
# tuple indexing
mytuple3 = (1, 2, 3, 4)
print(mytuple3[-1])
# tuple assign values ne supporte pas les changements
print("******")
# tuple items
mytuple4 = ("faten", "sou", 1, 2, 3)
print(mytuple4[1])
print(mytuple4[-1])

print("-------")
# opérateurs pour liste, tuple
# len
# concatenation
c = mytuple3+mytuple4
d = mytuple3+("A", "B", True)+mytuple4
print(c)
print(d)
print("******")
# repeat(*) tuple, list, string
mystring = "sou"
mylist = [1, 2]
mytuple = ["A", "B"]
print(mystring * 3)
print(mylist * 3)
print(mytuple * 3)
print("******")
# methods
# count()
# index()
xx = (1, 3, 7, 8, 2, 6, 5)
print("the position of index is {:d}".format(xx.index(7)))
print(f"the position of index is {xx.index(7)}")
print("******")
# tuple destruct
aa = ("A", "B", 4, "C")
x, y, _, z = aa
print(x)
print(y)
print(z)
