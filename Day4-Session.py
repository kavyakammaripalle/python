#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Tuple datatype(immutable)-denoted by ()
t1=()
print(t1)


# In[7]:


t2=('one','two','three')
print(t2)
for t in t2:
    print(t)


# In[9]:


#convert list into tuple and vice-versa
l1=[1,2,3,4,5,6]
a=tuple(list(l1))
print(a)
t1=(1,2,3,4,5,6)
b=list(tuple(t1))
print(b)


# In[11]:


#concatenation of tuple
t1=('a','b','c','d','e')
t2=('d','c','b','a')
t3=t2+t1
print(t3)


# In[24]:


#slicing of tuple
t=('kavya','kiran','karthi','surekha')
print(t[1:3])
print(t[1:])#print from index 1 till the end
print(t[0:])
print(t[::-1])#reverse the tuple
for x in t:
    print(x)


# In[31]:


t4=('kavya','kiran','karthi','surekha')
del t4


# In[ ]:





# In[ ]:




