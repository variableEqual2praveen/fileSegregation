import os
import sys
import re
import shutil
def imageSegregration() :  
    
    format_pattern_jpg = '.jpg$'
    format_pattern_png = '.png$'
    format_pattern_gif = '.gif$' 
    format_pattern_mp4 = '.mp4$'
    format_pattern_py = '.py$'
     
    res_jpg = re.findall(format_pattern_jpg,filePath)
    res_png = re.findall(format_pattern_png,filePath)
    res_gif = re.findall(format_pattern_gif,filePath)
    res_mp4 = re.findall(format_pattern_mp4,filePath)
    res_py = re.findall(format_pattern_py,filePath)
    if res_jpg  :
        src = filePath
        des = r"K:\\realme_phone bachup_dec29_2019\\segregation\\jpg\\"
        shutil.copy2(filePath,des)
        print(("1 --- {} moved  to des").format(filePath))
    if res_png :
        src = filePath
        des = r"K:\\realme_phone bachup_dec29_2019\\segregation\\png\\"
        shutil.copy2(filePath,des)
        print(("2--- {} moved to {}").format(filePath,des))
    if res_gif  :
        src = filePath
        des = r"K:\\realme_phone bachup_dec29_2019\\segregation\\gif\\"
        shutil.copy2(filePath,des)
        print(("3 --- {} moved  to des").format(filePath))
    if res_mp4  :
        src = filePath
        des = r"K:\\realme_phone bachup_dec29_2019\\segregation\\videos\\"
        shutil.copy2(filePath,des)
        print(("3 --- {} moved  to des").format(filePath))
    if res_mp4  :
        src = filePath
        des = r"K:\\realme_phone bachup_dec29_2019\\segregation\\py\\"
        shutil.copy2(filePath,des)
        print(("3 --- {} moved  to des").format(filePath))
    

path =  "K:\\realme_phone bachup_dec29_2019\\"

for root,dirs,files in os.walk(path) :
    for file in files :
        filePath = os.path.join(root,file)
        # print(filePath)
        imageSegregration()
    

        
