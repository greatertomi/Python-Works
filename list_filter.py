#Print numbers in a list less than any number the user gives
nums = []
final = []
print("Enter any amount of numbers seperated by space")
nums = [int(x) for x in input().split()]
benchmark = int(input("Select a number you want to print less than: "))
final = [x for x in nums if x < benchmark]
print("Initial list: ",nums)
print("Final list: ",final)
