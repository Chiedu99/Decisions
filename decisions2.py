# Chiedu Nduka-Eze
# 10/5/16
# Decisions option one
# This code creates a game that prompts you to answer math problem using multiplication, addition, or subtraction
import random


def getMaxNumber():
    """This function prompts the user for the max number"""
    maxNumber = int(input("what is the maximum number that you want:"))
    return maxNumber


def chooseProblem():
    """This function prompts the user for the type of problem"""
    problemType = input("Do you want +, -, or *?:")
    return problemType


def randomNumber(maxNumber):
    """this function calculates random numbers for the problem"""
    return random.randint(1, maxNumber)


def showProblem(randomNumberOne, randomNumberTwo, problemType):
    """"This function shows the problem"""
    print(randomNumberOne, problemType, randomNumberTwo)


def correctAnswer(randomNumberOne, randomNumberTwo, problemType):
    """this function calculates the maximum number"""
    if problemType == "*":
        return randomNumberOne * randomNumberTwo
    elif problemType == "-":
        return randomNumberOne - randomNumberTwo
    else:
        return randomNumberOne + randomNumberTwo


def getAnswer():
    """This function gets the users answer"""
    return int(input("What is your answer:"))


def rightOrWrong(playerAnswer, realAnswer):
    """This funtion tells the user if they are write or wrong"""
    if realAnswer != playerAnswer:
        return print("You are incorrect! try again!")
    else:
        return print("You are correct! Play again!")


def main():
    print("Hello, welcome to chiedu's math quiz")
    maxNumber = getMaxNumber()
    problemType = chooseProblem()
    randomNumberOne = randomNumber(maxNumber)
    randomNumberTwo = randomNumber(maxNumber)
    showProblem(randomNumberOne, randomNumberTwo, problemType)
    playerAnswer = getAnswer()
    realAnswer = correctAnswer(randomNumberOne, randomNumberTwo, problemType)
    rightOrWrong(playerAnswer, realAnswer)


main()
