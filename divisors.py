#Print the list of all the divisors for a number the user gives and check if it is a prime number
number = int(input("Enter any number to find its divisors: "))
divisors = []
i = 1
while i <= (number):
    if(number%i == 0):
        divisors.append(i)
    i+=1

print(divisors)
if(len(divisors) <= 2):
    print("This kind of numbers are called prime numbers")