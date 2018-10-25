Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = ()
>>> a
()
>>> type(a)
<class 'tuple'>
>>> a = ('onion', 'tometo', 'ginger', 'cucumber')
>>> a
('onion', 'tometo', 'ginger', 'cucumber')
>>> type(a)
<class 'tuple'>
>>> b = ('a', 'b', 'c', 1, 34)
>>> b
('a', 'b', 'c', 1, 34)
>>> type(b)
<class 'tuple'>
>>> b.append(12)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b.append(12)
AttributeError: 'tuple' object has no attribute 'append'
>>> b[1]
'b'
>>> b[5]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    b[5]
IndexError: tuple index out of range
>>> b[4]
34
>>> b[:4]
('a', 'b', 'c', 1)
>>> b[1:4]
('b', 'c', 1)
>>> b[2:]
('c', 1, 34)
>>> b + ('new')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b + ('new')
TypeError: can only concatenate tuple (not "str") to tuple
>>> b + ('new',)
('a', 'b', 'c', 1, 34, 'new')
>>> b
('a', 'b', 'c', 1, 34)
>>> b = b + (b + ('new',))
>>> b
('a', 'b', 'c', 1, 34, 'a', 'b', 'c', 1, 34, 'new')
>>> b
('a', 'b', 'c', 1, 34, 'a', 'b', 'c', 1, 34, 'new')
>>> b = (b + ('test',))
>>> b
('a', 'b', 'c', 1, 34, 'a', 'b', 'c', 1, 34, 'new', 'test')
>>> b
('a', 'b', 'c', 1, 34, 'a', 'b', 'c', 1, 34, 'new', 'test')
>>> b.split()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    b.split()
AttributeError: 'tuple' object has no attribute 'split'
>>> split(b)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    split(b)
NameError: name 'split' is not defined
>>> b.split('')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    b.split('')
AttributeError: 'tuple' object has no attribute 'split'
>>> b.split(' ')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    b.split(' ')
AttributeError: 'tuple' object has no attribute 'split'
>>> len(b)
12
>>> b.count(a)
0
>>> b.count('a')
2
>>> b.count("test")
1
>>> b.count('test',)
1
>>> # Python set
>>> 
>>> 
>>> a = {'oragge', 'banana', 'pear', 'apple'}
>>> a
{'banana', 'pear', 'apple', 'oragge'}
>>> type(a)
<class 'set'>
>>> a = set('orange', 'banana', 'pear', 'apple')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a = set('orange', 'banana', 'pear', 'apple')
TypeError: set expected at most 1 arguments, got 4
>>> a = (dkjfhkdjsnzcbXnmvjS)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a = (dkjfhkdjsnzcbXnmvjS)
NameError: name 'dkjfhkdjsnzcbXnmvjS' is not defined
>>> a = set(aabbccddeekjdfhkjdsf)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a = set(aabbccddeekjdfhkjdsf)
NameError: name 'aabbccddeekjdfhkjdsf' is not defined
>>> a = set('aabbccddeekglhjlkisgfnzc')
>>> a
{'k', 'j', 'a', 'l', 'z', 'c', 'e', 'd', 's', 'f', 'i', 'n', 'g', 'h', 'b'}
>>> len(a)
15
>>> a = set()
>>> a
set()
>>> type(a)
<class 'set'>
>>> A = {}
>>> a
set()
>>> type(A)
<class 'dict'>
>>> # সেটের উপাদানগুলোকে ইনডেক্স নম্বর দিয়ে অ্যাক্সেস করা যায় না।
>>> 
>>> a = {'a', 'b'}
>>> a
{'a', 'b'}
>>> a[1]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a[1]
TypeError: 'set' object does not support indexing
>>> a.add('r')
>>> a
{'a', 'r', 'b'}
>>> a.add('x', 'z')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.add('x', 'z')
TypeError: add() takes exactly one argument (2 given)
>>> a.update('z', 'x', 'c')
>>> a
{'a', 'z', 'c', 'x', 'r', 'b'}
>>> a.update('mnl')
>>> a
{'a', 'l', 'z', 'c', 'n', 'x', 'r', 'm', 'b'}
>>> a.update({'kjh', 'gf'})
>>> a
{'a', 'l', 'z', 'c', 'n', 'gf', 'x', 'r', 'kjh', 'm', 'b'}
>>> a.remove('a')
>>> a
{'l', 'z', 'c', 'n', 'gf', 'x', 'r', 'kjh', 'm', 'b'}
>>> a.remove('')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.remove('')
KeyError: ''
>>> a.remove('p')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.remove('p')
KeyError: 'p'
>>> a.pop()
'l'
>>> a
{'z', 'c', 'n', 'gf', 'x', 'r', 'kjh', 'm', 'b'}
>>> a.pop()
'z'
>>> a
{'c', 'n', 'gf', 'x', 'r', 'kjh', 'm', 'b'}
>>> # union Set
>>> 
>>> a = {1,2,3,4,5}
>>> b = {6,7,8}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> c = {1,2,3,4,5}
>>> d = {2,3,4,5,6}
>>> c.intersection(d)
{2, 3, 4, 5}
>>> a = {1,2,3,4,5,6}
>>> b = {5,6,7,8}
>>> a.difference(b)
{1, 2, 3, 4}
>>> b.difference(a)
{8, 7}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> a.intersection(b)
{5, 6}
>>> 
