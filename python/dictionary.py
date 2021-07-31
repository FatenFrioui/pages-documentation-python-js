user = {
    "name": "faten",
    "age": "37",
    "country": "tunisie",
    "skills": ["html", "css"],
    "rating": 10.5
    # (1,2,3):"test",
    # 1:"5"
}

print(user)

print(user['age'])
print("******")
print(user.get("age"))
print("******")
print(user.keys())
print(user.values())
# 2D dictionary
print("-----")
languages = {
    "one": {
        "name": "html",
        "progress": "80%"
    },
    "two": {
        "name": "css",
        "progress": "70%"
    }
}
print(languages)
print(languages['one'])
print(languages['two']['name'])
# length
print("******")
print(len(languages))
print(len(languages['two']))

frame1 = {
    "name": "angualar",
    "progress": "80%"
}
frame2 = {
    "name": "angualar",
    "progress": "80%"
}
frame3 = {
    "name": "angualar",
    "progress": "80%"
}
allframe = {
    "one": frame1,
    "two": frame2,
    "three": frame3,
}
print(allframe)
print("+"*10)
print(user.setdefault("name", "sou"))
print(user)
# popitem()
member = {
    "name": "sou",
    "age": "40"
}
print(member)
member.update({"age": 38})
print(member.popitem())
print("="*10)
# items()
allitems = member.items()
print(member)
member["age"] = 41
print(allitems)
# fromkeys() donne les keys valeur x
a = ('one', 'two', 'three')
b = "x"
print(dict.fromkeys(a, b))

# clear vider
print("="*10)
print(user)
user.clear()
print(user)
# update ajouter un nouveau element ou modifier
print("="*10)
print(member)
member.update({"country": "egypt"})
print(member)
# copy
b = member.copy()
print(b)
member.update({"skills": "php"})
print(member)
print(b)
# keys(),values()
print("="*10)
print(member.keys())
print(member.values())
