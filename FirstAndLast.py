#Select the first and last elements of a list
#listed = [4, 2, 1, 7, 9, 12, 23, 15, 7]
print("Enter any amount of numbers seperated by space")
listed = [x for x in input().split()]

def selector(list):
    return listed[0], listed[len(listed)-1]

print(selector(listed))