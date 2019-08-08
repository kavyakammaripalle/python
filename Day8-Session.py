#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Functions
def courses():
    """Display the courses"""
    print("'C','C++','Java','Python'")

courses()


# In[2]:


def greet(username):
    print(f"Hello, Good Morning {username.title()}")
        
greet(input("Enter a name:"))


# In[9]:


#passing argument types:positional,keyword
def describe_pet(_type,name):
    print(f"I have a {_type}")
    print(f"My {_type}'s name is {name}")

describe_pet('golden retriever','Rover')#POSITIONAL
describe_pet(name='Astro',_type='husky')#keyword


# In[11]:


#Default values
def describe_pet(_type,name='X'):
    print(f"I have a {_type}")
    print(f"My {_type}'s name is {name}")
describe_pet('husky','Y')


# In[ ]:




