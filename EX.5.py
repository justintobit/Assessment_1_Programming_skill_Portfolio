# -*- coding: utf-8 -*-
"""
EX.5
Days of the Month 
"""
#name stores and assigns number to a month in dictionary
name={1:'January',
        2:'Febuary',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'Decmeber'
        }

#this stores and assigns number to a number of days in a month in dictionary
ofdays={1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
        }
number=int(input("Input month number: "))#asks for user input

if number==2: #if the input number is 2 asks if it is a leap year
    leap=input("is this month a leap year? ")
    if leap.casefold() =="yes":#if the user input is yes
        ofdays[2]=29 #changes the the value of 2 from 28 to 29 in ofdays dictionary 
        print("number of days in Month", name[number], "is", ofdays[number], "days in a Leap year")
    else:
        print("number of days in Month", name[number], "is 28", "days in a Leap year")

state=number in name# to assign and check the input number to corresponding number in the dictionary

if state==True:# if the input is number
    print("number of days in Month", name[number], "is", ofdays[number],"days")
else:# if the number input is higher than 12 or lower than 1
    print("Inalid number")
            

        

    


    
    

