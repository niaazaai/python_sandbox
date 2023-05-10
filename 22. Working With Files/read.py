from pathlib import Path

script_location = Path(__file__).absolute().parent
file = open(f'{script_location}/file.txt' , 'r')

content = file.read()
print(content)
file.close()


# content_read_lines = file.readline()
# for lines in content_read_lines:
#     print(lines)
