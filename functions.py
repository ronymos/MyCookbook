def greet_user():
    """Generic greeting for users"""
    print("Hello!")
    print("welcome")


def greet_user_by_name(name="user", greeting="Hello"):
    """Customized greeting for users"""
    print(greeting + ", " + name)


def cube(base_number):
    cubed_value = base_number * base_number * base_number
    return cubed_value

greet_user()
greet_user_by_name(input("What's your name? "))
greet_user_by_name()
greet_user_by_name("Rony", "wellcome")
greet_user_by_name(greeting="Wellcome", name="RONY")

eleven_cubed = cube(11)
print(eleven_cubed)
