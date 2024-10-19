#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# In[34]:


data = pd.read_csv("crop_yield.csv")


# In[35]:


data.head(n=10)


# In[36]:


data.info()


# In[37]:


data.describe()


# In[41]:


data = data[['Soil_Type', 'Crop', 'Rainfall_mm', 'Temperature_Celsius',
       'Fertilizer_Used', 'Irrigation_Used', 'Weather_Condition',
       'Days_to_Harvest', 'Yield_tons_per_hectare']]
data.head()


# In[43]:


data.isna().sum()


# In[45]:


data


# In[46]:


data.hist(bins=60, figsize =(20,10))
plt.show()


# In[47]:


ax = data['Crop'].value_counts().plot(kind='pie', title='Crop Count')
plt.show()


# In[48]:


plt.figure(figsize=(10, 6))
ax = sns.boxplot(x='Fertilizer_Used', y='Yield_tons_per_hectare', data=data)
ax.set_title('Yield by Fertilizer Usage')
ax.set_xlabel('Fertilizer Used')
ax.set_ylabel('Yield (tons per hectare)')

plt.show()


# In[50]:


sns.kdeplot(data['Yield_tons_per_hectare'], fill=True)
plt.title('Yield Distribution (Tons per Hectare)')
plt.show()


# In[51]:


sns.boxplot(x = "Soil_Type", y = "Yield_tons_per_hectare", data = data)


# In[ ]:




