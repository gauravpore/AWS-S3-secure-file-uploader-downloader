from Delete import delete
from Download import download
from Upload import upload
from init import my_bucket

while True:
    print("Files in server: ")
    for file in my_bucket.objects.all():
        print(file.key)
    
    print("1. Upload file")
    print("2. Download file")
    print("3. Delete file")
    print("4. Quit.")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        upload(str(input("File name: ")), str(input("Object name: "))) #enter file path
    elif ch == 2:
        download(str(input("Object name: ")),str(input("Enter Path: ")))
    elif ch == 3:
        delete(str(input("Object name: ")))
    elif ch == 4:
        exit()
    else:
        print("Enter valid choice.")
