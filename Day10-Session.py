#!/usr/bin/env python
# coding: utf-8

# In[7]:


#classes:superclass-subclass
class A:
    v1='iam variable one'
    v2='iam variable two'
class B(A):
    pass
a=A()
a.v1
b=B()
b.v2   


# In[11]:


#Overwrite a variable
class A:
    v1='iam variable one'
    v2='iam variable two'
    v3='iam variable three'
    v4='iam variable four'
class B(A):
    v4='iam modified variable'
x=A()
x.v4
y=B()
y.v4


# In[13]:


class mom:
    v1='iam mom'
class dad:
    v2='iam dad'
class child(mom,dad):
    v3='iam child'
x=child()
x.v1
x.v2


# In[ ]:




