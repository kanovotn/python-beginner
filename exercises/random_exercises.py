import random
import secrets
import string
import time

# lottery
def lottery():
    lottery_ticket_list = []

    for i in range(100):
        lottery_ticket_list.append(random.randrange(1000000000, 9999999999))

    winning_tickets = random.sample(lottery_ticket_list, 2)
    return ", ".join(str(ticket) for ticket in winning_tickets)

# generate OTP
def generate_otp():
    secureGenerator = secrets.SystemRandom()
    return str(secureGenerator.randrange(100000, 999999))

# random character
def random_character():
    example_string = 'aldoeiyq820'
    return random.choice(example_string)

# random string of length 5 (uppercase and lowercase letters only)
def random_string():
    letters_list = string.ascii_letters
    random_string = ""
    for i in range(5):
        random_string += random.choice(letters_list)
    return random_string
    
""" Generate password, 
* 10 characters long 
* at least 2 upper case letters, 
* 1 digit, and 1 special symbol.
"""
def generate_password():
    characters_source = string.ascii_letters + string.digits + string.punctuation
    password = ""
    
    password = random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    
    for i in range(6):
        password += random.choice(characters_source)
    
    # To avoid predictability in the first 4 characters
    password_list = random.SystemRandom().shuffle(list(password))
    
    return "".join(password)
    
def multiply_random_float():
    number1 = random.uniform(0.1, 1.0)
    number2 = random.uniform(9.5, 99.5)
    return f'{number1} * {number2} = {number1*number2}'

# Generate random date between specified dates
def generateRandomDate(startDate, endDate, timeFormat):
    sTime = time.mktime(time.strptime(startDate, timeFormat))
    eTime = time.mktime(time.strptime(endDate, timeFormat))
    randomGenerator = random.random()
    
    randomTime = sTime + randomGenerator * (eTime - sTime)
    return time.strftime(timeFormat, time.localtime(randomTime))

# Dice same 5 times in a row
def reproducible_dice():
    dice = [1, 2, 3, 4, 5, 6]
    dice_result = ""
    for i in range(5):
        random.seed(32)
        dice_result += str(random.choice(dice))
    return dice_result
    

print("Two winning tickets are: ", lottery())
print("Random OTP is: ", generate_otp())
print("Random character is: ", random_character())
print("Random string of length 5: ", random_string())
print("Generated password: ", generate_password())
print("Multiplication of uniform numbers", multiply_random_float())
print("Random date between '1/1/2018', '12/12/2021':" , generateRandomDate('1/1/2018', '12/12/2021', '%m/%d/%Y'))
print("Reproducible dice: ", reproducible_dice())
