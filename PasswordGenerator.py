#Generate random characters with different levels of difficulty.
import random

list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#print(*list3, sep='')
#print(list1[random.randint(0,26)])
def generateEasy():
    password = []
    for i in range(6):
        choose = random.randint(1,2)
        #print(choose)
        if(choose == 1):
            password.append(list1[random.randint(0,26)])
        elif(choose == 2):
            password.append(list2[random.randint(0, 26)])
    print("Your Password is ", *password, sep='')

def generateMedium():
    password = []
    for i in range(9):
        choose = random.randint(1,3)
        #print(choose)
        if(choose == 1):
            password.append(list1[random.randint(0,26)])
        elif(choose == 2):
            password.append(list2[random.randint(0, 26)])
        else:
            password.append(list3[random.randint(0, 9)])
    print("Your Password is ", *password, sep='')

def generateHard():
    password = []
    for i in range(15):
        choose = random.randint(1,3)
        #print(choose)
        if(choose == 1):
            password.append(list1[random.randint(0,26)])
        elif(choose == 2):
            password.append(list2[random.randint(0, 26)])
        else:
            password.append(list3[random.randint(0, 9)])
    print("Your Password is ", *password, sep='')

level = int(input("Enter the password difficulty level, from 1 to 3: "))
try:
    if level == 1:
        generateEasy()
    elif level == 2:
        generateMedium()
    elif level == 3:
        generateHard()
except:
    print("An error occured. Please try again")