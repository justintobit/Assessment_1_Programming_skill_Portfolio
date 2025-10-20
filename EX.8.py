# -*- coding: utf-8 -*-
"""
EX.8

SIMPLE SEARCH  
"""

names=["Jake","Zac", "Ian", "Ron", "Sam", "Dave"]

search="SAM"

ui=input("input the names form" "Jake","Zac", "Ian", "Ron", "Sam", "Dave")

if ui.casefold()=="sam":
    print(f"{search} was found")
else:
    print("name is not found")