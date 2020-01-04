import os 

pwd = os.getcwd()
print("currentworking",pwd)
cd =  os.chdir(r"J:\\py_ex\\filesegregration\\testImageDB\\testpy")
pwd = os.getcwd()
print("currentworking",pwd)

ls = os.listdir()
for i in ls :
    
    if i is os.path.isdir() :
        print(i)

cd = os.chdir(r"01\\")
pwd = os.getcwd()
print("currentworking",pwd)
