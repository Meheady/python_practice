
a = [1, 2, 3, 4, 5, 6]

i = 0
while i < len(a):
    if a[i] % 2 == 0:
        a[i] = a[i] ** 2
    i += 1

print(a)

b = [1, 2, 3, 4, 5, 6];

j = 0;

sum = 0

while j < len(b):
    sum += b[j]
    j += 1

print("Sum of elements in b:", sum)  