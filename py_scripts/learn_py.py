'''

@author:	Gaurav Sood
@title:		Introduction to Python
@date:		4/10/2015

'''

# Single line comments in Python

# Get Started 
	# Command line:
		# Go to where python is installed. Type 'python'
	# IDLE
 		# go to Lib\idlelib
 
# Interactive Mode

# Begin
print "Hello John Smith!"

# Calculator
# ~~~~~~~~~~~~~~~~~~~
2+2
2*2

# Now some fun
17/5
type(17/5)
17/5.0
float(17)/5

# Explicit floor division
17 // 3.0

# Power
5 ** 2

# Complex calcs
5*2
10 + _

# _ remembers results from previous command

# Complex numbers
complex(1)

# Long Integers
type(10000000000)

# Bools
# ~~~~~~~~
type(1==1)
bool(0)


# Strings
# ~~~~~~~~~~~~~~~~~~~~~

# Use \ to escape '
print 'isn\'t'

Multiline strings
"""\
1. Convert to lower case
2. Take out special characters
3. Take out stop words
"""

print """\
1. Convert to lower case
2. Take out special characters
3. Take out stop words
"""

# Concatenation
('Data ' 'Science')
'Data ' + 'Science'

# Splitting
'Data Science'.split()

# Index
a_word = 'data'
a_word[0]
a_word[-1]
a_word[0:2] #  start is always included, and the end always excluded
a_word[:2] + a_word[2:]
len(a_word)

# Find
'Data Scienced'.find('a')
'Data Scienced'.find('a',2)
'Data Scienced'.rfind('a')

# Replace
'Data Scienced'.replace('d', '')

# Frequently used data types
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Tuples
# ~~~~~~~~~~~
# A tuple is a sequence of immutable Python objects.
tup0 = "a", "b", "c", "d";	

tup1 = ('J', 'F', 'M'); # Another way to initialize
tup1[0] = 1 # Can't change stuff inside it 

tup2 = (1, 2, 3, 4, '5');
type(tup2[4])
type(tup2[3])

len(tup1)
tup1*3
3 in tup2
max(tup1)

# Lists
# ~~~~~~~~~~~~~~~~
list1 = ['J', 'F', 'M'];
list2 = [1, 2, 3, 4, '5'];

list1[1] = 1
list1.append('A') # More efficient than insert
del list1[3]
list1.remove('J')
list1.pop()

# Count things up
list1.count('J')

len(list1)
list1*3
3 in list2
max(list1)

# List of Lists
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]

# Sets
# ~~~~~~~~~~~~~~
basket1 = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana'];
fruits1 = set(basket1);
basket2 = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana', 'guavas'];
fruits2 = set(basket2);
fruits2 - fruits1;

# Some useful functions
# But before we do that - functions
# Function
def add2(x):
	return x+2;

add2(2)

# filter
# filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true.
def f(x): return x % 3 == 0 or x % 5 == 0
filter(f, range(2, 25))

# map(function, sequence) calls function(item) for each of the sequence’s items and returns a list of the return values
map(add2, range(1, 11))

def addxy(x, y):
	return x +y;

map(addxy, range(1, 11), range(1, 11))

# reduce
# reduce(function, sequence) returns a single value constructed by calling the binary function function on the first two items of the sequence..
1+2+3+4+5+6+7+8+9+10
# Sum up 1 to 10
reduce(addxy, range(1, 11))

# Dicts
# ~~~~~~~~~~~~~~
dict1 = {'Name': 'Joe', 'Age': 27, 'Class': 'Data Science'};
dict1['Name'] = 'Liz'

# Delete
del dict1['Name']; # remove key/value with key 'Name'
dict1.clear();     # remove all entries in a dict
del dict1 ;		   # delete dict

dict1 = {}
dict1.update({'Name': 'Joe', 'Age': 27, 'Class': 'Data Science'});
dict1.keys()
dict1.values()

len(dict1)
dict1.has_key('Name')

# NumPy
# Windows: http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
# arrays, matrices

# Programming
# ~~~~~~~~~~~~~~~~~~~~
# http://pythontutor.com/

# Define variables
a_var = 1
no_var

# Coercion
str(10)
float(10)
type(10)
type(str(10))

# Duck Typing
def calculate(a, b, c): 
	print (a+b)*c;
calculate (1, 2, 3)
calculate ([1, 2, 3], [4, 5, 6], 2)
calculate ('apples ', 'and oranges, ', 3)

# If  
# Indent 
if a_var:
	print "yey!"

if a_var:
	print a_var

# If else
a = 1
if a > 5:
    print "This shouldn't happen."
else:
    print "This should happen."

# Loop
a = 0
while a < 10:
    a = a + 1
    print a

# For
for x in range(0,10):
	print x

for x in ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']:
	print x

dict1 = {}
dict1.update({'Name': 'Joe', 'Age': 27, 'Class': 'Data Science'});

for k in dict1:
	print k

for v in dict1.values():
	print v

for k, v in dict1.items():
	print k, v

# Since you will see this
list1 = ['J', 'F', 'M'];
[x.lower() for x in list1]

# Read and write from file
# ~~~~~~~~~~~~~~~~~~~~~~~~~~

# Read
import os

# set working directory
os.chdir("C:/Users/gaurav/Dropbox/learn/teach/DataScience/02_r_python/")
# open file
f = open("twinkle.txt", "r")
twinkle = f.read()
#f.readlines()
f.close()

# write

f = open("out.txt", "w") # f = open("out.txt", "a")
f.write(twinkle)
f.close()

# Install a package
	#   C:\Python27\python.exe ez_setup.py
	#	cmd: C:\Python27\python.exe -m easy_install BeautifulSoup4	

# Help
# ~~~~~~~~~~~
help()
help(tuple)
dir(tuple)