import os 
import re 
import shutil


def imagesegregation() :
        for image in files :
            format_pattern_jpg = '.jpg$'
            format_pattern_png = '.png$'
            format_pattern_gif = '.gif$' 
            
            res_jpg = re.findall(format_pattern_jpg,image)
            res_png = re.findall(format_pattern_png,image)
            res_gif = re.findall(format_pattern_gif,image)
            print(image)
            if res_jpg  :
                src = image
                des = r"J:\\py_ex\\filesegregration\\testDestinationDB\\jpg"
                shutil.copy2(image,des)
                print(("1 --- {} moved  to des").format(image))
            if res_png :
                src = image
                des = r"J:\\py_ex\\filesegregration\\testDestinationDB\\png\\"
                shutil.copy2(image,des)
                print(("2--- {} moved to {}").format(image,des))
            if res_gif  :
                src = image
                des = r"J:\\py_ex\\filesegregration\\testDestinationDB\\gif\\"
                shutil.copy2(image,des)
                print(("3 --- {} moved  to des").format(image))

def ifdir() :
    pwd = os.getcwd()
    cdToDir = os.chdir("{}\\{}}\\").format(pwd,fileORfolder)
    for i in os.listdir() :
        if os.path.isfile(i) :
            imagesegregation()
        if os.path.isdir(i) :
            ifdir()
            
        
        
while True :
    print(("PWD ---- {}").format(os.getcwd()))
    cd = os.chdir(r"J:\\py_ex\\filesegregration\\testImageDB")
    print(("PWD ---- {}").format(os.getcwd()))
    files = os.listdir()
    ifdir()
            



