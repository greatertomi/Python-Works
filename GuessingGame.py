#Users Guess a number between 1 and 200
import random

value = random.randint(1,201)
userValue = int(input("Guess the number: "))

while value != userValue:
    if(value < userValue):
        userValue = int(input("Answer is too large. Guess again: "))
    else:
        userValue = int(input("Answer is too small. Guess again: "))

if(value == userValue):
    print("Congrats! You got the right number which is ",value)