Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 60
>>> type(num)
<class 'int'>
>>> 
>>> num2 = 60.34
>>> type(num2)
<class 'float'>
>>> 
>>> 
>>> name = "Vinay"
>>> type(name)
<class 'str'>
>>> 
>>> 
>>> type((True or True))
<class 'bool'>
>>> 
>>> 
>>> num4 = '34'
>>> 
>>> type(num4)
<class 'str'>
>>> 
>>> 
>>> num
60
>>> num = "Snehal"
>>> num
'Snehal'
>>> type(num)
<class 'str'>
>>> # if, else, for, while, def, print, raise, try, except
>>> if = 20
SyntaxError: invalid syntax
>>> for = "kumar"
SyntaxError: invalid syntax
>>> if(21%3):
	print("Success")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> null
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    null
NameError: name 'null' is not defined
>>> num = None
>>> num
>>> type(num)
<class 'NoneType'>
>>> num = 1 + 2.0
>>> num
3.0
>>> num = 1 + int(2.0)
>>> num
3
>>> int(2.0)
2
>>> num = "1" + 23
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    num = "1" + 23
TypeError: can only concatenate str (not "int") to str
>>> num = "1" + "23"
>>> num
'123'
>>> num += str(32)
>>> num
'12332'
>>> 
>>> num1 = 20
>>> num2 = 30
>>> num3 = 40
>>> 
>>> num1 += ((num3%4)/num1*2/4)
>>> num1
20.0
>>> # 20 + 0 -> 20
>>> 
>>> num2 %= (30%(num1/num2))%(False/True)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    num2 %= (30%(num1/num2))%(False/True)
ZeroDivisionError: float modulo
>>> num2 %= (30+(num1+num2))%(True/True)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    num2 %= (30+(num1+num2))%(True/True)
ZeroDivisionError: float modulo
>>> num2 %= (30+(num1+num2))-(True/True)
>>> num2
30.0
>>> # 30 % 79
>>> 