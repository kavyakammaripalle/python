#!/usr/bin/env python
# coding: utf-8

# In[10]:


#working with for loops
magicians=['david','alice','carolina']
print(magicians) #prints the list
for m in magicians:
    print(m)     #prints the content in the list
for m in magicians:
    print(f"That was a great trick,{m.title()}.\nI cant wait to see your next trick,{m.title()}.\n")


# In[11]:


#making numerical lists
for value in range(1,5):
    print(value)


# In[12]:


#using range to make list of numbers
num=list(range(1,50))
print(num)


# In[16]:


#print even and odd numbers
even_num=list(range(2,50,2))
print(even_num)
odd_num=list(range(1,50,2))
print(odd_num)


# In[18]:


#print squares of given list of numbers
squares=[]
for value in range(1,10):
    square=value**2
    squares.append(square)
print(squares)


# In[20]:


a=[]
for value in range(1,10):
    ab=value**3
    a.append(ab)
print(a)


# In[26]:


#simple statistics with a list of numbers
numbers=[1,34,50,67,100,2,4,76,99,1000]
print(max(numbers))
print(min(numbers))
print(sum(numbers))


# In[27]:


#slicing of lists
players=['charles','martina','michael','florence','ella']
print(players[1:4])


# In[ ]:




