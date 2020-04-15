#!/usr/bin/env python
# coding: utf-8

# In[44]:


def prime(n):
    count = 0
    i = 1
    while (True):
        i = i + 1
        if isprime(i):
            count = count + 1
            if count == n:
                return i

def isprime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True


# In[48]:


num = 10001

sos = prime(num)

print sos


# In[ ]:




