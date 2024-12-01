"""  Decorators in Python are a powerful tool for modifying the behavior of functions or methods without changing
their actual code. They allow for the implementation of higher-order functions,
which can take other functions as
arguments and return new functions. Decorators are widely used for logging, access control, memoization
, and more. """


def decorate_another_fun(fun):
    def innera_fun():
        print("I'm decorating you")
        fun()         ## this is simply fun = decorate_another_function(decorate_me)
        print("im decorating1")
    return innera_fun


@decorate_another_fun
def decorate_me():
    print("Thank you for decorating")


decorate_me()


# Define the decorator
def simple_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")

    return wrapper


# Use the decorator on a function
@simple_decorator
def say_hello():
    print("Hello!")


# Call the decorated function
say_hello()
