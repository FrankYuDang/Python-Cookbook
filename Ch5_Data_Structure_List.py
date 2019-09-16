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

