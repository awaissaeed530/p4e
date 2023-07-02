fname = input("Enter filename: ")
try:
    file = open(fname)
    print(file.read())
except:
    print("Error occurred while opening file")
    exit(-1)
