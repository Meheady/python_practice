a = [1, 2, 3, 4, 5]

for item in a:
    print(item)

for i in range(len(a)):
    print(f"index {i}: {a[i]}")

for j in range(1, 50):
    if j % 2 == 0:
        print(f"{j} is even")
    else:
        print(f"{j} is odd ")