Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a+=2
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a+=2
NameError: name 'a' is not defined
>>> a=12
>>> a
12
>>> a+=12
>>> a
24
>>> 2==2 and 3==3
True
>>> 2==2 and 3==4
False
>>> 2==2 and 3==4
False
>>> 2==2 or 3==4
True
>>> 2==5 or 3==4
False
>>> 2==5
False
>>> not 2 == 5
True
>>> 
>>> a = 'Bangladesh'
>>> b = 'desh'
>>> b in a
True
>>> a in b
False
>>> 
>>> c in a
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    c in a
NameError: name 'c' is not defined
>>> a = 'Bangladesh\'
SyntaxError: EOL while scanning string literal
>>> a = 'Bangladesg'
>>> b = 12
>>> a is b
False
>>> a is not b
True
>>> 
