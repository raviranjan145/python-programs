#1. Write a Python program to create a tuple.

# x =()
# print(x)
# fruits = ("apple", "banana", "cherry")
# print(fruits[1])

#2. Write a Python program to create a tuple with different data types.
# diffdatatype = (1,'ram', 50.5,True)
# print(diffdatatype)

#3. Write a Python program to create a tuple with numbers and print one item.
# numbers= (1, 2, 3, 4, 5, 6, 11, 15)
# print(numbers)
# print(numbers[2])

#5.Write a Python program to add an item in a tuple.

# numbers= (1, 2, 3, 4, 5, 6, 11, 15)
# print(numbers)
#
# numbers = numbers +(9, )
# print(numbers)
#
# numbers = numbers[:5]+(21, 14, 7, ) +numbers[:5]
# print(numbers)

#6 write a python program to convert a tupple to string .
# tup = ('e','f', 'g', 'h')
# str = ''.join(tup)
# print(str)
# print(tup[len(tup)-2])
#7 write a python program to get the 4th element and 4th element from the last of the list .
# num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13)
# print(num[3])
# print(num)
# print(num[len(num)-4])

#8 write a python program to find the repeated iteam of a tupple .
# num = (1, 2, 3, 1, 10, 15, 18, 2, 2, 1, 1)
# print(num)
# count  = num.count(2)
# count1 = num.count(1)
# print(count)
# print(count1)

# 10 write a python program to check weather the element exits within a tupple
# num = (1, 2, 3, 1, 10, 15, 18, 2, 2, 1, 1)
# print(1 in num)
# print(11 in num)

# 11. Write a Python program to convert a list to a tuple

# num = [1, 2, 3, 1, 10, 15, 18, 2, 2, 1, 1]
#
# print(num)
#
# num = tuple(num)
# print(num)

# 13. Write a Python program to slice a tuple.
# tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
# #used tuple[start:stop] the start index is inclusive and the stop index
# slice = tuplex[3:5]
# #is exclusive
# print(slice)
# #if the start index isn't defined, is taken from the beg inning of the tuple
# slice = tuplex[:6]
# print(slice)
# #if the end index isn't defined, is taken until the end of the tuple
# slice = tuplex[5:]
# print(slice)
# #if neither is defined, returns the full tuple
# slice = tuplex[:]
# print(slice)
# #The indexes can be defined with negative values
# slice = tuplex[-8:-4]
# print(slice)
# #create another tuple
# tuplex = tuple("HELLO WORLD")
# print(tuplex)
# #step specify an increment between the elements to cut of the tuple
# #tuple[start:stop:step]
# slice = tuplex[2:9:2]
# print(slice)
# #returns a tuple with a jump every 3 items
# slice = tuplex[::3]
# print(slice)
# #when step is negative the jump is made back
# slice = tuplex[9:2:-4]
# print(slice)


#14 Write a Python program to find the index of an item of a tuple.

# num = (1, 2, 3, 4, 'ram', 'rohan', 5)
# print(num)
# index = num. index(5)
# print(index)


#15. Write a Python program to find the length of a tuple


# num = (1, 2, 3, 4, 'ram', 'rohan', 5)
# print(len(num))

#16. Write a Python program to convert a tuple to a dictionary.

# tuplex = ((2,'w'),(1,'a'))
# dict1 = {}
#
# for x,y in  tuplex:
#     dict1[x] = y
#
# print(dict1)



# 17. Write a Python program to unzip a list of tuples into individual lists.

# num = ((1, 2, 3, 4,) ,('ram', 'rohan', 5))
# print(list(zip(*num)))


#18. Write a Python program to reverse a tuple
# num = (1, 2, 3, 4, 'ram', 'rohan', 5)
# rev =reversed(num)
# print(tuple(rev))

# x = ("w3resource")
# # Reversed the tuple
# y = reversed(x)
# print(tuple(y))

# x = (5, 10, 15, 20)
# # Reversed the tuple
# y = reversed(x)
# print(tuple(y))

# 19. Write a Python program to convert a list of tuples into a dictionary.
#
#
# def Convert(tup, di):
#
#     for a, b in tup:
#         di.setdefault(a, []).append(b)
#     return di
#
# tup = [("akash", 10), ("gaurav", 12), ("anand", 14),
#      ("suraj", 20), ("akhil", 25), ("ashish", 30)]
#
# dicton = {}
#
# print(Convert(tup, dicton))

 # 20. Write a Python program to print a tuple with string formatting. Go to the editor
#Sample tuple : (100, 200, 300)
# Output : This is a tuple (100, 200, 300)

# num = (100, 200, 300)
# print(num)

# Write a Python program to replace last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# list2 =[]
# for i in list1:
#    k = list(i)
#    k[-1] = 100
#    list2.append(tuple(k))
#
# print(list2)

