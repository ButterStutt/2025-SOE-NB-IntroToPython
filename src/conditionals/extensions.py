print("Enter file")
file = input()

if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg") or file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("Application/pdf")
elif file.endswith(".txt"):
    print("text/txt")
elif file.endswith(".zip"):
    print("zipped up file into the archives")
else:
    print("application / octet - stream")
