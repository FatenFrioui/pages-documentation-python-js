# *args packin, unpacking arguments
# n1,n2,n3,n4 *args pour afficher un nombre non fini d'arguments en appel execution
def say_hello(*peoples):
    for name in peoples:
        print(f"hello {name}")


say_hello("sou", "touna")
# 2 *args+other parameter


def show_detail(name, *skills):
    print(f"hello {name} your skills is:")
    for skill in skills:
        print(skill)


# il met le name au debut et après les skills
show_detail("faten", "html", "css", "js")
show_detail("sou", "html", "css", "js", "php")

print("="*10)

# **KWargs


def show_skills2(**skills):  # **pour definir un dictionnaire
    # print(type(skills))  #dictionary
    for skill, value in skills.items():
        print(f"{skill} => {value}")


show_skills2(html="80%", js="60%")
print("="*10)
# default parameters


def sayhello(name="Unknown", age="Unknown", country="Unknown"):
    print(f"hi {name} {age} {country}")


sayhello("fate", 20, "tun")
sayhello("sou")


# pratique ******* packing, unpacking arguments
# en cas où on ne connait pas le nombre d'arguments et etre libre
# * pour tuple
# **pour dictionary
sayhello("*"*10)

myTuple = ("html", "css", "js")

mySkills = {
    'go': "80%",
    'python': "50%",
    'mysql': "70%"
}


def show_my_skills(name, *skills, **skillswithprogress):
    print(f"Hello {name} \nSkills without progressis: ")
    for skill in skills:
        print(f"- {skills}")

    print("skills with progress is: ")
    for skill_key, skill_value in skillswithprogress.items():
        print(f"- {skill_key} => {skill_value}")


# show_my_skills("sou", "html", "css","js", java="95%")
show_my_skills("sou", *myTuple, **mySkills)
