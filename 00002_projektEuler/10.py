#!/usr/bin/env python
# coding: utf-8

# In[25]:


def primegenerator(limit):
    total = 0
    i = 2
    while (i < limit):
        if isprime(i):
            total = total + i
        i = i + 1
    return total

def isprime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True


# In[28]:


sumlimit = 2000000
primegenerator(sumlimit)


# In[ ]:




