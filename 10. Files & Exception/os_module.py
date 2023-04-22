import os 

print(os.name)

  
# Get the list of all files and directories 
# in the root directory 
path = "C:/xampp/htdocs/"
dir_list = os.listdir(path)
  
print("Files and directories in '" , path , "' :") 
  
# print the list 
print(dir_list) 

 

print(os.system("dir"))

print(os.getpid())

print(os.getcwd())

print(os.getcwdb())
