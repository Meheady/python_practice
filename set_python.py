
#unorderd
#immutable
#not duplicated

my_set = {1, 2, 3, 4, 5, 5,2}

s = set(my_set)
print("Set:", s)

#union and intersection

a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8]

c = set(a).intersection(b) #retrun only common
d = set(a).union(b) #return all elements


print("Union of a and b:", d)

print("Intersection of a and b:", c)