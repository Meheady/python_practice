a = [1,2,3, "a",4,5,6]

for item in a:
    if type(item) == str:
        #break stop the loop if item is string
        continue # skip the rest of the loop for this iteration

    else:
        print(item)
