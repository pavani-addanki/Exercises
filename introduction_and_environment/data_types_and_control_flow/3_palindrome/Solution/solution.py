# Code your solution here

word = input('enter input string')
reverseString = word[::-1]

if word == reverseString:
    is_palindrome = True
else:
    is_palindrome = False

