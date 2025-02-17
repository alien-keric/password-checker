#!/usr/bin/env python3
#author: alienkeric
import string
import getpass 
import time
from tqdm import tqdm

# README.md
'''
step 1: python -m venv passchecker
step 2: source passchecker/bin/activate
step 3: pip install tqdm
step 4: python checker.py
'''

# user input(hiden password)
password = getpass.getpass("Enter your password: ")
print("password received")
special_chars = set("!@#$%^&*()_+-={}[]:;'\"<>,.?/\\|`~")


## loading bar
for _ in tqdm(range(10), desc="Checking", ncols=75):
    time.sleep(0.2)

## password checker 
def checker(password):
    if len(password) > 10:
        if any(x.isupper() for x in password) and  any(x.islower() for x in password) and any(x.isdigit() for x in password) and any(char in special_chars for char in password):
               print("Your password is Strong", "🫡🥷👊👽")
        else:
               print("Your password is moderate", "🙊🙊🙊🙊")
    else:
        print("Your password is Weak", "😩😩🤣🤣")

#password = input("Enter your password")
checker(password)

## how to check the special character thing - didn't work but maybe need some more 
'''
To check whether the String consists of special characters, there are multiple ways, 
1. including using the Character class, 
2. regular expressions, or 
3. simple string checks. Example: 
In this example, we will use the Character. isLetterOrDigit() method that checks if a string consists of special characters
'''

## option two
'''
special_chars = set("!@#$%^&*()_+-={}[]:;'\"<>,.?/\\|`~")
any(char in special_chars for char in password)
'''
