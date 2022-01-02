Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(45 +20)
65
print(10+20-15)
15
print(10*5)
50
print(100/3)
33.333333333333336
print(100//33)
3
print(100/33)
3.0303030303030303
print(10**2)
100
print(10%3)
1
print(10+5*2)
20
print(10-5*10+5)
-35
print(5*10**2)
500
print(10+5)*2
15
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(10+5)*2
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
print(10+5(*2))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(10+5(*2))
TypeError: 5 argument after * must be an iterable, not int
print((10+5)*2)
30
print((10-5*(10+5)))
-65
print((5*10)**2)
2500
print((12+(5*2+3)))
25
print((12+(5*(2+3))))
37
print(10+)
SyntaxError: invalid syntax
print("Ten divided by zero is",10/0)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print("Ten divided by zero is",10/0)
ZeroDivisionError: division by zero
