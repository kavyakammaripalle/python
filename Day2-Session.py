#!/usr/bin/env python
# coding: utf-8

# In[2]:


#adding and eliminating white spaces
#strip() method is used to eliminate white spaces
a= "I am learning  python "
print(a.strip())


# In[11]:


#\t tab space
print("Kavya kiran\t software engineering\t python training")

#\n new line
print("kavya kiran\nsoftware engineering\npython training")


# In[30]:


#Numbers calculation
print(2+3)
print(3-8)
print(3*9)
print(5*8)
print(2**3)
print((2.5)**3)


# In[33]:


#zen of python
import this


# In[43]:


#Lists-collection of items in particular order-deonted by []
#indexing starts from 0,1,2....
laptop=['hp','lenovo','macbook','dell','alienware']
print(laptop[4])
print(laptop[1])
print(laptop[1].title())
print(laptop[1].upper())
print(laptop[1].lower())
#negative indexing starts from right side
print(laptop[-3])
print(laptop[-2].upper())


# In[61]:


#fstrings in lists
laptop=['hp','lenovo','macbook','dell','alienware']
a=f"my first laptop was {laptop[2]}"
b=f"my second laptop was {laptop[-5].upper()}"
print(a)
print(b)


# In[75]:


#Add an element in the list
laptop=['hp','lenovo','macbook','dell','alienware']
laptop[0]='hpspectra'#replaces the new element 
print(laptop)
laptop.append('hp spectra')#adds a new element
print(laptop)

#delete and element form the list
laptop=['hp','lenovo','macbook','dell','alienware']
del laptop[-3]
print(laptop)
laptop.pop()#deletes the last element in the list
print(laptop)
laptop.pop(1)
print(laptop)


# In[78]:


#Sorting of list
cars=['bmw','benz','hyundai','toyota', 'audi']
cars.sort()
print(cars)
cars.reverse()
print(cars)


# In[92]:


#Loops
friends=['ross','rachel','joey','chandler','monica']
for f in friends:
    print(f)#indentation
#Range is always exclusive
for i in range(1,10):
    print(i)


# In[ ]:




