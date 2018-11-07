Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> range(5, 21)
range(5, 21)
>>> list(range(5, 21))
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> a = ['onion', 'potato', 'ginger', 'cucumber']
>>> print(type(a))
<class 'list'>
>>> for item in a:
	print(item)

	
onion
potato
ginger
cucumber
>>> a = {'n' : 'm', 'ni' : 'r', 'mbl' : '43545'}
>>> print(a)
{'n': 'm', 'ni': 'r', 'mbl': '43545'}
>>> for item in a:
	print(item)

	
n
ni
mbl
>>> a = 'python'
>>> for word in a:
	print(word)

	
p
y
t
h
o
n
>>> range(5, 19)
range(5, 19)
>>> list(range(5,19))
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
>>> list(range(5, 21))
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> for number in range(1, 11)
SyntaxError: invalid syntax
>>> for number in range(1, 11):
	print(number)

	
1
2
3
4
5
6
7
8
9
10
>>> for number in range(0, 10):
	print(number)

	
0
1
2
3
4
5
6
7
8
9
>>> for number in range(5, 19):
	print(number)

	
5
6
7
8
9
10
11
12
13
14
15
16
17
18
>>> for number in range(5, 21):
	print(number)

	
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
>>> for number in range(10, 100, 2)
SyntaxError: invalid syntax
>>> for number in range(10, 100,2):
	print(number)

	
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
>>> for number in range(10, 100, 3):
	print(number)

	
10
13
16
19
22
25
28
31
34
37
40
43
46
49
52
55
58
61
64
67
70
73
76
79
82
85
88
91
94
97
>>> for number in range(10, 1000, 100):
	print(number)

	
10
110
210
310
410
510
610
710
810
910
>>> 
