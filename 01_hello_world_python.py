# -*- coding: utf-8 -*-
"""
@author: Rajasekhar Mugada
@brief : Python basics
"""

#Python variables

#strings
dt_str = "Hello world ! - Python"

#numbers : int/long/float/complx
dt_num1 = 123.45
dt_num2 = 12 + 3.45j

#list
dt_list = ['hi', 1, 2, 3, 4.56]

#tuple
dt_tuple = ('hi', 1, 2, 3, 4.56) 

#Dictionary
dt_dict = {'key':'value', 'id':2, 10:1234}

#set : add, union, intersect, difference, clear
dt_set = {'hi', 1, 2, 3, 4.56, 'hi', 1, 2, 3, 4.56}


print ("String : ", dt_str )
print ("Numbers : float ex: ", dt_num1, " complex ex: ", dt_num2 )
print ("List : ", dt_list, "  list's 0th index element : ", dt_list[0])
print ("Tuple : ", dt_tuple, "  tuple's 0th index element : ", dt_tuple[0])
print ("Dictionary : ", dt_dict, "  dictionary value for key 10 : ", dt_dict[10])
print ("Set : ", dt_set)
