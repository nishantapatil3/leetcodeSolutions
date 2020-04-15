#!/usr/bin/env python
# coding: utf-8

# In[32]:


def multiples35(num):
    total = 0
    for i in range(1, num):
        if (i%3 == 0) or (i%5 == 0):
            total = total + i
    return total


# In[34]:


num = 1000
multiples35(num)


# In[ ]:




