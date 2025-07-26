
# file  = open('./python_practice/data.txt','r');

# content = file.read()
# print(content)

# file.close();


# with open ('./python_practice/data.txt','r') as file :
#     content = file.read();

# print(content)


#write in file

# with open ('data.txt','w') as file:
#     file.write('This is data one\n')
#     file.write('this is data  two\n')

# # append in file

# with open ('data.txt','a') as file:
#     file.write ('\nappend new line here one')
#     file.write ('\nappend new line here two')

# lines = ['Md Meheady hasan\n', '01568627574\n'];
# with  open('data.txt','a') as file:
#     file.writelines(lines);

import os

filePath = 'data.txt'

if os.path.exists(filePath):
    print('File exists')
else:
    print('File does not exist')
    

import pathlib

fileEx = pathlib.Path(filePath)

if fileEx.exists():
    print('File exists')
else:
    print('File does not exist')

# check if file is a file or directory

if fileEx.is_file():
    print('This is a file')
elif fileEx.is_dir():
    print('This is a directory')
else:
    print('Nothing found')


# get file size
fileSize = fileEx.stat().st_size
print(f'File size is {fileSize} bytes')