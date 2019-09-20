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

# Strings are sequential collections of zero or more characters.
# Literal string values are differenticated from identifiers
#   by using quotation marks.

myName = 'David'
print('myName[3] :', myName[3])
print(myName*2)
print(myName.upper())
print(myName.center(10))
print(myName.find('v'))
print(myName.split('v'))
print(myName.ljust(3))
print(myName.ljust(6))
print(myName.rjust(6))

# Table 4: Methods Provided by String in Python
#
#       Method Name     |       Explanation
#-----------------------|------------------------
#   astring.cener(w)    |   Returns a string centerred in a field of size w
#   astring.count(w)    |   Returns the number of occurrences of item in the string.
#   astring.lower()     |   Returns a string in all lowercase.
#   astring.find(item)  |   Returns the index of the first occurrence of item
#   astring.split(schar)|   Split a string into substring at achar

# String is immutable, but list is muttable.
# Tuple is immutable.
# Tuples are written as comma-delimited values enclosed in parentheses.

myTuple = (2, True, 4.96)
print(myTuple)
len(myTuple)
print('myTuple[0] :', myTuple[0])
print(myTuple * 3)
print('myTuple[0:2] :', myTuple[0:2])

# A set is an unordered collection of zero or more immutable Python data objects.
# A set is written as comma-delimited values enclosed in curly braces.

mySet = {3, 4, "cat", 4.5, False}
print('mySet :', mySet)

# Table 5: Operations in a Set in Python
#
# Operation Name| Operator          | Explanation
#---------------|--------------------------------------
#   membership  | in                | Set membership
#   length      | len               | Returns the cardinality of the set
#   |           | aset              | otherset | Returns a new set with all elements for mboth sets
#   &           | ast & otherset    | Returns a new set with only those elements common to both
#   -           | aset - otherset   | Returns a new set with all items from the first set not in sect
#   <=          | aset <= otherset  | Asks whether all elements of the first set are in 2nd

mySet = {False, 4.5, 3, 6, 'cat'}
yourSet = {99, 3, 100}

print('-'*40)
print('*'*10, 'set example','*'*10)
print('aset.union(otherset) :', mySet.union(yourSet))
print('aset | otherset :', mySet | yourSet)
print('aset.intersection(otherset) :', mySet.intersection(yourSet))
print('aset & otherset :', mySet & yourSet)
print('aset.difference(otherset) :', mySet.difference(yourSet))
print('aset - otherset :', mySet - yourSet)
print('Ask whether all in {3,100}.issubset:', {3,100}.issubset(yourSet))
print('Ask whether all in {3,100} <= yourset :', {3,100} <= yourSet)
print('Add element in a set .add :', mySet.add("house")) # unordered
print('remove an element :', mySet.remove(4.5))
print('Pop an arbitrary element :', mySet.pop())








