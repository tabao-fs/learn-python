# 1) Variables
number = 10
number = 1.1

# 2) Assigning values to Variables

# 2.1) Declaring and assigning value to a variable
website = "apple.com"
print(website)

# 2.2) Changing the value of a variable
website = "apple.com"
print(website)

# assigning a new value to website
website = "programiz.com"

print(website)

# 2.3) Assigning multiple values to multiple variables
a, b, c = 5, 3.2, "Hello"

print (a)
print (b)
print (c)

x = y = z = "same"

print (x)
print (y)
print (z)

# 3) Constants
# 3.1) Assigning value to constant
PI = 3.14
GRAVITY = 9.8

print(PI)
print(GRAVITY)

# 4) Literals
# 4.1) Numeric Literals
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

# 4.2) String literals
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# 4.3) Boolean literals
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# 4.3) Special literals
drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)

# 4.4) Literal Collections
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)
