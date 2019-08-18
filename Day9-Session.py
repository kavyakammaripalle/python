#!/usr/bin/env python
# coding: utf-8

# In[3]:


#class,objects,constructor,oops
#how to declare methods in a class
def sit(self,x,y):
    self.x=x
    self.y=y
#constructor: __init__
#deconstructor:__del__


# In[18]:


class Dog:
    """ method to model a dog"""
    def __init__(self,name,age): #constructor
        """initialize name and age attributes"""
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name} is now sitting")
    def stand(self):
        print(f"{self.name} is standing now")
mydog=Dog('rover',4)
print(f"my dogs name is {mydog.name}")
print(f"my dog is now {mydog.age} years old")
mypet=Dog('icy',1)
print(f"my dogs name is {mypet.name}")
print(f"my dog is now {mypet.age} years old")
mydog.name
mypet.age


# In[ ]:




