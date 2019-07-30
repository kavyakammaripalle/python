#!/usr/bin/env python
# coding: utf-8

# In[1]:


#To get length of the list
cars=['bmw','benz','toyota','audi']
len(cars)


# In[6]:


#Writing over a tuple
dimensions=(200,50)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions=(300,60)
print("modified dimensions:")
for dimension in dimensions:
    print(dimension)


# In[7]:


#Python styling guide
#pep 8-Pyhton Enhancement proposal(how to structure your code)
#1.Indentation
#2.Line length
#3.Blank Lines


# In[13]:


#if statements(conditional testing)
cars=['bmw','benz','toyota','audi']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
car='bmw'
car=='BMW'
car.upper()=='BMW'
car=='audi'


# In[22]:


#Dictionary data type(mutable)(collection of key-value pairs,Each key is connected to a value)
alien={'colour':'green','points':10}
print(alien['points'])
#Add key-value pairs in dictionary
alien['x-position']=0
alien['y-posiiton']=1
print(alien)


# In[ ]:





# In[ ]:




