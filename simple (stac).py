#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore') 


# In[12]:


start= {'Car': ['Audi', 'BMW', 'Mercedes'],
        'Count': [124, 98, 113]}




# In[13]:


start


# In[14]:


c=sns.barplot(start,x="Car",y="Count",palette="coolwarm")


# In[15]:


total = sum(start["Count"])
RF= [count / total for count in start['Count']]


# In[16]:


ML= ['Audi', 'BMW', 'Mercedes']


# In[17]:


p=plt.pie(RF,shadow=True,labels=ML)


# In[18]:


e1=[0.1 ,0.1,0.1 ]
p=plt.pie(RF,shadow=True,explode=e1,labels=ML)


# In[28]:


start2= {'Name': ['Arnak', 'Chetya', 'Balu','Sholk'],
        'Marks': [70,80,88,84]}


# In[29]:


start


# In[30]:


start2


# In[32]:


b1=sns.barplot(start2,x='Name',y='Marks',palette="plasma")


# In[33]:


p1=plt.pie(start2['Marks'])


# In[40]:


ml2= ['Arnak', 'Chetya', 'Balu','Sholk']
e2=[0.1,0,0.1,0]
p1=plt.pie(start2['Marks'],labels=ml2,explode=e2,colors=['skyblue', 'lightcoral', 'lightgreen','pink'])


# In[ ]:




