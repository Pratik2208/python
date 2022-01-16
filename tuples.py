"""
    Student ID = 20CE069
    STUDENT NAME = panchal pratik Arvindbhai
    a. Write a Python program to create a tuple with different data types.

    b. Write a Python program to create a tuple with numbers and print one item.

    c. Write a Python program to add an item in a tuple.

    d. Write a Python program to convert a tuple to a string.

    e. Write a Python program to find the length of a tuple.



                    GITHUB REPORSITORY LINK = https://github.com/Pratik2208/python.git

"""

# A. Write a python program to create a tuple with different data types.

tuple1 = (23 ,43,54,32,35)
tuple2 = ("Hello", "Python")
print(tuple1)
print(tuple2)

# B. Write a python program to create a tuple with numbers and print one item.

tuple = (1,2,3,4,5,6,7)
print(tuple[5])

# C. Write a python program to add an item in a tuple

tuple = (2 , 4,5,7,9)
tuple = tuple + (10,12,18)
print(tuple)

# D. Write a python program to convert a tuple with to a string

tuple = ('P','R','A','T','I','K')
str = ''.join(tuple)
print(str)

# E. Write a program to find the length of the tuple


tuple = ('J','A','Y')
print("Length of the tuple:", len(tuple))