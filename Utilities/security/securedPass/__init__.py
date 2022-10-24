# script to generate a Random Password
from secrets import choice
from string import (ascii_letters, digits, punctuation)


def pin(pin_lenght):  # Function to generate a pin password, parameter pin_leng is int to decide the size of the pin
    pin_range = '1234567890'
    pin_choice = ''.join(choice(pin_range) for _ in range(int(pin_lenght)))
    return pin_choice


def password(password_lenght, ponctuation = False):
    # Function to generate a password with letters and digits, and ponctuations if necessary
    if ponctuation == True:  # if poncution equals to True, letters going to have ponctuation
        letters = ascii_letters + digits + punctuation
    else:  # else letters going to have only letters and digits
        letters = ascii_letters + digits
    password_choice = ''.join(choice(letters) for _ in range(password_lenght)) # concatenate the letters to creat a password
    return password_choice

