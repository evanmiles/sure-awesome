# convert.py
print("This is a program to convert Fahrenheit temps to Celsius")

def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature?: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("The temperature is", round(celsius), "degrees celsius.")

main()
input("Press the any key to quit")