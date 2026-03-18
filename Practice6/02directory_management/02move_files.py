#1
import shutil
with open("file1.txt","w") as f:
    f.write("Hello world! My name is Kanat")
shutil.move("file1.txt","file_moved.txt")
print("Done!")
#2
import shutil
with open("original.txt","w") as f:
    f.write("Hello!")
shutil.copy2("original.txt","copy.txt")
print("It's correctly copy and pass!")
#3
import shutil
import os
with open("test.txt","w") as f:
    f.write("KBTU is university in central asia")
os.mkdir("myfolder")

shutil.move("test.txt","myfolder/")
print("Donee!!!")
#4
import shutil
import os
with open("data.txt","w") as f:
    f.write("It's my new data of file")
os.mkdir("backup")

shutil.copy2("data.txt","backup/")
print("Copy is done!")
#5
import os
print(os.listdir("."))
