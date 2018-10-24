Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 23
>>> # a is an int variavle
>>> a
23
>>> a = 24  # a is an in variable
>>> a
24
>>> a = 'bangla'
>>> b = "desh"
>>> type(a)
<class 'str'>
>>> type(b)
<class 'str'>
>>> c = 'Bangladesh is my 'motherland', I love her very much.'
SyntaxError: invalid syntax
>>> c
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> c = "Bangladesh is my 'motherland', I lobve her mvery much."
>>> c
"Bangladesh is my 'motherland', I lobve her mvery much."
>>> c = "Bangladesh is my \"motherland"\", I love her very much."
SyntaxError: unexpected character after line continuation character
>>> cc = "Bangladesh is my \"motherland"\", I love her very much."
SyntaxError: unexpected character after line continuation character
>>> c
"Bangladesh is my 'motherland', I lobve her mvery much."
>>> c = "Bangladesh is my \"motherland\", I love her very much."
>>> c = "Bangladesh is my \"motherlabd\", I love her very much."
>>> c
'Bangladesh is my "motherlabd", I love her very much.'
>>> c = 'Bangldeshis my \'motherland\', i love her very much.'
>>> c
"Bangldeshis my 'motherland', i love her very much."
>>> print('\')
	  
SyntaxError: EOL while scanning string literal
>>> 
	  
>>> print('\\')
	  
\
>>> print('\n')
	  


>>> print('\t')
	  
	
>>> a = 'Bangla'
	  
>>> a[0]
	  
'B'
>>> a[1]
	  
'a'
>>> a[5]
	  
'a'
>>> a[6]
	  
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a[6]
IndexError: string index out of range
>>> a[:1]
	  
'B'
>>> a = [:2]
	  
SyntaxError: invalid syntax
>>> a  [:2]
	  
'Ba'
>>> a = [:3]
	  
SyntaxError: invalid syntax
>>> a = [:3]
	  
SyntaxError: invalid syntax
>>> 
	  
>>> a[:3]
	  
'Ban'
>>> a[2:]
	  
'ngla'
>>> a[4:]
	  
'la'
>>> a[-1]
	  
'a'
>>> a[-2]
	  
'l'
>>> a[-3]
	  
'g'
>>> a[a:4]
	  
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a[a:4]
TypeError: slice indices must be integers or None or have an __index__ method
>>> a[1:4]
	  
'ang'
>>> a[:4]
	  
'Bang'
>>> a[1]
	  
'a'
>>> a[1:4]
	  
'ang'
>>> a[4] = 'b'
	  
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a[4] = 'b'
TypeError: 'str' object does not support item assignment
>>> a = 'bangla'
	  
>>> print(a)
	  
bangla
>>> print('My favorite language is:', a)
	  
My favorite language is: bangla
>>> print('My favorite language is: %s' %a)
	  
My favorite language is: bangla
>>> number = 345.354354343
	  
>>> print(number)
	  
345.354354343
>>> print('%.2f' %number)
	  
345.35
>>> print('%.4f' %number)
	  
345.3544
>>> print('%.1f' %number)
	  
345.4
>>> print('%.f' %number)
	  
345
>>> print('%.5f' %number)
	  
345.35435
>>> a = input()
	  
bangla
>>> b = input()
	  
english
>>> print('My favorite languages are:', a, 'and', b)
	  
My favorite languages are: bangla and english
>>> a = input()
	  
Bangla
>>> b = input()
	  
English
>>> print('My favorite langeages are: %s and %s' %(a, b))
	  
My favorite langeages are: Bangla and English
>>> a = 'bangla'
	  
>>> a
	  
'bangla'
>>> b = 'desh'
	  
>>> a+b
	  
'bangladesh'
>>> x = 'Dhaka'
	  
>>> y = 'Barishal'
	  
>>> z = 'Sylhet'
	  
>>> x + '-' + x + '-' + z
	  
'Dhaka-Dhaka-Sylhet'
>>> '-'.join((x, y, z))
	  
'Dhaka-Barishal-Sylhet'
>>> "bangladesh is my motherland. i just love her." .title()
	  
'Bangladesh Is My Motherland. I Just Love Her.'
>>> a.capitalize()
	  
'Bangla'
>>> a.upperz()
	  
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.upperz()
AttributeError: 'str' object has no attribute 'upperz'
>>> a.upper()
	  
'BANGLA'
>>> 'BANGLA'.lower()
	  
'bangla'
>>> 'Bangla'.lower()
	  
'bangla'
>>> 'BANGLA'.casefold()
	  
'bangla'
>>> 'Bangla'. casefold()
	  
'bangla'
>>> 'bangla'.swapcase()
	  
'BANGLA'
>>> 'Bangla'.swapcase()
	  
'bANGLA'
>>> 
