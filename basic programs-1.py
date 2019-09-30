#!/usr/bin/env python
# coding: utf-8

# In[3]:


#print if given number is even or odd
num=int(input("Enter any number:"))
if num%2==0:
    print(f"The given integer {num} is an even number")
elif num%2!=0:
    print(f"The given integer {num} is an odd number")


# In[4]:


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


# In[30]:


#fibonacci series of a given number
num=int(input("enter the number:"))
def fib(n):
    x=0
    y=1
    if n<0:
        print("invalid number")
    elif n==0 or n==1:
        print(x)
    else:
        print(x)
        print(y)
    
        for i in range(2,n):
            z=x+y
            x=y
            y=z
            print(z)
        
fib(num)
    
        


# In[ ]:



        


# 

# In[2]:


#amstrong 
number=int(input("enter a number :"))
sum=0
temp=number
while(temp>0):
    digit=temp%10
    sum+=digit**3
    temp//=10
if number==sum:
    print("Amstrong number")
else:
    print("not an amstrong number")



# In[5]:


#Reverse a string
s=input("Enter anything and i will reverse it")
def rev(s):
    return s[::-1]
rev(s)


# In[ ]:


#sum of n digits
n=int(input("Enter any number:"))
def digits(n):
    sum=0
    while(n>0):
        reminder=n%10
        sum=sum+reminder
        n=n//10
        return sum
digits(n)

