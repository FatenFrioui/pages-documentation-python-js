# function => lambda
# anonymous function: it has no name
# you can call it inline without defening it
# you can use it in return data from another function
# lambda used for simple functions and def handle the large tasks
# lambda is one single expression not block of Code
# lambda type is function
#-----------------------------------------------------------------------------------------------------

def say_hello(name,age) : return f"hello {name}, your age is {age}"

hello=lambda name,age : f"hello {name}, your age is {age}"

print(say_hello("Faten",37))
print("*"*10)
print(hello("Faten",37))

# function name
print(say_hello.__name__)   # say_hello
print(hello.__name__)       # <lambda>

print(type(hello))          # <class 'function'>