
# file  = open('./python_practice/data.txt','r');

# content = file.read()
# print(content)

# file.close();


with open ('./python_practice/data.txt','r') as file :
    content = file.read();

print(content)