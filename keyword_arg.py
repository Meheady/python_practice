
def my_func(fName, lName):
    print(f"Myn ame is {fName} {lName}")
    return f"{fName} {lName}"

result = my_func("Mehedi", "Hasan")

print("Full name:", result)




#def new_func(first, last):
def new_func(**kwargs):
    return kwargs
    print("First name:", first)
    print("Last name:", last)
    return f"{first} {last}"

data  = new_func(first="Mehedi", last="Hasan")
print("Full name with keyword args:", data)
