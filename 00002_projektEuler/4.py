#!/usr/bin/env python
# coding: utf-8

# In[1]:


upperlimit = 999
lowerlimit = 100

max_product = 0

for i in range(upperlimit, lowerlimit-1, -1):
    for j in range(i, lowerlimit-1, -1):
#         print i,j
        product = i*j
        
        if product < max_product:
            break
        number = product
        reverse = 0
        
        while(number != 0):
            reverse = reverse*10 + number%10
            number = number//10
        
        if (reverse == product) and (product > max_product):
            max_product = product

print max_product
