# Write a program to find out whether a student is pass or fail ,
# # if it requires total 40% and at least 33% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.

m1 = int(input("Enter marks one"))
m2 = int(input("Enter marks two"))
m3 = int(input("Enter marks three"))


if(m1<33 or m2<33 or m3<33):
    print("You are fail because you have less than 33% in one of the subjects")

elif(m1+m2+m3)/3 <40:
    print("You are fail due to less total percentage")

else:
    print("Congratulations! You passed the exam")