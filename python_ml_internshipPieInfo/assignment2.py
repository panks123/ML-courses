Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Assignment 2
>>> #Arithmetic operators
>>> 10+30
40
>>> 10*20
200
>>> 20-10
10
>>> 20/4
5.0
>>> 20/3
6.666666666666667
>>> 20//3
6
>>> 20*6
120
>>> 20%7
6
>>> 3**6
729
>>> #String and string operations
>>> s='HelloWorld!'
>>> s
'HelloWorld!'
>>> s[:]
'HelloWorld!'
>>> s[:4]
'Hell'
>>> s[2:]
'lloWorld!'
>>> s[2:8:2]
'loo'
>>> s[5]
'W'
>>> s[-2]
'd'
>>> s[::-1]
'!dlroWolleH'
>>> s[-3::-2]
'loolH'
>>> s1='Welcome'
>>> s+s1
'HelloWorld!Welcome'
>>> 'Hello'*5
'HelloHelloHelloHelloHello'
>>> s.find('ll')
2
>>> s.find('ol')
-1
>>> s.replace('Happy','Welcome')
'HelloWorld!'
>>> s
'HelloWorld!'
>>> s.replace('Hello','Welcome')
'WelcomeWorld!'
>>> s.upper()
'HELLOWORLD!'
>>> s.lower()
'helloworld!'
>>> #LISTS
>>> li1=[1,2,3,4,5]
>>> li[3]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    li[3]
NameError: name 'li' is not defined
>>> li1[3]
4
>>> li1[-3]
3
>>> li1[:]
[1, 2, 3, 4, 5]
>>> li1[:3]
[1, 2, 3]
>>> li1[3:]
[4, 5]
>>> li1[::-1]
[5, 4, 3, 2, 1]
>>> li1[-1::-2]
[5, 3, 1]
>>> li[3:5]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    li[3:5]
NameError: name 'li' is not defined
>>> li1[3:5]
[4, 5]
>>> li1.append(12)
>>> li1.extend([4,3,2,1])
>>> li1
[1, 2, 3, 4, 5, 12, 4, 3, 2, 1]
>>> li1.sort()
>>> li1
[1, 1, 2, 2, 3, 3, 4, 4, 5, 12]
>>> li1.insert(1,33)
>>> li1
[1, 33, 1, 2, 2, 3, 3, 4, 4, 5, 12]
>>> li1.push(20)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    li1.push(20)
AttributeError: 'list' object has no attribute 'push'
>>> li.pop()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    li.pop()
NameError: name 'li' is not defined
>>> li1.push(20)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    li1.push(20)
AttributeError: 'list' object has no attribute 'push'
>>> li1.pop()
12
>>> li1.remove(3)
>>> li1
[1, 33, 1, 2, 2, 3, 4, 4, 5]
>>> li1.remove(3)
>>> li1
[1, 33, 1, 2, 2, 4, 4, 5]
>>> li1.pop(1)
33
>>> li1
[1, 1, 2, 2, 4, 4, 5]
>>> li1.clear()
>>> li1
[]
>>> #Tuple
>>> t=(1,2,1,3,4,5,'ewtet',)
>>> t
(1, 2, 1, 3, 4, 5, 'ewtet')
>>> t[:]
(1, 2, 1, 3, 4, 5, 'ewtet')
>>> t[:3]
(1, 2, 1)
>>> t[3:]
(3, 4, 5, 'ewtet')
>>> t[::-1]
('ewtet', 5, 4, 3, 1, 2, 1)
>>> t[1::2]
(2, 3, 5)
>>> t.index(2)
1
>>> t.index(6)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    t.index(6)
ValueError: tuple.index(x): x not in tuple
>>> t=t+(4,5,4,3,7)
>>> t
(1, 2, 1, 3, 4, 5, 'ewtet', 4, 5, 4, 3, 7)
>>> t.count(1)
2
>>> #SETs
>>> s={1,2,3,1,4,3,5,6,7}
>>> s
{1, 2, 3, 4, 5, 6, 7}
>>> s.add(66)
>>> s
{1, 2, 3, 4, 5, 6, 7, 66}
>>> s.update([6,4,5,5,3,33,4,77])
>>> s
{1, 2, 3, 4, 5, 6, 7, 66, 33, 77}
>>> s.remove(77)
>>> s
{1, 2, 3, 4, 5, 6, 7, 66, 33}
>>> s.pop()
1
>>> s
{2, 3, 4, 5, 6, 7, 66, 33}
>>> s.pop()
2
>>> s1={23,4,66,7,9,8,10}
>>> s1
{66, 4, 7, 8, 9, 10, 23}
>>> s1.union(s)
{33, 66, 3, 4, 5, 6, 7, 8, 9, 10, 23}
>>> s1.intersection(s)
{66, 4, 7}
>>> s1.difference(s)
{8, 9, 10, 23}
>>> s.differnce(s1)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    s.differnce(s1)
AttributeError: 'set' object has no attribute 'differnce'
>>> s.difference(s1)
{33, 3, 5, 6}
>>> s.symmetric_differnce(s1)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s.symmetric_differnce(s1)
AttributeError: 'set' object has no attribute 'symmetric_differnce'
>>> s.symmetric_difference(s1)
{3, 5, 6, 8, 9, 10, 23, 33}
>>> s1.symmetric_difference(s)
{33, 3, 5, 6, 8, 9, 10, 23}
>>> s.isdisjoint(s)
False
>>> s1.issubset(s)
False
>>> s.issuperset(s1)
False
>>> s.clear()
>>> s
set()
>>> #Dictionary()
>>> d={1:"one",2:"Two",3:"Three",4:"Four",5:"Five"}
>>> d
{1: 'one', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}
>>> d[1]
'one'
>>> d[6]="Six"
>>> d
{1: 'one', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six'}
>>> d.pop(5)
'Five'
>>> d
{1: 'one', 2: 'Two', 3: 'Three', 4: 'Four', 6: 'Six'}
>>> d.keys()
dict_keys([1, 2, 3, 4, 6])
>>> d.values()
dict_values(['one', 'Two', 'Three', 'Four', 'Six'])
>>> d.items()
dict_items([(1, 'one'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (6, 'Six')])
>>> d1={10:"Ten",9:"Nine"}
>>> d1
{10: 'Ten', 9: 'Nine'}
>>> d.update(d1)
>>> d
{1: 'one', 2: 'Two', 3: 'Three', 4: 'Four', 6: 'Six', 10: 'Ten', 9: 'Nine'}
>>> id(d1)
51281088
>>> id(d)
51299696
>>> type(li1)
<class 'list'>
>>> type(t)
<class 'tuple'>
>>> type(1)
<class 'int'>
>>> type(s)
<class 'set'>
>>> type(d)
<class 'dict'>
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> set
Help on class set in module builtins:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

help> exit()
No Python documentation found for 'exit()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> e
No Python documentation found for 'e'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> return
The "return" statement
**********************

   return_stmt ::= "return" [expression_list]

"return" may only occur syntactically nested in a function definition,
not within a nested class definition.

If an expression list is present, it is evaluated, else "None" is
substituted.

"return" leaves the current function call with the expression list (or
"None") as return value.

When "return" passes control out of a "try" statement with a "finally"
clause, that "finally" clause is executed before really leaving the
function.

In a generator function, the "return" statement indicates that the
generator is done and will cause "StopIteration" to be raised. The
returned value (if any) is used as an argument to construct
"StopIteration" and becomes the "StopIteration.value" attribute.

In an asynchronous generator function, an empty "return" statement
indicates that the asynchronous generator is done and will cause
"StopAsyncIteration" to be raised.  A non-empty "return" statement is
a syntax error in an asynchronous generator function.

Related help topics: FUNCTIONS

help> 
