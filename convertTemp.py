# convertTemp.py

#section1 question1
print("This is a program to convert Fahrenheit temps to Celsius")

#section3 question1
def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature?: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("The temperature is", round(celsius), "degrees celsius.")

main()
#section1 question2
input("Press the any key to quit")