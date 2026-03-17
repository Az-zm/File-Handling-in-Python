try :
    with open("sample.txt","wt") as fh:
        fh.write("This is a sample text file.\nIt contains multiple lines.")
    with open("sample.txt","rt") as fh:
        Line1 = fh.readline()
        Line2 = fh.readline()
        print(f"Reading File Content:\nLine1 : {Line1}Line2 : {Line2}")
except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found.")