#natSum.py

# This program finds the sum of the first n natural numbers, where the value of n is provided by the user.


n = int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1 = sum1 + n
    n = n - 1
print("The sum of first n natural numbers is", sum1)