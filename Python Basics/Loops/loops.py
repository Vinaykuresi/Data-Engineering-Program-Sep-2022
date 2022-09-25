Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> 
>>> ticket_id_1 = 1001
>>> ticket_id_2 = 1002
>>> ticket_id_3 = 1003
>>> 
>>> ticket_ids = [1001, 1002, 1003, 1004, 1005, 1006]
>>> 
>>> ticket_ids[0]
1001
>>> ticket_ids[5]
1006
>>> len(ticket_ids)
6
>>> ticket_ids[len(ticket_ids)-1]
1006
>>> ticket_ids[len(ticket_ids)/2]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ticket_ids[len(ticket_ids)/2]
TypeError: list indices must be integers or slices, not float
>>> ticket_ids[int(len(ticket_ids)/2)]
1004
>>> ticket_ids[1]
1002
>>> num = 4
>>> num
4
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> list(range(0))
[]
>>> 