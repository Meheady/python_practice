
#normal function

def add(x, y):
    return x+y

print(add(5, 10))


#lanbda function
#only return allowed in lambda function
#lambda function is an anonymous function


add_lambda = lambda a,b: a + b

print(add_lambda(5, 10))



students = [('Mehedi',50), ('Sakib', 80), ('Tamim', 70), ('Shakib', 90)]

sort_by_marks = sorted(students, key = lambda x:x[1], reverse=True)

print(sort_by_marks)


# practice map func

nums  = [1, 2, 3, 4, 5]

sum_nums = list(map(lambda a: a+a, nums))

print(sum_nums)

#filter function

marks_up_50 = list(filter(lambda x: x[1]> 50, students))

print(marks_up_50)

#reduce function

from functools import reduce

sum_of_marks = reduce(lambda x, y: x + y[1], students, 0)
## reduce takes a function, an iterable and an initial value
#

print(sum_of_marks)