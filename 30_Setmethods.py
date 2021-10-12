a=set()

a.add(9)
a.add(9)
a.add(9)
a.add(9)
a.add(9)
a.add(9)
a.add(9)
a.add(9)
a.add(9)
a.add(9)
a.add(7)
a.add(4)

print(a)


# a.add([9,8,7])
# # We cannot add list & dictionary in a set . Because both can be changed and updated.
# print(a)



a.add((73,38,93))
#We can add tuple in a set , as it cannot be changed and sets also.
print(a)

print(len(a)) # Prints the length of a set

a.remove((73,38,93)) #removes an element present in the set
#a.remove(99) #Throws an error present in the set



# b=set()
# b.add(882)
# b.add(3)
# b.add(9)
# b.add(6)
# b.add(7)
# b.add(13)
# b.add(2)
# print(b)

# print(b.pop())

# b.empty()
# print(b)


c=a.union({3,4,5,6}) # only works when assigned to different variable
print(c)


d = a.intersection({3,4,5,6})
print(d)
