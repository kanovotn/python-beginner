import random
import string

def get_random_password(length):
    
    # random characters
    random_source = string.ascii_letters + string.digits + string.punctuation

    # select one from each category
    password = random.choice(string.ascii_lowercase)

    password += random.choice(string.ascii_uppercase)

    password += random.choice(string.digits)

    password += random.choice(string.punctuation)

    # generate the rest of the password
    for i in range(length - 4):
        password += random.choice(random_source)

    # shuffle password to avoid the predictability in the beginning of the password
    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    return password

def get_user_defined_password_length():

    while True:
        length_string = input("Enter the length of the password between 4-16: ")
        length = int(length_string)
        if length < 4 or length > 16:
            continue
        break
    return length

print("Random password: ", get_random_password(get_user_defined_password_length()))
