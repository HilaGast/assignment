# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 11:24:30 2018

@author: hila
"""

def check_palindrome():
   """
   Runs through all 6-digit numbers and checks the mentioned conditions.
   The function prints out the numbers that satisfy this condition. 
   
   Note: It should print out the first number (with a palindrome in its last 4 digits), 
   not all 4 "versions" of it.
   """
   results=[]
   for i in range(100000, 1000000-3):
       start_number=str(i)
       last_4_digits=start_number[2:]
       start_number_plus1=str(i+1)
       last_5_digits=start_number_plus1[1:]
       start_number_plus2=str(i+2)
       middle_4_digits=start_number_plus2[1:5]
       final_number=str(i+3)
       if is_palindrome(last_4_digits) and is_palindrome(last_5_digits) and is_palindrome(middle_4_digits) and is_palindrome(final_number):
           results.append(i)
   return(results)

def is_palindrome(number):
    """
    Checks whether a string number is a palindrome and return a boolean result 
    """
    return(number[:]==number[::-1])       

if __name__ == '__main__':
    result2=check_palindrome()
    print('Question 2 solution: ' + str(result2))