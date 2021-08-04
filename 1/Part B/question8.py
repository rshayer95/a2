# CREATE THE FILE 
newFile = open("./1/yourfullname.txt", "x")
newFile.close()
# NOW OPEN THE FILE
file = open("./1/yourfullname.txt", "a")
# APPEND THE CONTENT

file.write("This is first Line\n")
file.write("This is second Line\n")

# CLOSE THE FILE
file.close()

# OPEN THE FILE AGAIN WITH READ PROPERTY
file = open("./1/yourfullname.txt", "r")
print(file.read())

