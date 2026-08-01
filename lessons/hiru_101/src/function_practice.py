def double_num(num):
    return num * 2

def get_user_name():
    return input("What's your name? ")

def get_user_age():
    return int(input("How old are you? "))

def welcome_user():
    user_name = get_user_name()
    print("Hello " + user_name + "!")
    user_age = get_user_age()
    print("You are " + str(user_age) + ". Welcome!")

