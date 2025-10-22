# -*- coding: utf-8 -*-
"""
EX.8

SIMPLE SEARCH  
"""

names=["Jake","Zac", "Ian", "Ron", "Sam", "Dave"]#stores the names in the list

search="SAM"#assigns the name to be searched

ui=input("input the names form" "Jake","Zac", "Ian", "Ron", "Sam", "Dave")#printing

if ui.casefold()=="sam":#if the user input is sam will print found
    print(f"{search} was found")
else:
    print("name is not found")