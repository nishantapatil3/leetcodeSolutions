#!/usr/bin/env python
# coding: utf-8

# In[22]:


def sumofsquares(n):
    total = 0
    for i in range(1, n+1):
        total = total + i**2
    return total

def squareofsums(n):
    return (n*(n+1)/2)**2


# In[23]:


num = 100

sos = sumofsquares(num)
sos2 = squareofsums(num)

print sos
print sos2
print sos2-sos


# In[ ]:




