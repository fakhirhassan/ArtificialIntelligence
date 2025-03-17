# import random
# randomNumber = random.randint(1,9)
# def guessNumber():
#     game = True
#     tries = 3
#     while game:
#         guess = int(input("enter the number"))
#         if guess == randomNumber:
#             print("you are right")
#             tries -= 1
#             game = False

#         elif guess < randomNumber:
#             print("number is too low")
#             tries -= 1
#         elif guess > randomNumber:
#             print("number is too high")
#             tries -= 1
#         else:
#             print("you are wrong")
#             tries -= 1
#         if tries == 0:
#             print("you are out of tries")
#             game = False
# guessNumber()

# #LABTASK1

# number = int(input("Enter a number to reverse: "))
# reversedNumber = 0

# while number > 0:
#     digit = number % 10
#     reversedNumber = (reversedNumber * 10) + digit
#     number = number // 10

# print("Reversed number is:", reversedNumber)

# LABTASK2
# number = int(input("Enter an integer: "))
# evenSum = 0
# oddSum = 0

# while number > 0:
#     digit = number % 10
#     if digit % 2 == 0:
#         evenSum += digit
#     else:
#         oddSum += digit
#     number = number // 10

# print("Sum of even digits:", evenSum)
# print("Sum of odd digits:", oddSum)

# #LABTASK3

number = int(input("Enter the number up to which to generate Fibonacci series: "))
a = 0
b = 1
c = 0 
count = 0
while count  < number:
    print(a, end=" ")
    c = a + b  
    a = b         
    b = c      
    count +=1    

print()

# LABTASK4
# marks = int(input("Enter the marks: "))
# if marks >= 91:
#     print("A")
# elif marks >= 81:
#     print("B")
# elif marks >= 71:
#     print("C")
# elif marks >= 61:
#     print("D")
# elif marks >= 51:
#     print("E")
# else:
#     print("F")

# #LABTASK5

# number = int(input("Enter a number: "))
# if number > 0:
#     factorial = 1
#     for i in range(1, number + 1):
#         factorial *= i
#     print("Factorial of", number, "is:", factorial)
# else:
#     print("Please enter a positive number")


