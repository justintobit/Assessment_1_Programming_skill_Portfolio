# -*- coding: utf-8 -*-
"""
EX.3

Biography
"""

name=input('What is your name? ')
town=input('Where do you live? ')


try:#expects and accept if the input is a number
    age=int(input('What is your age? '))
except ValueError:
    print("Age must be a number")
    age= int(input('What is your age? '))
    
info={'name': name, 'age' : age, 'hometown': town}

print(f"Name is:{info['name']}\nAge is:{info['age']}\nHometown is in:{info['hometown']}")