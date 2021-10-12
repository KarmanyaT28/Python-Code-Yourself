# Write a program to print the multiplication table of given number using for loop

number = int(input("Tell me the number to calculate multiplication table"))
i=1
for i in range(11):
    # print(number*i)
    # print(str(number) + "X" + str(i) + "=" +str(number*i))
    print(f"{number}X{i}={number*i}")

print("Table completed")
