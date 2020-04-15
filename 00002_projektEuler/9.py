#!/usr/bin/env python
# coding: utf-8

# In[11]:


def findtriplet(total):
    for c in range(1, total):
        for b in range(1, c):
            for a in range(1, b):
                if a*a + b*b == c*c:
                    if a+b+c == total:
                        return a, b, c


# In[12]:


findtriplet(1000)


# In[ ]:




