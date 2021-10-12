# is an unordered collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element,
myDict = {
    "Fast": " In a quick manner",
    "TalkPy" : "A community",
    "Marks":[1,2,3,4],
    "AnotherDict": {'karmanya': 'Coder'},
    3:7
}
# A collection of key-value pairs.

# print(myDict['Fast'])
# print(myDict['TalkPy'])
# print(myDict['Marks'])

print(myDict['AnotherDict']['karmanya'])


# Properties
'''1. It is unordered
2. It is mutable
3. It is indexed
4. Cannot contain duplicate keys'''



#MUTABLE
myDict['Marks'] = [26,38,48]
print(myDict['Marks'])


#methods
print(myDict.keys()) #Prints the keys of the dictionary
print(myDict.values()) #Prints the values of keys of the dictionary
print(myDict.items()) # Prints the (key,value) for all contents in the dictionary
print(myDict)



updateDict = {
    "Lovish" : "Friend",
    "Divya":"Friend",
    "Shubah":"Best Friend",
    "Karan" : "Normal friend"
}

myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)


print(myDict.get("Karan")) #Prints value associated with key "Karan"
print(myDict["Karan"]) #Also prints the value associated with key "Karan"


print(myDict.get("kjkf")) # Returns none as kjkf is not present in the dictionary
# print(myDict["kjkf"]) # throws an error as kjkf is not present in the dictionary




print("Some checking done-----------------------------------------------------------")

NewDict = {"All":"good","All":"dheuhd"}
print(NewDict)
print(NewDict["All"])
print(NewDict.get("All"))
#Only prints the new value of the key.
# This shows that a dictionary cannot contains same keys in it. It will update the value of that key if used in future.


print(type(myDict))