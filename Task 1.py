try :
    with open("sample.txt","rt") as fh:
        # Here we are using readline() instead of read() to read the content line by line. 
        Line1 = fh.readline()
        Line2 = fh.readline()
        print(f"Reading File Content:\nLine1 : {Line1}Line2 : {Line2}")
# This except block will be executed if the file 'sample.txt' doesn't exist. 
except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found.")