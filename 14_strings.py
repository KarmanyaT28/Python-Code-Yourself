# greeting = "Good Morning,"
# name = "Harry"
# print(type(name))


#----------------------------
# #Concatenating two strings
# c = greeting + name
# print(c)

#----------------------------

name = "Karmanya"
print(name[0])
print(name[4])


#----------------------------
# name[3] = "d" ----> String object does not support item assignment



#-----------String Slicing-----------------
print(name[0:3])
# 0 is included but 3 is not included.
# Same will be repeated in case of lists also.
# ---------------------------


print(name[:4])
# if left blank then 0 is taken by default
print(name[0:])
# if left blank then length of the string is taken by default


#--------Negative Indices-----------
c = name[-4:-1]


d = name[1:7:2]# with escape value of one
print(d)


