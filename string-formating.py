Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = bangla
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a = bangla
NameError: name 'bangla' is not defined
>>> a = 'bangla'
>>> a
'bangla'
>>> len(a)
6
>>> a.count('a')
2
>>> sentence = "How can a clam cram in aclean cream can?"
>>> sentence.count('c')
6
>>> sentence.count('c', 5)
5
>>> sentence.count('c', 5, 9)
0
>>> sentence[5]
'a'
>>> sentence[1]
'o'
>>> sentence.find('c')
4
>>> sentence.find('c', 5)
10
>>> sentence[10]
'c'
>>> sentence[0]
'H'
>>> sentence[9]
' '
>>> sentence[8]
'a'
>>> sentence.index('x')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    sentence.index('x')
ValueError: substring not found
>>> sentence.replace('c', 'd')
'How dan a dlam dram in adlean dream dan?'
>>> sentence.replace('?', '')
'How can a clam cram in aclean cream can'
>>> sen = 'how are you?'
>>> sen.strip('?')
'how are you'
>>> sen.split(' ')
['how', 'are', 'you?']
>>> sen.split('')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    sen.split('')
ValueError: empty separator
>>> sen.split(" ")
['how', 'are', 'you?']
>>> 
