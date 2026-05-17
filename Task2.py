# a mode is used to create a non-existing file and write data to it. If the file already exists, it will be overwritten.
with open("output.txt","at") as fh:
    # using user input to append data and write to the file
    fh.write(input("Enter text to write to the file : "))
    print("Data successfully written to output.txt")
    fh.write("\n")
    fh.write(input("Enter additional text to append : "))
    print("Data successfully appended.")
# reading the content of the file and printing it to the console
with open("output.txt","rt") as fh :
    content = fh.read()
    print(f"Final content of output.txt : {content}")     