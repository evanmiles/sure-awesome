# futval.py

def main():
    #section1 question1
    print("This program calculates the future value of an investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    #section2 question1
    years = eval(input("Enter the number of years: "))
    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in", years, "years is:", "%.2f" % principal)

main()
#section1 question2
input("Press the any key to quit")