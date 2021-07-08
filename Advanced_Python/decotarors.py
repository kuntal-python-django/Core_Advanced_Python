''' Assign functions to variables '''
# def greet(name):
#     return "hello "+name

# greet_someone = greet
# print(greet_someone("Kuntal"))


''' Define functions inside other functions '''
# def greet(name):
#     def get_message():
#         return "Hello "
#     result = get_message() + name
#     return result

# print(greet("Kuntal"))


''' Functions can be passed as parameters to other functions '''
# def greet(name):
#    return "Hello " + name 

# def call_func(func):
#     other_name = "Kuntal"
#     return func(other_name)  

# print(call_func(greet))


''' Functions can return other functions '''
# def compose_greet_func():
#     def get_message():
#         return "Hello there!"

#     return get_message

# greet = compose_greet_func()
# print(greet())


# ------------------------------------------------------------------------------------------
''' Creating Decorators 1 '''
def uppercase_decorator(function):
    def wrapper():
        make_uppercase = function().upper()
        return make_uppercase
    return wrapper


''' Creating Decorators 2 '''
def split_string(function):
    def wrapper():
        splitted_string = function().split()
        return splitted_string
    return wrapper


''' Calling Decorators '''
# def say_hi():
#     return 'hello there'

# decorate = uppercase_decorator(say_hi)
# print(decorate())


''' Calling Decorators '''
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())

