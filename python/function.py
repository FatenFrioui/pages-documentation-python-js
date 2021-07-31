def function_name():
    print("hello")


function_name()
datafunction = function_name()
print("*"*10)
print(datafunction)

a, b = "sou", "faten"
# print(f"hello {a}")

# def   ->function keyword[define]


def say_hello(name):

    print(f"hello {name}")  # task


say_hello("a")  # sou is the argument
say_hello("b")  # b is the argument


def addition(n1, n2):
    if type(n1) != int or type(n2) != int:
        print("only integer allowed")
    else:
        print(n1 + n2)

    # print(int(n1)+int(n2))
addition(100, 200)


def full_name(first, middle, last):
    print(
        f"hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")
    print("hello {} {} {}".format(first, middle, last))
# strip() elliminer les espaces
# .1s: premier caractere


full_name("  sou  ", 'faten', "fat")
