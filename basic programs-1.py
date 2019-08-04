#!/usr/bin/env python
# coding: utf-8

# In[3]:


#print if given number is even or odd
num=int(input("Enter any number:"))
if num%2==0:
    print(f"The given integer {num} is an even number")
elif num%2!=0:
    print(f"The given integer {num} is an odd number")


# In[2]:


#print if given number is prime
num=int(input("enter a number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Given number is not a prime")
            break
        else:
            print("Given number is prime")
            break
else:
    print("given number is not prime")
            


# In[1]:


#how to find factorial in python
n=int(input("enter any number:"))
fact=1
if n<0:
    print("Cannot find factorial of negative numbers!")
elif n==0:
    print("Factorial of zero is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
print(f"Factorial of {n} is:")
print(fact)    


# In[ ]:





# In[ ]:




