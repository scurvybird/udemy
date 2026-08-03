import os

#os.mkdir("new_folder")
#creates a new directory called "new_folder" in the directory this program is run in (in this case: lessons/hiru_101/src)

if os.path.exists("README.md"):
    print("OK")
else:
    print("not OK")
