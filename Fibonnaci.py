#Allow users to generate a particular amount of fibonnaci numbers
value = int(input("How many fibonacci numbers do you want to generate: "))
fibonnaci = [1,1]
for i in range(2,value):
    fibonnaci.append(fibonnaci[i-2] + fibonnaci[i-1])

print(fibonnaci)