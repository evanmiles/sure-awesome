#nameNumValue.py

# This program calculates the numeric value of a single name provided as input.

#Convert input to lowercase
name = input("Enter your full name: ").lower()
#Print a newline
print ()
#Use the sum function to compute sum of letters
print (sum(ord(ch) - 96 for ch in name)) 