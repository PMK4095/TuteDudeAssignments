#Write and Append Data to a File
try:
    with open("output.txt","w") as file:
        input1=file.write(input("Enter text to write to the file: "))
        print("Data successfully written to output.txt.\n")

    with open("output.txt","a") as file:
        input2=file.write(input("Enter additional text to append: "))
        print("Data successfully appended.\n")

    with open("output.txt", "r") as file:
        print("Final content of output.txt:")
        readOutput=file.read()
        print(readOutput)

except FileNotFoundError:
    print("File does not exist.")
