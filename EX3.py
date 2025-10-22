# -*- coding: utf-8 -*-
"""
EX.3

Biography
"""

name=input('What is your name? ')
town=input('Where do you live? ')


try:#expects and accept if the input is a number
    age=int(input('What is your age? '))
except ValueError:#if the number is not number will run this conditon
    print("Age must be a number")
    age= int(input('What is your age? '))
    
info={'name': name, 'age' : age, 'hometown': town}#stores and assigns the user input 

print(f"Name is:{info['name']}\nAge is:{info['age']}\nHometown is in:{info['hometown']}")#Prints the user input