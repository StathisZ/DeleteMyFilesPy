import os
import sys

folderPath = input("Paste or type the folder path: ")
fileExtension = input("Type the file extension you want to remove (i.e .txt): ")

filelist = os.listdir(folderPath)
if len(filelist) == 0:
    print("There are no files of that type in that folder.")
    sys.exit(0)

if len(filelist) > 0:
    fileNumber = 0
    typedList = []
    for file in filelist:
        if file.endswith(fileExtension):
            fileNumber = fileNumber + 1
            typedList.append(file)
    print("There are " + str(fileNumber) + " file(s) in the folder.")
    answer = input("Do you want to see the names of the files? y/n: ")
    if answer.lower().startswith("y"):
        print(typedList)
        answer1 = input("Do you want to delete those files? y/n: ")
        if answer1.lower().startswith("y"):
            for item in filelist:
                print("Deleting.......")
                if item.endswith(fileExtension):
                    os.remove(os.path.join(folderPath, item))
        elif answer1.lower().startswith("n"):
            print("Bye!")
            sys.exit(0)
    elif answer.lower().startswith("n"):
        answer1 = input("Do you want to delete those files? y/n: ")
        if answer1.lower().startswith("y"):
            for item in filelist:
                print("Deleting.......")
                if item.endswith(fileExtension):
                    os.remove(os.path.join(folderPath, item))
        elif answer1.lower().startswith("n"):
            print("Bye!")
            sys.exit(0)


newFolder = os.listdir(folderPath)
if len(newFolder) == 0:
    print("All Done!")
