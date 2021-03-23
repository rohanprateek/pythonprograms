# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:18:27 2021

@author: Rohan Prateek
"""
# Lab 6: In preparation for the NumPy Ex1 for this lab

import numpy as np

# String type with ASCII chars each take one byte
npStrDef = np.dtype([('dummy', 'S1')])
npChar = np.zeros(1, dtype=npStrDef)
print('\nAbout dtype char string')
print('Type: ', type(npChar))
print('Item Size: ', npChar.itemsize)
print('Value: ', npChar)

# String type with Unicode chars each take four bytes of size
# Becuase NumPy uses UTF-32 encoding for unicode strings
npUStrDef = np.dtype([('dummy', 'U1')])
npUChar = np.ones(1, dtype=npUStrDef)
print('\nAbout dtype unicode_')
print('Type: ', type(npUChar))
print('Item Size: ', npUChar.itemsize)
print('Value: ', npUChar)

# Structured datatype ref:https://numpy.org/doc/stable/user/basics.rec.html
# Creating a structured datatype using basic dtypes 
# Give char code for the 'name' element both U10 and S10 and observe the changes
npEmpData = np.array([('Emp1Name', 22), ('Emp2Name', 33)], 
                     dtype=[('name', 'U10'), ('age', np.ubyte)])
print('\nEmp data')
print('Type: ', type(npEmpData))
print('Size: ', npEmpData.size)
print('Strides: ', npEmpData.strides)
# Each Unicode char occupies 2 bytes of str len 10 = 20 + 20 = 40 bytes
# Each entry of age occupies one byte each 'i1', so total 80 + 2 = 82 bytes
print('nbytes: ', npEmpData.nbytes) # prints 82 bytes

print('npEmpData: ', npEmpData)

print(npEmpData[0])
print(npEmpData[1])

npEmpData[0]['name'] = 'NewEmp1Na'
npEmpData[0]['age'] = 111
print(npEmpData[0])
print(npEmpData[1])

numEmp = 1

npEmpDataDef = np.dtype([('id', np.uint), ('name', 'S64'), 
                         ('age', np.ubyte), ('height', np.ubyte)])

npEmpArr = np.zeros(numEmp, dtype=npEmpDataDef)

print(npEmpArr)

            