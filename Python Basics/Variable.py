Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> take_off_planes = 121
>>> initial_no_of_planes = 121
>>> take_off_planes = 63
>>> landed_planes = 54
>>> 
>>> current_no_of_planes = initial_no_of_planes - take_off_planes + landed_planes
>>> 
>>> current_no_of_planes
112
>>> 
>>> num = 65
>>> type(num)
<class 'int'>
>>> 
>>> num = "Vinay"
>>> type(num)
<class 'str'>
>>> Num
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Num
NameError: name 'Num' is not defined
>>> Num = 34

>>> Num
34
>>> a = True
>>> b = False
>>> 
>>> a and (not b)
True
>>> num1 = 20
>>> num2 = 30
>>> num3 = 40
>>> 
>>> num1 = num1 + num2
>>> num1
50
\
>>> num1 = num1 - (num3+20)
>>> num1
-10
>>> num3 = num3/num1
>>> num3
-4.0
>>> num2 = (num3 * (-10))%(num1/-2)
>>> num2
0.0
>>> # (-4.0 * -10)% (-10/-2)
>>> # (40)%5
>>> 40 % 5
0
>>> 15 - 10 * 25
-235
>>> 
>>> (15 - 10) * 25
125
>>> num1 == (num2+10)-20
True
>>> num1/-2 <= (num3*-3)%-2
False
>>> 5 <= 0
False
>>> num1 = 3
>>> num1 = 35
>>> 
>>> (num1 > num3*11) >= ((num2+10)>num3)
True
>>> (num1 > num3*11) >= ((num2+10)<num3)
True
>>> # T -> 1
>>> # F -> 0
>>> 1 >= 0
True
>>> num3 = 30
>>> ((num3 < num1%5) != ((num2+2)*20%4 < -1)) <= False # S -> F, G -> F, P -> F, R -> F, S -> T
True
>>> (False != False) <= False
True
>>> (True != False) <= False
False
>>> 1 <= 0
False
>>> 