#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to add two numbers using class and object.
# (Take both numbers as input from the user)

# In[1]:


class addition:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def add(self):
        print("{}+{}={}".format(self.a,self.b,self.a+self.b))

num1=int(input("Enter num1 :"))    
num2=int(input("Enter num2 :"))
obj=addition(num1,num2)

obj.add()
        


# # Define a function swap that should swap two values and print the swapped variables outside the Swap function
# 

# In[9]:


a=10
b=20
def swap():
    global a,b
    a,b= b,a

print("Value of a before swap:",a)
print("Value of b before swap:",b)
swap()
print("Value of a after swap:",a)
print("Value of b after swap:",b)


# In[ ]:




