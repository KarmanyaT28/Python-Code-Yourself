# Write a program to calculate the factorial of a given number using for loop

i=1
prod=1
n=int(input("Enter the number"))
for i in range(1,n+1):
    prod=prod*i
    i=i+1

print(f"The factorial of this number is {prod}")