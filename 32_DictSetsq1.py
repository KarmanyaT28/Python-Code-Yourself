# Write a program to create a dictionary of hindi words with values as their english translation>provide user
# with an option to look it up!

Hindidict={
    "Namaste":"a greeting",
    "Acha":"Good",
    "Bura":"Bad",
    "Sahi":"Right",
    "Galat":"Wrong",
    "Waqt":"Time",
    "Padhai Karo":"Study",
}
print("The options are",Hindidict.keys())
a = input("Enter the word\n")
# print("The meaning of your word is:",Hindidict[a])

#below line will not throw an error if the key is not present
print("The meaning of your word is:",Hindidict.get(a))


