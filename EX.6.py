# -*- coding: utf-8 -*-
"""
EX.6
Brute Force Attacks
"""

pw= 1234
maxa=5
att=0


while att <maxa: # uses a while loop
    i=int(input("Enter password"))#assigns user input to variable i
    if i==pw:# using if-else statement, if i is equal to the password
        print("Password valid")
        break;
    else:# if the password is invalid
        maxa-=1#decrease by one the attempts 
        print("password invalid, you have", maxa, 'attempts left')



        

          

    
        
        
    
    

    

