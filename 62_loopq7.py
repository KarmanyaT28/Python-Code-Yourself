# Write a program to print the following star pattern
#     *
#    ***
#   *****


n=5
for i in range(5):
    print(" " * (n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" " * (n-i-1))









