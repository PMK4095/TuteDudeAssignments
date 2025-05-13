try:
    print("Reading file content:\n")
    with open("sample.txt", 'r') as fileNew:
        readFileContent=fileNew.read()
        print(readFileContent)

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
finally:
    print("The program will now exit.")