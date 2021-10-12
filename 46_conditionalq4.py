# Write a program to find whether a given username contains less than 10 characters or not.


username=input("Enter your username")

length=len(username)

if(length<10):
    print("Characters are less than 10")

else:
    print("Characters more than 10")