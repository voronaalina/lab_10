import os
import shutil

new_dir="MY_PYTHON"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print("Каталог " + new_dir + " створено")
else:
    print("Каталог уже існує")

copy_of_files = ["c:/lab10/file1.txt", "c:/lab10/file2.txt", "c:/lab10/file3.txt"]
for file_name in copy_of_files:
    check_file = os.path.exists(file_name)
    if check_file:
        shutil.copy(file_name, new_dir)
        print("Файл " + file_name + " скопійовано в каталог " + new_dir)
    else:
        print("Такого файлу не існує")
