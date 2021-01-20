#!/usr/bin/env python
# coding: utf-8

# Write a Python program to print even numbers in a list.
# Sample:
# Input: list1 = [12, 3, 55, 6, 144]
# Output: [12, 6, 144]
# Input: list2 = [2, 10, 9, 37]
# Output: [2, 10]

# In[2]:


list1=[12,3,55,6,144]
list2=[2,10,9,37]
even=[]
for value in list1:
    if(value%2==0):
        even.append(value)
print(even)        


# In[5]:


even2=[]
for value in list2:
    if value%2==0: even2.append(value)
print(even2)        


# Write a program to print the following pattern
#     1
#    22
#   333
#  4444
# 55555

# In[6]:


n=int(input("Enter a number:"))
for i in range(1,n+1):
    print((n-i)*" ",i*str(i))


# In[ ]:




