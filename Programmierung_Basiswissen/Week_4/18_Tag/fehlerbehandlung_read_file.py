# FileNotFoundError

try:
    with open("vornamen.txt", "r") as aliasname:
        print(aliasname.read())
        print("The file has been read")
except FileNotFoundError:
    print("An exception occurred")
print("The program continues running!")

try:
    with open("protected.txt", "a") as aliasname:
       aliasname.write("\nNew content")
       print("Successful write operation")
except PermissionError:
    print("Permission denied: 'protected.txt'")
    