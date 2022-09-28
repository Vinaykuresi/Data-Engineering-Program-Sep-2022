Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> pan_card = "ASGPV1023V"
>>> pan_card[2]
'G'
>>> pan_card[len(pan_card)-1]
'V'
>>> num_list = [3, 4, 5, 6]
>>> 
>>> num_list[1] = 7
>>> num_list
[3, 7, 5, 6]
>>> pan_card[5:len(pan_card)-1]
'1023'
>>> pan_card[2]="H"
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    pan_card[2]="H"
TypeError: 'str' object does not support item assignment
>>> 