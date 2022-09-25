Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ticket_ids = [1001, 1006, 1003, 1004, 1005, 1007, 1008, 1009, 1010, 1011, [1008, 1009, 1010, 1011]]
>>> 
>>> ticket_ids
[1001, 1006, 1003, 1004, 1005, 1007, 1008, 1009, 1010, 1011, [1008, 1009, 1010, 1011]]
>>> 
>>> ticket_ids[len(ticket_ids)-1]
[1008, 1009, 1010, 1011]
>>> 
>>> ticket_ids[len(ticket_ids)-1][-1]
1011
>>> #ticket_ids[len(ticket_ids)-1][len(ticket_ids[len(ticket_ids)-1])]
>>> len(ticket_ids[len(ticket_ids)-1])
4
>>> len(ticket_ids[len(ticket_ids)-1])-1
3
>>> ticket_ids[len(ticket_ids)-1][len(ticket_ids[len(ticket_ids)-1])-1]
1011
>>> ticket_ids[len(ticket_ids)-1][int(len(ticket_ids[len(ticket_ids)-1])/2)]
1010
>>> ticket_ids = [1001, 1006, 1003, 1004, 1005, 1007, 1008, 1009, 1010, 1011]
>>> ticket_ids
[1001, 1006, 1003, 1004, 1005, 1007, 1008, 1009, 1010, 1011]
>>> 
>>> ticket_ids.pop()
1011
>>> ticket_ids
[1001, 1006, 1003, 1004, 1005, 1007, 1008, 1009, 1010]
>>> ticket_ids.pop(5)
1007
>>> ticket_ids
[1001, 1006, 1003, 1004, 1005, 1008, 1009, 1010]

>>> 