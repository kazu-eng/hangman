#### The Self-Taught Programmer
## Part-III, Challenge

# No1 print
print("<<Challenge 3-1>>")

print("Hello, Japan!")
print("Learn Python")
print("Let's get started")


# No2 if-else (comparison operator)
print("<<Challenge 3-2>>")

a = 5
b = 11
if (a<10):
    print("a is smaller than 10")
else:
    print("a is NOT smaller than 10")
if (b<10):
    print("b is smaller than 10")
else:
    print("b is NOT smaller than 10")


# No3 if-elif-else
print("<<Challenge 3-3>>")

c = 30

if (a<=10):
    print("a is smaller than or equal to 10")
elif (a<=25):
    print("a is greater than 10, and smaller than 25 and equal")
else:
    print("a is greater than 25")
    
if (b<=10):
    print("b is smaller than 10 and equal")
elif (b<=25):
    print("b is greater than 10, and smaller than or equal to 25")
else:
    print("b is greater than 25")
    
if (c<=10):
    print("c is smaller than or equal to 10")
elif (c<=25):
    print("c is greater than 10, and smaller than or equal to 25")
else:
    print("c is greater than 25")
    
# No4 % () remainder
print("<<Challenge 3-4>>")

print("a%b =", a%b)
print("b%c =", b%c)
print("c%a =", c%a)

# No5 / () division
print("<<Challenge 3-5>>")

print("a/b =", a/b)
print("b/c =", b/c)
print("c/a =", c/a)

# No6 input
print("<<Challenge 3-6>>")

age = input("Input your age ")
age = int(age)  # cast with 'int' because 'input' in 'str'

if (age < 20):
    print("You are young")
elif (age < 35):
    print("You are not old")
else:
    print("Sorry to ask about that")
    


