# Unpacking a sequence into separate variables
# Sep, 15, 2019

p = (4, 5)
x, y = p
print('x = ', x)
print('y = ', y)

data = [ 'ACME', 50, 91.1, (2012, 12, 21)]
name, share, price, date = data
print('name :', name)
print('data :', date)

name, shares, price, (year, mon, day) = data
print('name :', name)
print('year :', year)

p = (4, 5)
x, y, z = p
