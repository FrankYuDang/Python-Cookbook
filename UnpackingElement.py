# Unpacking elements from iterables of Arbitrary Lenth
# Sep, 16, 2019

# Star expression can be used to unpack N elements from an iterable.

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

user_record = ('Dave', 'dave@example.com','773-555-12112', '847-555-1212')
name, email, *phone_numbers = user_record
print("name :", name)
print("phone_numbers", phone_numbers) # phone_numbers is a list.

# Extract the first 7 numbers and stack up to the current one.
def compare_current(sales_record):
    *trailing_qtrs, current_qtr = sales_record
    trailing_avg = sum(trailing_qrts) / len(trailing_qrts)
    return avg_comparison(trailing_avg, current_qtr)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print('trailing :', trailing)
print('current :', current)

# Extended iterable unpacking is for unpacking iterables of unknown or arbitrary length.
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# Star unpacking can also be useful when combined with
# string processing operations, such as spliting.
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/fasle'
uname, *fields, homedir, sh = line.split(':')
print('uname :', uname)
print('homedir :', homedir)
print('sh :', sh)

# Unpack and throw them away
# a common throwaway variable name, such as _ or ign (ignored)
record = ( 'ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print('name :', name)
print('year :', year)

# star unpacking similar to list-processing features.
# split function
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print('head :', head)
print('tail :', tail)

        

    






