#Prints Words in reverse
word = input("Enter a word: ")
lister = word.split()

i = len(lister)-1
while i >= 0:
    print(lister[i], end = " ")
    i -= 1
