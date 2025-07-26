
# file  = open('./python_practice/data.txt','r');

# content = file.read()
# print(content)

# file.close();


# with open ('./python_practice/data.txt','r') as file :
#     content = file.read();

# print(content)


#write in file

with open ('data.txt','w') as file:
    file.write('This is data one\n')
    file.write('this is data  two\n')

# append in file

with open ('data.txt','a') as file:
    file.write ('\nappend new line here one')
    file.write ('\nappend new line here two')

lines = ['Md Meheady hasan\n', '01568627574\n'];
with  open('data.txt','a') as file:
    file.writelines(lines);
