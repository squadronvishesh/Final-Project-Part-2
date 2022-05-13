#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas as pd 
import numpy as np 
import seaborn as sns
data = pd.read_csv("/Users/visheshakshatpathak/Downloads/ep.csv")
#1. Understanding the data 
data.head()


# In[62]:


data.tail()


# In[63]:


data.shape


# In[64]:


data.nunique


# In[11]:


data.describe()


# In[65]:


data.columns


# In[66]:


data['Education Code'].unique() #to show unique values in a particular avenue.


# In[ ]:


#claeaning the dataset


# In[19]:


data.isnull().sum()


# In[67]:


#dropping the non important/empty entities
newdata= data.drop(['trCode'], axis=1)


# In[22]:


data.head()


# 

# In[23]:


# relationship analysis


# In[24]:


corelation = data.corr()


# In[35]:


sns.heatmap(corelation, xticklables=corelation.columns, yticklables=corelation.columns, annot=True)


# In[ ]:


#got errors while wokring with heatmaps


# In[36]:


sns.pairplot(data)


# In[75]:


#plotting histogram to get insights about the spread of data
sns.distplot(newdata['Workex Code'], bins=20)


# In[72]:


sns.catplot(x='Education Code', kind= 'box', data= newdata)


# In[74]:


sns.catplot(x='Workex Code', kind= 'box', data= newdata)

