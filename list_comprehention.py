a = [1, 2, 3, 4, 5, 6];

result = [];

for i in a:
    if i % 2 == 0:
        result.append(i);

#print(result);

newResult = [j for j in a if j % 2 == 0];

print(newResult);

b_new =  [l**2 if l % 2 == 0 else l  for l in a ]

print(b_new);