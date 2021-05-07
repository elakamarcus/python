#!/bin/python3
import random

def getRandom():
    # return a random int between 0 and 10
    return random.randint(0, 10)

def askQuestion(a, b):
    # get user input, answer to the math question
    userResponse = int(input("What is {} - {}: ".format(a, b)))
    result = a - b
    # compare if user input is the same as the result
    if (userResponse != result):
        # if not right .. try again
        print("Try again!")
        askQuestion(a, b)
    else:
        # if correct, print encouraging message
        print("Great job!")

def main():
    # introduce success counter
    success = 0
    # run the program until 10 successful attempts
    while(success < 10):
        # Get two random numbers
        i = getRandom()
        j = getRandom()
        # Check which is the smaller, to avoid negative numbers, and pass to ask question function
        if i < j:
            askQuestion(j, i)
        elif j < i:
            askQuestion(i, j)
        # increment success counter
        success += 1

    print("Congratulation. All done!")

if __name__ == "__main__":
    main()