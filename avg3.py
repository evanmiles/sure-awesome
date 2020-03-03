# avg3.py

def main():
    #section1 question1
    print("This program computes the average of three exam scores.")

    #section1 question3
    firstScore = eval(input("Enter the first exam score: "))
    secondScore = eval(input("Enter the second exam score: "))
    thirdScore = eval(input("Enter the third exam score: "))
    average = (firstScore + secondScore + thirdScore) / 3

    print("The average of the scores is:", round(average))

main()
#section1 question2
input("Press the any key to quit")