Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = {}
>>> a
{}
>>> type(a)
<class 'dict'>
>>> a = {'name' : 'Md Moshiur Rahman', 'nickname' : 'Rony', 'email' : 'moshiur1798@gmail.com'}
>>> a
{'name': 'Md Moshiur Rahman', 'nickname': 'Rony', 'email': 'moshiur1798@gmail.com'}
>>> type(a)
<class 'dict'>
>>> a['name']
'Md Moshiur Rahman'
>>> a['email']
'moshiur1798@gmail.com'
>>> a['name'] = 'Mohammad moshiur Rahman'
>>> a
{'name': 'Mohammad moshiur Rahman', 'nickname': 'Rony', 'email': 'moshiur1798@gmail.com'}
>>> a['hometown'] = 'Narsingdi'
>>> a
{'name': 'Mohammad moshiur Rahman', 'nickname': 'Rony', 'email': 'moshiur1798@gmail.com', 'hometown': 'Narsingdi'}
>>> b ={'father' : 'Rafiqul Islam', 'mother': 'Lutfun Nahar Begum'}
>>> b
{'father': 'Rafiqul Islam', 'mother': 'Lutfun Nahar Begum'}
>>> a.update(b)
>>> a
{'name': 'Mohammad moshiur Rahman', 'nickname': 'Rony', 'email': 'moshiur1798@gmail.com', 'hometown': 'Narsingdi', 'father': 'Rafiqul Islam', 'mother': 'Lutfun Nahar Begum'}
>>> del a['hometown']
>>> a
{'name': 'Mohammad moshiur Rahman', 'nickname': 'Rony', 'email': 'moshiur1798@gmail.com', 'father': 'Rafiqul Islam', 'mother': 'Lutfun Nahar Begum'}
>>> a.clear()
>>> a
{}
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a.copy()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.copy()
NameError: name 'a' is not defined
>>> a = {'name' : 'moshiur', 'phone' : '8748935'}
>>> a
{'name': 'moshiur', 'phone': '8748935'}
>>> a.copy()
{'name': 'moshiur', 'phone': '8748935'}
>>> a.get('name')
'moshiur'
>>> a.get('home')
>>> a.get('home', 'kisu nai')
'kisu nai'
>>> 'name' in a
True
>>> 'home' in a
False
>>> a.items()
dict_items([('name', 'moshiur'), ('phone', '8748935')])
>>> a.keys()
dict_keys(['name', 'phone'])
>>> a.values()
dict_values(['moshiur', '8748935'])
>>> 
