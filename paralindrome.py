#Check if entered word is a paralindrome

value = input("Enter a word: ")

lastIndex = len(value) - 1
vLength = int(len(value)/2)
i = 0;
isPara = False
for i in range(vLength):
    if(value[i]== value[lastIndex-i]):
        isPara = True
    else:
        isPara = False
        break;

if(isPara == True):
    print("This word is a parlindrome")
else:
    print("This word is not a parlindrome")