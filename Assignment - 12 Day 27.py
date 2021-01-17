#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys


# In[4]:


list1 = (each*2 for each in range(100000))


# In[5]:


sys.getsizeof(list1)


# In[13]:


for each in list1:
    print(each)


# In[14]:


a = map(lambda x: 9/5*x+32, list1)


# In[16]:


sys.getsizeof(a)


# In[17]:


a = map(lambda x: 9/5*x+32, [1,2,3,4,5,6,76,7,7,8,89,99])


# In[18]:


sys.getsizeof(a)


# In[19]:


for each in a:
    print(each)


# In[ ]:




