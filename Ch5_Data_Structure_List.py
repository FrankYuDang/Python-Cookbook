# Python tutorial 5.1 More on List
# 16.09.2019 Frank

# list.append(x)
# a[len(a):] = [x]

# list.extend(iterable)
# a[len(a):] = iterable.
# Note: iterable measns you can step through the object as a collection.

# list.insert
# a.insert(0, x) - insert at the front of the list
# a.insert(len(a), x) - a.append(x)

# list.remove(x)
# Remove the 1st item from the list whose value is equal to x.

# list.pop([i])
# Remvoe the item at the given posion in the list, and return it.

# list.clear()
# Remove all the items from the list

# list.index(x[, start[, end]])
# ....

# list.count(x)
# Return the number of times x appears in the list

# list.sort(key = None, reverse = False)
# Sort the items of t he list in place.

# list.reverse()
# reverse the elements of the list in place.

# Insert, remove, sort that only modify the list have no return value printed.
fruits = ['oranges', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print('number of apple :', fruits.count('apple'))
print('index of banana :', fruits.index('banana'))
fruits.reverse
print(fruits)
fruits.sort()
print(fruits)

# 17/09/2019 - Using lists as Stacks
# Last in, first out.

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print('appended-twice stack :', stack)
stack.pop()
print('poped-once stack :', stack)
stack.pop()
print('poped-twice stack :', stack)

# Using lists as Queues.
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")         # Terry arrives
queue.append("Graham")
print("The first to arrive now leaves :", queue.popleft())
print("The second to arrive now leaves :", queue.popleft())
print("Remaining queue in order of arrival :", queue)

# 5.1.3 List comprehension
squares = []
for x in range(10):
    squares.append(x**2)
print("New squares :", squares)

# map() function - calculate the length of each word in the tuple
def myfunc(n):
    return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print("x :", list(x)) # print map() contents

squares = list(map(lambda x: x**2, range(10)))
print('sqaures created by map() :', squares)

squares = [x**2 for x in range(10)]
# A list comprehension consists of brackets containing an expression
# followed by a for clause, then zero or more for or if clause.
# THe result will be a new list resulting from evaluating the expression
# in the context of the for and if clauses which follow it.

a1 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print('a1 :', a1)
# It is equivalent to:
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print('combs :', combs)
print("-"*40)
# More list comprehension
vec = [-4, -2, 0, 2, 4]
# Create a new list with the values doubled
double_vec = [x**2 for x in vec]
print("double_vec :", double_vec)

# filter the list to exclude negative numbers
ex_neg_vec = [x for x in vec if x >= 0]
print("ex_neg_vec :", ex_neg_vec)

# apply a function to all the elements
func_vec = [ abs(x) for x in vec]
print("func_vec :", func_vec)

# call a method on each element
freshfruit = ['   banana', '          loganberry', 'Passion furit    ']
print("freshfruit :", freshfruit)
clean_space_freshfruit = [ weapon.strip() for weapon in freshfruit]
print('cleann_space_freshfruit :', clean_space_freshfruit)

# create a list of 2-tuples like (number, square)
num_sq_tuple = [(x, x**2) for x in range(6)]
print('num_sq_tuple :', num_sq_tuple)

# flatten a list using a listcomp with two for
matrix_vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('matrix_vec :', matrix_vec)
list_vec = [num for elem in matrix_vec for num in elem]
print('list_vec :', list_vec)

from math import pi
pi_string = [str(round(pi, i)) for i in range(1,6)]
print('pi_string :', pi_string)

print('-'*40)
print('5.1.4 Nested list comprehension')
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]
transpose_matrix = [[row[i] for row in matrix] for i in range(4)]
print('transpose_matrix_by_nested_list :', transpose_matrix)
row_matrix = []
transposed = []
for i in range(4):
    for row in matrix:
        transposed.append(row(i) for row in matrix)
        # print('i :', i)
        # print("row :", row)
        # print("row(i) :", row[i])
        # print("transposed :", transposed[:])
# is the same as
transposed = []
for i in range(4):
    # the following 3 lines implement nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print('tranposed :', transposed)

# In the real world.
zip_matrix = list(zip(*matrix))
# zip('ABCD', 'xy') --> Ax By
print('zip_matrix :', zip_matrix)

#----------------------------------
# 5.2 The del statement. 
# del can remove slices from a list or clear entire list
a = [-1, 1, 66.25, 333, 333, 1234.5]
print('a :', a)
del a[0]
print('a :', a)
del a[2:4]
print('a :', a)
del a[:]
print('a :', a)


#----------------------------------
# Tuples and sequence
t = 12345, 54321, 'hello!'
print('t[0] :', t[0])
print('t :', t)
# tuple can be nested:
nested_u = t, (1, 2, 3, 4 ,5)
print('nested_u :', nested_u)
print('Tuple is immutable, thus NO t[0] = 8888')

# Tuples vs Lists
print("""
Tuples are immutable and contain heterogenesou sequence of elements
    that are accessed via unpacking or indexing.
Lists are mutable, and their elements are usually homogeneous
    and accessed by iterating over the list""")

# Tuple has quirks when 0 or 1

print('# Sequence can be tuple packing and sequence unpacking')
#-------------------------------------
# 5.4. Sets.
# applications - membership testing and elminating duplicate entries.
# Curly braces or the set()

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)



        







