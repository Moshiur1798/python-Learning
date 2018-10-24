Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = []
>>> a
[]
>>> type(a)
<class 'list'>
>>> a = ['onion', 'potato', 'ginger', 'cucumber']
>>> a
['onion', 'potato', 'ginger', 'cucumber']
>>> type(a)
<class 'list'>
>>> b = ['onion', 'potato', 'tometo', 'cucumber', 1, 3.1416]
>>> b
['onion', 'potato', 'tometo', 'cucumber', 1, 3.1416]
>>> type(b)
<class 'list'>
>>> type(b[0])
<class 'str'>
>>> type(b[1])
<class 'str'>
>>> type(b[4])
<class 'int'>
>>> type(b[5])
<class 'float'>
>>> b
['onion', 'potato', 'tometo', 'cucumber', 1, 3.1416]
>>> b[0] = 'rice'
>>> b
['rice', 'potato', 'tometo', 'cucumber', 1, 3.1416]
>>> b[4] = 570
>>> b
['rice', 'potato', 'tometo', 'cucumber', 570, 3.1416]
>>> b[5] = 23486.4678
>>> b
['rice', 'potato', 'tometo', 'cucumber', 570, 23486.4678]
>>> b
['rice', 'potato', 'tometo', 'cucumber', 570, 23486.4678]
>>> b[2] = 343
>>> b
['rice', 'potato', 343, 'cucumber', 570, 23486.4678]
>>> b[4] = 'finger'
>>> b
['rice', 'potato', 343, 'cucumber', 'finger', 23486.4678]
>>> b[6] = 'new'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    b[6] = 'new'
IndexError: list assignment index out of range
>>> b.append('new')
>>> b
['rice', 'potato', 343, 'cucumber', 'finger', 23486.4678, 'new']
>>> b[6]
'new'
>>> b.insert(1, 'python')
>>> b
['rice', 'python', 'potato', 343, 'cucumber', 'finger', 23486.4678, 'new']
>>> b.extend(['a', 'b', 'c'])
>>> b
['rice', 'python', 'potato', 343, 'cucumber', 'finger', 23486.4678, 'new', 'a', 'b', 'c']
>>> b + ['d', 'e', 'f']
['rice', 'python', 'potato', 343, 'cucumber', 'finger', 23486.4678, 'new', 'a', 'b', 'c', 'd', 'e', 'f']
>>> b
['rice', 'python', 'potato', 343, 'cucumber', 'finger', 23486.4678, 'new', 'a', 'b', 'c']
>>> b = b + ['d', 'e', 'f']
>>> b
['rice', 'python', 'potato', 343, 'cucumber', 'finger', 23486.4678, 'new', 'a', 'b', 'c', 'd', 'e', 'f']
>>> c = ['dish', 'catch']
>>> c
['dish', 'catch']
>>> b = b+c
>>> b
['rice', 'python', 'potato', 343, 'cucumber', 'finger', 23486.4678, 'new', 'a', 'b', 'c', 'd', 'e', 'f', 'dish', 'catch']
>>> 
