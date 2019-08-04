#!/usr/bin/env python
# coding: utf-8

# In[2]:


#empty dictionary
alien_0={}
alien_0['colour']='green'
alien_0['points']=5
print(alien_0)


# In[6]:


#modifying values in a dictionary
alien={'color':'green','points':'10'}
print(f"The alien is in {alien['color']} colour with {alien['points']} points")
alien['colour']='red'
print(f"\n The alien is now in {alien['colour'].title()} colour ")


# In[9]:


#Removing key-values in a dictionary
alien={'color':'green','points':'10'}
print(alien)
del alien['points']
print(alien)


# In[21]:


#using get() method
alien={'color':'green','speed':'10'}
print(alien)
message=alien.get('points','no point value assigned')
print(message)


# In[27]:


#Looping through a dict
user={
    'username':'kavya_27',
    'fname':'kavya',
    'lname':'kiran'
}

for key,value in user.items():
    print(f"\n key:{key}")
    print(f"value:{value}")


# In[28]:


#functions(def)
#doc strings""" """
def greet_user(): 
    """Defining a function"""
    print("hello")
#calling function
greet_user()


# In[33]:


def greet_user(username):
    """ passing parameters"""
    print(f"hello,{username.title()}")
greet_user('kavya')   #passing arguments


# In[ ]:





# In[ ]:





# In[ ]:




