# GET FIRST NUMBER
firstNumber = int(input("Enter first number: "))
# GET SECOND NUMBER
secondNumber = int(input("Enter second number :"))
# GET THIRD NUMBER
thirdNumber = int(input("Enter third number: "))

operator = str(input("Enter s to find small or g to find greatest number: "))

if operator == "s":
    if firstNumber == secondNumber and secondNumber == thirdNumber:
        print('Numbers are equal')
    elif firstNumber < secondNumber and firstNumber < thirdNumber:
        print(firstNumber, " is smallest among " , firstNumber , ", " , secondNumber , ", " , thirdNumber)
    elif secondNumber < firstNumber and secondNumber < thirdNumber:
        print(secondNumber, " is smallest among " , firstNumber , ", " , secondNumber , ", " , thirdNumber)
    elif thirdNumber < secondNumber and thirdNumber < firstNumber:
        print(thirdNumber, " is smallest among " , firstNumber , ", " , secondNumber , ", " , thirdNumber)

elif operator == "g":
    if firstNumber == secondNumber and secondNumber == thirdNumber:
        print('Numbers are equal')
    elif firstNumber > secondNumber and firstNumber > thirdNumber:
        print(firstNumber, " is greatest among " , firstNumber , ", " , secondNumber , ", " , thirdNumber)
    elif secondNumber > firstNumber and secondNumber > thirdNumber:
        print(secondNumber, " is greatest among " , firstNumber , ", " , secondNumber , ", " , thirdNumber)
    elif thirdNumber > secondNumber and thirdNumber > firstNumber:
        print(thirdNumber, " is greatest among " , firstNumber , ", " , secondNumber , ", " , thirdNumber)
else:
    print("Wrong Input, please try again")
