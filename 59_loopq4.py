# Write a program to find whether a given number is prime or not
number=int(input("enter your number which has to be checked"))
# i=2
# for i in range(2,number):
#     if(number%i==0):
#         break

# print("Not a prime number")


prime = True

for i in range(2,number):
    if(number%i==0):
        prime=False
        break

if prime:
    print("Prime number")

else:
    print("not a prime bro")
