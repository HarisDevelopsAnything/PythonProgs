from zipfile import *
import os
print("1) Zip specific files 2) Zip all files in dir 3) Unzip files 4) Exit")
ch= int(input("Enter your choice: "))
if ch==1:
    nzip= input("Name of zip file?: ")
    file= ZipFile(nzip, 'w', ZIP_DEFLATED)
    while True:
        name= input("Enter file name (or enter to finish): ")
        if os.path.isfile(name):
            file.write(name)
            print(f"Added {name} to archive.")
        elif name=='':
            print("Archive created.")
            break
        else:
            print("File not found!")
elif ch==2:
    nzip= input("Name of zip file?: ")
    file= ZipFile(nzip, 'w', ZIP_DEFLATED)
    list= os.listdir(".")
    for i in list:
        file.write(i)
    print("Archived all files in directory.")
elif ch==3:
    nzip= input("Name of zip file?: ")
    if os.path.isfile(nzip):
        file= ZipFile(nzip, 'r', ZIP_STORED)
    else:
        print("No such archive!")
        exit(0)
    try:
        d= input("Enter the directory to extract to: ")
        file.extractall(path=d)
        print("Extracted.")
    except:
        print("Permission/IO Error occurred.")
else:
    print("Exiting.")
