Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("I am gonna be a pythonist.")
I am gonna be a pythonist.
>>> print("My name is khan and I am not a terrorist.")
My name is khan and I am not a terrorist.
>>> 3+2
5
>>> 10-4
6
>>> 6*7
42
>>> 48/3
16.0
>>> 10%3
1
>>> 5 + (9*3)
32
>>> -13+5
-8
>>> x=5

>>> x
5
>>> x=12
>>> x
12
>>> x=10.34
>>> x
10.34
>>> x='python'
>>> x
'python'
>>> a=5
>>> b=10

>>> a*b
50
>>> 
>>> a=5
>>> type(a)
<class 'int'>
>>> b=10
>>> type(b)
<class 'int'>
>>> a*b
50
>>> type(a*b)
<class 'int'>
>>> a=1
>>> type(a)
<class 'int'>
>>> b=3.1416
>>> type(b)
<class 'float'>
>>> c="Hello World!"
>>> type(c)
<class 'str'>
>>> d=true
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d=true
NameError: name 'true' is not defined
>>> d = true
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    d = true
NameError: name 'true' is not defined
>>> type(d)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    type(d)
NameError: name 'd' is not defined
>>> d = true
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d = true
NameError: name 'true' is not defined
>>> a = input()
10
>>> a
'10'
>>> b = input()
200
>>> b
'200'
>>> a = input()
10
>>> b = input()
40
>>> a*b
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'str'
>>> a = input()
10
>>> type(a)
<class 'str'>
>>> b = input()
40
>>> type(b)
<class 'str'>
>>> a*b
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'str'
>>> a=input()
10
>>> a=int(a)
>>> b= input()
40
>>> b=int(b)
>>> a*b
400
>>> a = int(input())
10
>>> b = int(input())
40
>>> a*b
400
>>> a, b = input().split()
10 40
>>> a
'10'
>>> b
'40'
>>> a*b
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'str'
>>> a=int(a)
>>> b=int(b)
>>> a*b
400
>>> a, b = int(input().split())
10 40
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a, b = int(input().split())
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> a, b, c = input().split()
2 3 4
>>> c
'4'
>>> b
'3'
>>> a
'2'
>>> a=int(a)
>>> b=int(b)
>>> c=int(c)
>>> a*b*c
24
>>> 3+2
5
>>> 10-4
6
>>> 6*7
42
>>> 48/3
16.0
>>> 10%3
1
>>> 5+(9*3)
32
>>> -13+5
-8
>>> 3**2
9
>>> 1.0/2.0
0.5
>>> 1.0//2.0
0.0
>>> 2.0//2.0
1.0
>>> 3.0//2.0
1.0
>>> 
