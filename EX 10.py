# -*- coding: utf-8 -*-
"""
EX.10

Is it even?
"""


def ev_odd(a):# function to check if the number is odd or even
    if a % 2 == 0:
        return f'the number {a} is even'# returns the the number is even
    else:
        return f'the number {a} is odd'# returns the the number is odd
    
         
#main function
def main():
    x=int(input("Enter Number: "))#gets user input and assign to variable x
    number=ev_odd(x)#assigned to number, calls the returned function and checks if number is odd or even
    print(number)# prints if the number is odd or even
main()#calls the function
  








