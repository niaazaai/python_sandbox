from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'pi_digits.txt'
print(file_location)


# path = Path(file_location)
# contents = path.read_text().rstrip()
# print(contents)



# path = Path(file_location)
# contents = path.read_text()

# lines  = contents.splitlines()

# line_str = ''
# for line in lines : 
#     # line_str = f" <:: {line} ::> "
#     line_str += line.strip()

# print(line_str)
# print(len(line_str))

 

# path = Path(file_location)
# contents = path.read_text()

# lines  = contents.splitlines()

# line_str = ''
# for line in lines : 
#     # line_str = f" <:: {line} ::> "
#     line_str += line.strip()


# print(line_str)

# birth = input(":::::::> ")
# if birth in line_str: 
#     print("Your Birth day is appears in the pi " )
# else:
#     print("Your Birth day is not appears in the pi") 




write_path = Path(f"{script_location}/programming_text.txt")
write_path.write_text('Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio, impedit. \nOdit voluptas in voluptates mollitia, \nearum dignissimos minima consequatur tenetur a, \nblanditiis sed ipsam beatae necessitatibus aut maxime! Quod, sunt.')
 

string_apply = ''
list_to_file = ["apple", "tenetur", "minima" , "adipisicing", "consectetur" , "impedit" , "mollitia" , "voluptas"]

write_path1 = Path(f"{script_location}/python_list.txt")

string_apply += '[ '
pos = -1

for   element in list_to_file :
    pos += 1

    string_apply += element
    if pos == len(list_to_file) - 1:
        continue
    string_apply += ' , '

string_apply += ' ] '
write_path1.write_text(string_apply)
    