# print("Hello")

# Data types
# Int - 234, 938, -1, -344, 0  
# Float - 19.22, 30.44, -9.3 
# String - 
# 'hello'
# "hello"
# "dont't"

# Bool - True (1) , False (0)

# output and print 
# print("Pradip")
# print(11, 21.33, True, 'ram')       # print multiple values

# by default print add new line (\n) at end. we can change it. 
# print("Python ", end="-")
# print("Tutorials")

# variables
# age = 24
# print(age)

# input
# num1 = int(input("Enter no :"))
# num2 = int(input("Enter no :"))

# print(num1 + num2)
# print("num1 is :", num1,"& num2:",num2)

# Arithmetic operation
# str1 = 6
# str2 = 3
# str3 = str1 // str2
# print(str3)


# strings and its methods
# str = "Hello"
# print(type(str))
# print(str)
# print("Hello" * 3)


# conditional statements
# x = "hello"
# y = 'hello'

# print(x == y)

# chained conditional 
# result = 7>3 < 8==8
# print(result)

# print( not False)

# if elif else

# x = 10
# if x == 10:
#     print("Equal")
# elif x > 10:
#     print("Greater")
# else:
#     print("Less")


# Collections: A collection is a data structure that groups multiple items  (elements) together 
#              so you can store, organize, and manipulate them as a single entity.
#              Instead of handling individual variables one by one, collections let you work with a whole bunch of values at once.
# Why collections
# 1. To store related data together. 
# 2. To perform operations like searching, sorting, or iterating over multiple items. 
# 3. To manage data efficiently in programs.

# In Python, common collection types include:
#--------------------------
# List: Ordered, Mutable(changeable sequence of elements), Duplicate allow.
# mylist = [4, True, "Apple", 10.77]
# print(len(mylist)) 
# mylist.reverse()
# print(mylist)

# mylist.clear()
# print(mylist)

# mylist.append(["Grape", "Laptop"])
# print(mylist) 

# mylist.extend(["Grape", "Laptop"])
# print(mylist)

# mylist.pop(0)
# print(mylist)
# var = mylist
# mylist[2] = "Citaphal"
# print(mylist)
# print(var)          # made modification to this variable which copies original list.



# ---------------------------------
# Tuple: Ordered, (Immutable)unchangeable sequence, Duplicates allow.
# x = (0, "Gulab", 2, False, 8, 2)

# print(x.index("Gulab"))
# print(x.count(2))

# ----------------------------------
# Set: Unordered, mutable,  No duplicates.
# x = set()       # Define empty set
# unique = {2, 10, 40, 2, 500, 225, 40}

# unique.add(88)
# unique.remove(40)           # remove specific elemet from set eg.40
# unique.pop()                # pop any arbitrary element, not specific.
# unique.update([55, 66])     # add element from other list, set, tuple, etc
# unique.clear()
# print(unique)

# s2 = {111, 2, 10,  333}
# merged = unique.union(s2)
# print(merged)
# intestn = unique.intersection(s2)
# print(intestn)
# copied = unique.copy()
# copied.add(77)                # create deep copy.
# print(copied)
# print(unique)

# print( 500 in unique)


# ---------------------------------
# Dictionary: Key-value pairs for  mapping data.
#             Keys are unique. 
#             Values can be any data type.
#             unordered 
#             Keys must be immutable types (e.g., strings, numbers, tuples).
# x = {'key': 4}
# x['key'] = 10       # update
# x['key2'] = 13      # add key
# x[2] = True
# x[3] = ["small", "medium", "big"]

# x[4] = False
# del x[4]            # delete

# print(x)
# print(x.values())
# print(x.keys()) 
# print('key2' in x)

# for key in x:
#     print(key, x[key])

# for key, value in x.items():
#     print(key , value , end="\n")


 
# -----------------------------------
# LOOPS:
# for i in range(1, 10, 2):         # range(start, stop, range)
#     print(i , end=" ")

# for i in ["Red", "Green", "Blue", "Yellow"]:
#     print(i, end=" ")

# x = [10, 20, 30, 40, 50]

# for i in range(len(x)):
#     print(x[i] , end=" ")

# i = 0
# while i <= 20:
#     if(i==10):
#         i += 1
#         continue
#     if(i>=15):
#         break
#     print(i , end=" ") 
#     i += 1


# ----------------------------
# Slice Operator [start:stop:step] - slice operator in Python is a powerful way to extract parts (subsets) 
#                                   of sequences like lists, tuples, strings, etc.

# lst = [10, 20, 30, 40, 50, 60, 70]

# ele = lst[ : ]            #print all
# ele = lst[ : : 1] 
# ele = lst[ : : 2]
# ele = lst[2: 6: 1]
#ele = lst[ : : -1]         #reverse 
# print(ele)


# sliced = (1, 2, 3, 4, 5, 6, 7, 8)[:]
# print(sliced)




#-------------------------------
# comprehensions
# x = [x for x in range(5)]
# x = [(x+100) for x in range(5)]
# x = [0 for x in range(5)]

# x = [['*' for j in range(10)] for x in range(5)]          #create 5 nested list which contain 10 '*' in each list.

# x = [i for i in range(100) if i % 5 == 0]                 #print list which contain element which divisible by 5.

# x = ["even" if x%2==0 else "odd"  for x in range(10) ]  

# x = [ (x, y)  for x in range(3)   for y in range(2)]      #nested lists

# x = { (x)**2  for x in [1, -1, 2, -2, 2] }

# x = {key_expr:value_expr   for x in iterable}             #syntax for dictionary
# def value_exp(x):
#     print(x)
#     if(x>=0 and x<=3):
#         return "Small"
#     elif (x>=4 and x<=7):
#         return "Medium"
#     else:
#         return "Big"
# x = { x:value_exp(x)  for x in range(10)}

# x = { x: x**2   for x in range(1, 5)}
# x = { x: x**2   for x in range(10) if x%2==0}

# print(x)

# Generator Comprehension:  It returns a generator, which generates items lazily (on demand), so it’s memory efficient.
# gen = (x**2 for x in range(5))  
# for val in gen:
#     print(val)

# pairs = [(x, y, "even") if (x + y) % 2 == 0 else (x, y, "odd")
#          for x in range(3) for y in range(3)]
# print(pairs)




#---------------------------------
# Function 

# def geek(a = 10, b = 20):                   #default values set for parameters
    # print("Inside geek")          
    # print(a, b, sep="-:-")                # sep in print
    # print(f"num1 : {a} and num2 : {b}")   # format variables
    # print("num1 = {} and num2 = {}".format(a, b))
    # return a+b

# result = geek(44, 66)
# print(result)
# result2 = geek()
# print(result2)


# def srq_cube_qaude(a):
#     return a**2, a**3, a**4         # return multiple value. This values return as TUPLE.

# mylist = srq_cube_qaude(2)
# print(mylist)
# print(type(mylist))
# sqrt, cube, quade = srq_cube_qaude(2)
# print(sqrt)
# print(cube)
# print(quade)

# -->*args and **kwargs                     # arguments  &  keyword arguments
# def func(*args, **kwargs):
#     print(sum(args))
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# func(1, 2, 3, a=4, b=5)

 
#-->Anonymous function (Lambda function): one line function
# y = lambda x : x + 5
# print(y(10))

# z = lambda x, y: pow(x, y)
# print(z(2, 4))

#-->Nested function
# def  func(x):
#     def func2():
#         print(x)
    
#     func2()             # here func2() is called inside func() method

# func(55)


#-->Closures: Same like nested function, here instead of calling, we return the inner function.
# def  func(x):
#     def func2():
#         print(x)
    
#     return func2            # here func2 return without () paranthesis.

# # func(77)()
# y = func(55)
# y()



#--->Decorator functions


#---->unpacking 
# def summation(*args):
#     return sum(args)
# a = [1, 44, 88, 233, 876]

# print(*a)
# print(summation(*a))            # first unpack it from list, and in summation function again pack it.


# map : modify whole list element. It return same length map as provided. It actually return value.
# x = [2, 5, 8, 19, 32, 48, 52, 59, 78, 83]

# mp = map(lambda i: i * 10, x)
# print(list(mp))


# filter : segregate/seperate elements from list. Return list may or may not be same. It actually return true/false.
# x = [2, 5, 8, 19, 32, 48, 52, 59, 78, 83]

# flt = filter(lambda i : i % 2==0, x)
# print(list(flt))

