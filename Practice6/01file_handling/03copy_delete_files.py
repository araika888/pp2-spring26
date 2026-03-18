#1 
import os
if os.path.exists("2file.txt"):
    os.remove("2file.txt")
    print("Файл 2file.txt удален!")
else:
    print("The file does not exist!") 
#2 
import os
if os.path.exists("myfolder"):
    try:
        os.rmdir("myfolder")
        print("Пустая папка myfolder удалена!")
    except OSError:
        print("Папка myfolder существует, но не пустая!")
else:
    print("Папка myfolder не существует!") 

#3
import shutil
if os.path.exists("My second folder"):
    shutil.rmtree("My second folder")
    print("Папка My second folder со всем содержимым удалена!")
else:
    print("Папка My second folder не существует!")