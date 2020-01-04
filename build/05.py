import os 
import re 
import shutil
pwd = os.getcwd()
cd = os.chdir(r"J:\\py_ex\\filesegregration\\testImageDB\\")
pwd = os.getcwd()
print("pwd",pwd)


def dirORfile() :
    pwd = os.getcwd()
    ls = os.listdir()
    # print(ls)
    for content in ls :
        # print("debug01")
        if content is os.path.isfile(pwd) :
            imagesegregation()
            print(content)
        if content is os.path.isdir(pwd) :
            cd = os.chdir(content)
            print(content)
            

dirORfile()