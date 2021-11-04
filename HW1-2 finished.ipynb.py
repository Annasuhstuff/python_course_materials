#!/usr/bin/env python
# coding: utf-8

# # 0. Наибольший общий делитель - 1 балл
# Напишите функцию, которая на вход принимает два целых числа, а на выходе отдает их наибольших общий делитель. 
# 
# Пример
# 
# Ввод 
# 
# `lcd(10,2)`
# 
# Вывод
# 
# `2`
# 
# Пример
# 
# Ввод 
# 
# `lcd(10,25)`
# 
# Вывод
# 
# `5`

# In[1]:


def lcd (a, b):
    if a > b:
        r = a % b
        if r == 0:
            return b
        else:
            return lcd (b, r)
    if a < b:
        r = b % a
        if r == 0:
            return a
        else:
            return lcd (a, r)

print (lcd(10, 25))


# # 1. Задачка про перевод из `camel_case`'a в `snake_case` - 1.5 балла
#  Напишите функцию, которая на вход принимает строку, записанную в `CamelCase`, а переводит ее в `snake_case`.
#  Подсказка: идите по строке циклом, обрабатывайте каждый символ, если символ заглавный, к обработанным ранее добавляйте нижнее подчеркивание и нынешний переводите в `lower case` 
#  
#  Пример:
# 
# **Вход**: `'camelCaseVar'`
# 
# **Выход**: `'camel_сase_var'`

# In[2]:


def camel_to_snake(str):
    result = ""
    for c in str:
        if c.isupper():
            if len(result) == 0:
                result += c.lower()
            else:
                result += '_' + c.lower()
        else:
            result += c
    return result

print (camel_to_snake( "ААааааА" ))


# # 2. Про Поросёнка Петра - 2 балла
# На плоскости в точке `(0,0)` стоит Поросёнок Пётр. Он умеет ходить налево, направо, вверх и вниз. Расстояние его прохода в какую-либо сторону измеряется в шагах. Когда он идет вправо, его первая координата увеличивается, когда влево - уменьшается. Когда он идет вверх, его вторая координата увеличивается, а когда вниз - уменьшается.
# С клавиатуры считывается число `N` - число ходов, которые сделает Пётр. После чего на каждом шаге спрашивается, сколько шагов и в какую сторону за этот ход Пётр сделает. Так происходит, пока Пётр не осуществит все N ходов.
# Программа должна вывести, сколько шагов Пётр должен был бы сделать, чтобы кратчайшим путем прибыть из свое начальной точки `(0,0)` в свою конечную точку. 
# 
# Напоминание: Пётр умеет ходить только вверх-вниз, и влево-вправо, но не по диагонали.
# 
# Пример ввода:
# 
# Введите N: `3`
# 
# Ход 1: `Вверх 1`
# 
# Ход 2: `Вниз 1`
# 
# Ход 3: `Вверх 1`
# 
# Пример вывода:
# `Пётр находится на расстоянии 1 от (0,0)`

# In[ ]:


def peter (where, steps):
    if where == 'Вверх':
        return 0, int(steps)
    elif where == 'Вниз':
        return 0, -int(steps)
    elif where == 'Вправо':
        return int(steps), 0
    elif where == 'Влево':
        return -int(steps), 0
    return 0, 0

position_x = 0
position_y = 0
n = input('Введите N: ')
for i in range(1, int(n) + 1):
    line = input('Step {}: '.format(i))
    words = line.split()
    where = words[0]
    steps = int(words[1])
    print('parsed words: [{}], [{}]'.format(where, steps))
    dx, dy = get_dxy(where, steps)
    print('dx: {}, dy: {}'.format(dx, dy))
    position_x = position_x + dx
    position_y = position_y + dy

pos = abs(position_x) + abs(position_y)

print ( 'Петр находится на расстоянии {} от (0, 0)'.format(abs(pos)))


# # 3. Sort the keys of the dictionary from a to z.  - 0.5 балла

# In[ ]:


d_ = {"tiramisu":5, "chocolate":2, "pudding":3, "cheesecake":4}

def my_function ( d_ ):
    
    sorteddic = sorted (d_)
    return sorted ( d_ )
    sorteddic = my_function(d_)

print (my_function(d_))


# # 4. Compare three values, return true only if 2 or more values are equal - 0.5 балла

# In[ ]:


def numbers (a, b, c):
    if a == b  or b == c or a == c:
        return True
    else :
        return False

print (numbers (3,3,3))
print (numbers (3,5,5))
print (numbers (3,4,5))
print (numbers (1,1,5))
print (numbers (3,4,4))


# # 5. Given a list with pairs, sort on the sum of pairs - 0.5 балла

# In[ ]:


x = [(3,6),(4,7),(5,9),(8,4),(3,1)]

def sortedpairs (x):

    x.sort(key=lambda item: (item[0]+item[1]))  
    return x
print(sortedpairs(x))


# # 6. Create a function that takes a list of numbers. Return the largest number in the list. - 0.5 балла

# In[ ]:


findLargestNum([4, 5, 1, 3]) ➞ 5

findLargestNum([300, 200, 600, 150]) ➞ 600

findLargestNum([1000, 1001, 857, 1]) ➞ 1001


# In[ ]:


def my_max(arr):
        
    max= 0
    for i in arr:
        if i > max:
            max = i
    return max
print(list(map(my_max, [[4, 5, 1, 3], [300, 200, 600, 150], [1000, 1001, 857, 1]])))


# # 7. Create a function that takes a string and returns the concatenated first and last character. - 0.5 балла

# In[ ]:


repetition("ab", 3) ➞ "ababab"

repetition("kiwi", 1) ➞ "kiwi"

repetition("cherry", 2) ➞ "cherrycherry"


# In[ ]:


def newword ():
    sttr = input( )
    n = int(input( ))
    return (sttr * n)
newword ()    


# # 8. Create a function that takes a 2D list lst returns the sum of the minimum value in each row. - 0.5 балла

# In[ ]:


sum_minimums([
  [1, 2, 3, 4, 5],
  [5, 6, 7, 8, 9],
  [20, 21, 34, 56, 100]
] ➞ 26

# minimum value of the first row is 1
# minimum value of the second row is 5
# minimum value of the third row is 20


# In[ ]:


sum_minimums = ([
  [1, 2, 3, 4, 5],
  [5, 6, 7, 8, 9],
  [20, 21, 34, 56, 100]
])

def my_min(arr):
        
    min = arr [0]
    for i in arr:
        if i < min :
            min = i
    return min
print(sum(list(map(my_min, sum_minimums  ))))


# # 9. Create a function to return the amount of potatoes there are in a string. - 0.5 балла

# In[ ]:


potatoes("potato") ➞ 1

potatoes("potatopotato") ➞ 2

potatoes("potatoapple") ➞ 1


# In[ ]:


def potatofunction (text):
  potatocount = 0
  potatoes = False
  while not potatoes:
    start = text.find("potato")
    if start == -1:
      potatoes = True
    else:
      idx_from = start + len("potato")
      text = text [idx_from:]
      potatocount += 1
  return (potatocount)
print (potatofunction ( "potatopotato" ))


# # 10. Create a function that takes a list of integers as an argument and returns a unique number from that list. All numbers except unique ones have the same number of occurrences in the list. - 0.5 балла

# In[ ]:


find_single_number([2, 2, 2, 3, 4, 4, 4]) ➞ 3

find_single_number([2]) ➞ 2

find_single_number([]) ➞ None

find_single_number([7, 13, 3, 6, 5, 4, 4, 13, 5, 3, 6, 7, 6, 5, 3, 13, 4, 7, 13, 5, 7, 4, 3, 6, 8, 4, 3, 7, 5, 6, 13]) ➞ 8

find_single_number([1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 101, 4, 3, 1, 5, 6, 2]) ➞ 101


# In[ ]:


def find_single_number(list):
    for i in list:
        uniq_number = 0
        uniq_qty = 0
        for j in list:
            if i == j:
                uniq_number = i
                uniq_qty += 1
        if uniq_qty == 1:
            return uniq_number
    return None

l = [ 5, 12, 13, 5, 4, 12, 13, 14, 1, 14, 1, 4, 100500 ]
print(find_single_number(l))


# # 11. Given a letter and a list of words, return whether the letter does not appear in any of the words. - 0.5 балла

# In[ ]:


forbidden_letter("r", ["rock", "paper", "scissors"]) ➞ False

forbidden_letter("a", ["spoon", "fork", "knife"]) ➞ True

forbidden_letter("m", []) ➞ True


# In[ ]:


def forbidden_letter (letter, thelist):
  for word in thelist:
    for l in word:
        if l == letter:
            return False
  return True

print(forbidden_letter("r", ["rock", "paper", "scissors"]))
print(forbidden_letter("a", ["spoon", "fork", "knife"]))
print(forbidden_letter("m", []))


# # 12.  Define a function which create a Pattern like this one.  - 2 балла

# In[ ]:


Input: 4
Pattern:

 01234
  | |     0
 -----    1
  | |     2
 -----    3
  | |     4


# In[ ]:


def print_pattern(size):
    size += 1
    first_row = ''
    for i in range(size):
            first_row += str(i)
    print(first_row)
    row = ''
    for i in range(size):
        if i % 2 == 0:
            row += ' '
        else:
            row += '|'
    for i in range(size):
        if i % 2 == 0:
            print(row + '   ' + str(i))
        else:
            print('-' * size + '   ' + str(i))
sz = int(input("Введите число: "))
print_pattern(sz)


# # 13. Create a function that takes three numbers as arguments and returns True if it's a triangle and False if not.  - 0.5 балла

# In[ ]:


is_triangle(2, 3, 4) ➞ True

is_triangle(3, 4, 5) ➞ True

is_triangle(4, 3, 8) ➞ False


# In[ ]:


def is_triangle (x, y, z):
  value = True
  if ( x + y <= z ) or ( x + z <= y) or ( y + z <= x ):
    value = False
  return value
print (is_triangle(2, 3, 4))
print (is_triangle(3, 4, 5))
print (is_triangle(4, 3, 8))


# # 14. Create a "Code" Generator that takes text as input and replaces some letter with another letter, and outputs the "encoded" message. Create funcs to encode and decode messages

# In[ ]:


replacement = {"a": "b", "d": "1" ......}


# In[ ]:


def generator(letters, text):
  result = ''
  for symbol in text:
    if symbol in letters:
      result += letters[symbol]
    else:
      result += symbol
  return result

def encoder (text):
  codedic = {'a' : 'A', 'b' : 'B', 'c' : 'C', 'z' : 'Z'}
  return generator(codedic, text)

def decoder (text):
  codedic = {'A' : 'a', 'B' : 'b', 'C' : 'c', 'Z': 'z'}
  return generator(codedic, text)

encoded = encoder ('a b c z')
print(encoded)
decoded = decoder (encoded)
print(decoded)

