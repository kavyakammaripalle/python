#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Accepting input from the user
message=input("what is your name:")
print(message)
print(f"Good morning, {message}.how are you?")


# In[1]:


Age=input("how old are you? :")
Age=int(Age)
if Age<18:
    print("you're a minor")
else:
    print("you're a major")


# In[3]:


#To find if a given number is even or odd:
num=input("enter any number:")
num=int(num)
if num%2==0:
    print(f"The given number {num} is an even number")
else:
    print(f"The given number {num} is an odd number")


# In[6]:


#introduction to  while loops
#(if condition is true it will execute the program or else it will fail)
number=4
while number<=10:
    print(number)
    number+=2


# In[2]:


#Letting the user when to quit
prompt="\n tell me something:"
prompt+="\n Quit to end the program"
message=""
while message!='quit':
    message=input(prompt)
    print(message)


# In[ ]:





# In[ ]:




