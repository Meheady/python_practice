
a = [1, 2, "Mehedi", 3.14, True, None]

print(a[0])  # Accessing the first element
a[0] = "Changed"  # Modifying the first element
print(a)

print(a[-1])  # Accessing the last element
print(len(a))
a.append("add new element")  # Adding a new element
print(a)

print(a.index(1))

print(a.count(55))

print(a[1:3])

print(a[-4:-2])

b = [1, 2, "Mehedi", 3.14, True, None, None]

if "TTT" in b:
    print("TTT is in the list")
else:
    print("TTT is not in the list")

b.remove(None)

#b.pop(0) # Removes the first element
#b.pop()  # Removes the last element
#del b[0]  # Deletes the first element
#b.clear()  # Clears the list

# for x in b:
#     print(x)

# for f in range(len(b)):
#     print(b[f])

# [print(y) for y in b if y != "Mehedi"]

print(b.reverse)