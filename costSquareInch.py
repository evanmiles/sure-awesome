#costSquareInch.py

# This program calculates the cost per square inch of circular pizza, given it's diameter and price.

# Create two functions(besides the main function):
 # - One to compute the Area of the pizza
 # - One to compute Cost per Square Inch. 
    
# The main function calls the Area function, that function calls the Cost per Square Inch function,
# a value is returned to the Area function and that value is returned to the main function for printing

# The formula for area is:
# A = pi * r^2

import math

def pizzaArea():
  diameter = int(input('What is the diameter of the whole pizza in inches? '))
  radius = diameter / 2
  area = math.pi * radius ** 2
  return area
  
def costPerInch():
  
  area = pizzaArea()
  price = float(input("What is the price of the pizza? "))
  total = price / area
  return total
  
def main():

    ans = costPerInch()
    print("The cost per square inch is $ %.2f" % ans)
    
main()