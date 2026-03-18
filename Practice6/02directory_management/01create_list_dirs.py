#1 getcwd показывает где я
import os
print("1.where am i?")
current=os.getcwd()
print(current)
#2 listdir показывает что внутри
print("2.what's in current folder?")
items=os.listdir(".")
for item in items:
    print(" ->",item)
#3 mkdir создает папку
print("creating new folder where name is 'task1' ")
os.mkdir("task1")
print("Folder task1 created!")
#4 makedir создает папку внутри папки
print("creating nested filders a/b/c")
os.makedirs("a/b/c",exist_ok=True)
print("Folders a/b/c created!")
#5
print("let's see what wee have now:")
for item in os.listdir("."):
    if os.path.isdir(item):
        print("  folder",item)
    else:
        print("  file",item)