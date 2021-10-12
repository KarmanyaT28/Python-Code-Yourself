# name = input("Enter your name\n")
# print("Good afternoon, " + name)


# ---------------------------------------------------------------------------

# Write a program to fill in a letter template given below
# letter = '''Dear <Name> , you are selected ! <DATE>'''

# letter = '''
# Greetings from TalkPy.org
# Dear <|NAME|>,
# You are selected !
# Date : <|DATE|>

# With regards
# '''
# name = input("Enter your name\n")
# date = input("Enter date\n")
# letter = letter.replace("<|NAME|>",name)
# letter = letter.replace("<|DATE|>",date)

# print(letter)


#-------------------------------------------------------------------------
# Write a program to detect double spaces in a string without using conditional statements

st = "A string with  double    spaces"

doubleSpaces = st.find("  ")
print(doubleSpaces)


#-----------------------------------------------------------------------
#Replacing the double space with single spaces
st = st.replace("  "," ")
print(st)
