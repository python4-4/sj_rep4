Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> sample_list1=['eggs','butter','flour', 'bread','cheese']
>>> sample_list1
['eggs', 'butter', 'flour', 'bread', 'cheese']
>>> sample_list2 = list([1, 'drink', 10, 'sandwiches', 0.45e-2])
>>> sample_list2
[1, 'drink', 10, 'sandwiches', 0.0045]
>>> sample_list1, sample_list2
(['eggs', 'butter', 'flour', 'bread', 'cheese'], [1, 'drink', 10, 'sandwiches', 0.0045])
>>> sample_list1[0]
'eggs'
>>> sample_list1[1]
'butter'
>>> sample_list1[0]+''sample_list1[1]
SyntaxError: invalid syntax
>>> sample_list1[0]+''+sample_list1[1]
'eggsbutter'
>>> sample_list1[1:3]
['butter', 'flour']
>>> sample_list2[1:3]
['drink', 10]
>>> numbers = list(range(10))
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> numbers[2:5]
[2, 3, 4]
>>> numbers[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> numbers[::2]
[0, 2, 4, 6, 8]
>>> numbers * 2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> numbers + sample_list2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 'drink', 10, 'sandwiches', 0.0045]
>>> sample_list3 = [1, 2, 3, ['a', 'b', 'c'], ['Hello', 'Python']]
>>> sample_list3
[1, 2, 3, ['a', 'b', 'c'], ['Hello', 'Python']]
>>> sample_list3[3][1]
'b'
>>> sample_list3.append(' '.join(sample_list3[4]))
>>> sample_list3
[1, 2, 3, ['a', 'b', 'c'], ['Hello', 'Python'], 'Hello Python']
>>> sample_list3[4]
['Hello', 'Python']
>>> sample_list3.pop(3)
['a', 'b', 'c']
\
>>>  sample_list3.pop(2)
 
  File "<pyshell#25>", line 2
    sample_list3.pop(2)
    ^
IndentationError: unexpected indent
>>> sample_list3.pop(2)
3
>>> sample_list3
[1, 2, ['Hello', 'Python'], 'Hello Python']
>>> sample_list3.pop(2)
['Hello', 'Python']
>>> sample_list3
[1, 2, 'Hello Python']
>>> ample_list3.insert(2, 3)

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    ample_list3.insert(2, 3)
NameError: name 'ample_list3' is not defined
>>> sample_list3.insert(2, 3)
>>> sample_list3
[1, 2, 3, 'Hello Python']
>>> sample_list3.insert(3, ['a', 'b', 'c'])
>>> sample_list3
[1, 2, 3, ['a', 'b', 'c'], 'Hello Python']
>>> list1 = [1, 1, 2, 3, 5, 5, 7, 9, 1]
>>> list1
[1, 1, 2, 3, 5, 5, 7, 9, 1]
>>> set1 = set(list1)
>>> set1
set([1, 2, 3, 5, 7, 9])
>>> 1 in set1
True
>>> 100 in set 1
SyntaxError: invalid syntax
>>> 100 in set1
False
>>> set1 = {1, 2, 3, 5, 7}
>>> set2 = {5, 7, 11}
>>> set1 | set2
set([1, 2, 3, 5, 7, 11])
>>> set1 & set2
set([5, 7])
>>> set1 - set2
set([1, 2, 3])
>>> set1 ^ set2
set([1, 2, 3, 11])
>>> dic1 = {1:'egg', 2:'ham', 3: 'milk'}
>>> dic1
{1: 'egg', 2: 'ham', 3: 'milk'}
>>> dic1[3]
'milk'
\
>>> dic1 = {1:'egg', 2:'ham', 3: 'milk', 4:'egg'}
>>> dic1
{1: 'egg', 2: 'ham', 3: 'milk', 4: 'egg'}
>>> dic1 = {1:'egg', 2:'ham', 3: 'milk', 4:'egg', 3:'cheese'}
>>> dic1
{1: 'egg', 2: 'ham', 3: 'cheese', 4: 'egg'}
>>> dic1.get(5)
>>> dic1[5]

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    dic1[5]
KeyError: 5
>>> dic1.get(5)
>>> dic1.get(2)
'ham'
>>> printMyDepartment

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    printMyDepartment
NameError: name 'printMyDepartment' is not defined
>>> 
================= RESTART: C:/Users/user/Desktop/multiply.py =================
>>> intMultiplier(3,5)

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    intMultiplier(3,5)
  File "C:/Users/user/Desktop/multiply.py", line 2, in intMultiplier
    for multiplier in range(intiNum,lastNum+1):
NameError: global name 'intiNum' is not defined
>>> 
================= RESTART: C:/Users/user/Desktop/multiply.py =================
>>> intMultiplier(3,5)
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
==============================
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
==============================
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
==============================
>>> intMultiplier(11,15)
11 x 1 = 11
11 x 2 = 22
11 x 3 = 33
11 x 4 = 44
11 x 5 = 55
11 x 6 = 66
11 x 7 = 77
11 x 8 = 88
11 x 9 = 99
==============================
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
==============================
13 x 1 = 13
13 x 2 = 26
13 x 3 = 39
13 x 4 = 52
13 x 5 = 65
13 x 6 = 78
13 x 7 = 91
13 x 8 = 104
13 x 9 = 117
==============================
14 x 1 = 14
14 x 2 = 28
14 x 3 = 42
14 x 4 = 56
14 x 5 = 70
14 x 6 = 84
14 x 7 = 98
14 x 8 = 112
14 x 9 = 126
==============================
15 x 1 = 15
15 x 2 = 30
15 x 3 = 45
15 x 4 = 60
15 x 5 = 75
15 x 6 = 90
15 x 7 = 105
15 x 8 = 120
15 x 9 = 135
==============================
>>> 
================ RESTART: C:\Users\user\Desktop\department.py ================
>>> printMyDepartment()
Sejong University
English Literature

>>> printMyDepartment()
Sejong University
English Literature

>>> printMyDepartment()
Sejong University
English Literature

>>> printMyDepartment()printMyDepartment()printMyDepartment()printMyDepartment()
SyntaxError: invalid syntax
>>> printMyDepartment()
Sejong University
English Literature

>>> printMyDepartment()
Sejong University
English Literature

>>> printMyDepartment()
Sejong University
English Literature

>>> printMyDepartment()
Sejong University
English Literature

>>> printMyDepartment()
Sejong University
English Literature

>>> 
===================== RESTART: C:/Python27/my_module.py =====================
>>> import my_module
>>> a = int(raw_input("Enter first number : "))
b = int(raw_input("Enter second number : "))
Enter first number : 7
>>> 5
5
>>> 
===================== RESTART: C:/Python27/my_module.py =====================
>>> import my_module
>>> 
======================== RESTART: C:/Python27/test.py ========================
Enter first number : 7
Enter second number : 9

Traceback (most recent call last):
  File "C:/Python27/test.py", line 6, in <module>
    ret_val = sumOfDouble(a, b)
NameError: name 'sumOfDouble' is not defined
>>> 
======================== RESTART: C:/Python27/test.py ========================
Enter first number : 7
Enter second number : 9
sumOfDouble function in my_module
Result Value from sumOfDouble :  32
multipleOfDouble function in my_module
Result Value from multipleOfDouble:  252
>>> 
========================= RESTART: C:/Python27/f.py =========================
10

Traceback (most recent call last):
  File "C:/Python27/f.py", line 3, in <module>
    time.sleep(1)
NameError: name 'time' is not defined
>>> 
========================= RESTART: C:/Python27/f.py =========================
10
9
8
7
6
5
4
3
2
1
Happy New Year~~!!! 
>>> 
========================= RESTART: C:/Python27/f.py =========================
10
9
8
7
6
5
4
3
2
1
Happy New Year~~!!! 
>>> import random
>>> print random.randint(1,100)
42
>>> 
