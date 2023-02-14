# ========================== os Module ==========================
# os => Operating System

import os
from datetime import datetime

# print(dir(os))

# os.getcwd() => get current working directory.

# E:\YouTube\Code\Python_Module
# E:\YouTube\Code\Python_Module

# print(os.getcwd())

os.chdir(r"E:\YouTube\Code")

# print(os.getcwd())

# print(os.listdir())
# print(os.listdir(os.listdir()[2]))

# os.mkdir("yehya_demo/inner_demo")
# os.makedirs("yehya_demo/inner_demo")

# os.rmdir("yehya_demo/inner_demo")
# os.removedirs("yehya_demo/inner_demo")

# os.rename("yehya.txt", 'alaa.txt')

# print(os.stat("alaa.txt"))
# print(os.stat("alaa.txt").st_size)
# mod_time = os.stat("alaa.txt").st_mtime

# print(datetime.fromtimestamp(mod_time))

# print(type(os.walk(r"E:\YouTube\Code")))

# for dir_path, dir_names, file_names in os.walk(r"E:\YouTube\Code"):
#     print("Current Path:", dir_path)
#     print("Directories:", dir_names)
#     print("Files:", file_names)
#     print("=" * 75)

# print(os.path.abspath(__file__))

# print(os.path.dirname(os.path.abspath(__file__)))

# print(dir(os.path))

# print(os.path.exists("yehya_demo/yehya.py"))