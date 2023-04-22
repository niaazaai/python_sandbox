# from pathlib  import Path 

# import json 

# # json file to store the python list 
# data = [ 1,2,34,45,66,78,99,7,6,22,5,4,333,3,223123,213,123]
# content = json.dumps(data); 
# path = Path('./10. Files & Error Handling/file.json')
# path.write_text(content)


# # to get the data back from the file we use json module 

# path = Path('./10. Files & Error Handling/file.json')
# content  = path.read_text()

# json_content = json.loads(content); 

# print(json_content)

# for value in json_content:
#     print(value)
    





from pathlib import Path 
import json 

script_location = Path(__file__).absolute().parent
file_location = script_location / 'list.json'
print(file_location)



# to write json data to file or store the data structure in a file 
list = ["apple", "tenetur", "minima" , "adipisicing", "consectetur" , "impedit" , "mollitia" , "voluptas"]
path = Path(file_location)
content = json.dumps(list)
path.write_text(content)


# to get the data back from .json file we can do as follow 
read_content = path.read_text(); 
read_content = json.loads(read_content)
# print(read_content)

for item in read_content:
    print(f":::> {item}")

    
    
