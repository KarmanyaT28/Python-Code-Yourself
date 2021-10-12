f = open('sample.txt','r')

# data = f.read()
data = f.read(5) # reads first five characters from the file.
print(data)
f.close()

# Modes of opening a file
# r - Open for reading
# w - Open for writing
# a - open for appending
# + - open for updating


# rb will open for read in binary mode
# rt will open for read in text mode 




