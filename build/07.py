import os
import sys
import re
import shutil

#fuction to find current dir 
def pwd() :
    currentDir = os.getcwd()
    return currentDir
#function to change dir path & print the path
def cd(x) :
    changeDir = os.chdir(x)
    return pwd()
#function to listDir  
def ls() :
    return os.listdir(pwd())



def imagesegregation() :
        for content in contents :
            format_pattern_jpg = '.jpg$'
            format_pattern_png = '.png$'
            format_pattern_gif = '.gif$' 
            
            res_jpg = re.findall(format_pattern_jpg,content)
            res_png = re.findall(format_pattern_png,content)
            res_gif = re.findall(format_pattern_gif,content)
            print(content)
            if res_jpg  :
                src = content
                des = r"J:\\py_ex\\filesegregration\\testDestinationDB\\jpg"
                shutil.copy2(content,des)
                print(("1 --- {} moved  to des").format(content))
            if res_png :
                src = content
                des = r"J:\\py_ex\\filesegregration\\testDestinationDB\\png\\"
                shutil.copy2(content,des)
                print(("2--- {} moved to {}").format(content,des))
            if res_gif  :
                src = content
                des = r"J:\\py_ex\\filesegregration\\testDestinationDB\\gif\\"
                shutil.copy2(content,des)
                print(("3 --- {} moved  to des").format(content))

                
# ##testing block
# path = "J:\\py_ex\\filesegregration\\testImageDB"
# print("pwd",pwd())
# print("path001",cd(path))
# print(ls())

path = "J:\\py_ex\\filesegregration\\testImageDB"

cd(path)
ls = ls()
for i in ls :
    if os.path.isdir(i) :
        print("this is folder",i)
    if os.path.isfile(i) :
        # print("this is a file ",i)
        cd(path)
        contents = os.listdir()
        imagesegregation()

        
        