#List out numbers that are common on both lines of code
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = []

'''for i in a:
    for j in b:
        if(i == j):
            common.append(i)'''
#List Comprehension
common = [x for x in a for y in b if x==y]

#To remove duplicates
common = list(dict.fromkeys(common))
print(common)