# 1.8 Getting started with Data
# 19/09/2019

print(2+3*4)
print(5==10) # Relational operator
print((5 >= 1) and (5<= 10)) # Logical operator

print( """
 Table 1: Relational and Logical operators

         Operation Name   |  Operator
 -------------------------|-----------------
            less than     |       <
           greater than   |       >
      less than or equal  |      <=
    greater than or equal |      >=
             equal        |      ==
           not equal      |      !=
          logical and     |      and
          logical or      |       or
          logical not     |      not
""")
# Identifiers are used in programming as names. 
# A python variable is created when a name is used forthe first time
#   on the left-hand side of an assingment statement.
#   Assignment statements provide a way to associate a name with a value.
#   The variable will hold a reference to a piece of data and not the data itself

# 1.8.2 Built-in Collection Data types.
#   Lists, strings and tuples are ordered collecitons
#   Sets and dictonaries  are unordered collections

# A list is an ordered collections of zero or more references to Python data objects
# lists are written as comma-delimited enclosed in square brackets.
[1, 3, True, 6.5]
mylist = [1, 3, True, 6.5]
print("mylist :", mylist)

# Table 2: Operations on Any Sequence in Python
#
#   Operation name      |  Operator  |     Explanation
# ----------------------|------------|------------------------------
#      indexing         |     []     |  Access an element of a sequence
#   concatneation       |      +     |   Combining sequences together
#     repetition        |      *     | Concatenate a repeated number of times
#     memebership       |     in     | Ask whether an itme is in a sequence
#       length          |     len    | Ask the number of items in the sequence
#       slicing         |     [:]    | Extract a part of sequence. 

# Itialize a list
Initialize_myList = [0]*6
print('Initialize_myList :', Initialize_myList)

myList = [1, 2, 3, 4]
A = myList*3
A1 = [myList]*3 # It is a repetition of references to the data objects.
print('A :', A)
print('A1 :', A1)
myList[2] = 45
print('A :', A)
print('A1 :', A1)

# Table 3: Methods Provided by Lists in Python
#
#       Method Name     |       Use
#-----------------------|-----------------------------
#       append          |       alist.append(item)
#       insert          |       alist.insert(i, item)
#       pop             |       alist.pop()
#       pop             |       alist.pop(i)
#       sort            |       alist.sort()
#       reverse         |       alist.reverse()
#       del             |       del alist[i]
#       index           |       alist.index(item)
#       count           |       alist.count(item)
#       remove          |       alist.remvoe(item)

# dot notation for asking an object to invoke a method.

# range object repreesnt a sequence of integers.
# By default, it starts from zeor.

