# 1) Multi-line statement

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)

colors = ['red',
          'blue',
          'green']

a = 1; b = 2; c = 3

# 2) Indentation
for i in range(1,11):
    print(i)
    if i == 5:
        break

if True:
    print('Hello')
    a = 5

if True: print('Hello'); a = 5

# 3) Comments

#This is a comment
#print out Hello
print('Hello')

# 3.1) Multi-line comments

#This is a long comment
#and it extends
#to multiple lines

"""This is also a
perfect example of
multi-line comments"""

# 4) Docstrings

def double(num):
    """Function to double the value"""
    return 2*num
print(double.__doc__)
