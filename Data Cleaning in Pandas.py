#!/usr/bin/env python
# coding: utf-8

# In[116]:


import pandas as pd


# In[117]:


df=pd.read_excel("C:/Users/Online/Downloads/Customer Call List.xlsx")


# In[118]:


df


# In[119]:


df=df.drop(columns ="Not_Useful_Column")


# In[120]:


df


# In[121]:


# df['Last_Name']=df['Last_Name'].str.lstrip('...')
# df['Last_Name']=df['Last_Name'].str.lstrip('/')
# df['Last_Name']=df['Last_Name'].str.rstrip('_')
df['Last_Name']=df['Last_Name'].str.strip('123._/')


# In[122]:


df


# In[123]:


# df['Phone_Number']=df['Phone_Number'].str.replace('[^a-zA-Z0-9]','')
# df["Phone_Number"]=df["Phone_Number"].apply(lambda x:str(x))
# df["Phone_Number"]
# df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x)[0:3] + '-' + str(x)[3:6] + '-' + str(x)[6:10])
# df["Phone_Number"] 
# Replace 'nan--' or 'Na--' with an empty string
df["Phone_Number"] = df["Phone_Number"].str.replace('nan--', '')
df["Phone_Number"] = df["Phone_Number"].str.replace('Na--', '')
df


# In[124]:


df[['Street_Address','State','Zip_code']]=df['Address'].str.split(',',2,expand=True)


# In[125]:


df


# In[126]:


df['Paying Customer']=df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer']=df['Paying Customer'].str.replace('No','N')


# In[92]:


df


# In[93]:


df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('No','N')


# In[94]:


df


# In[102]:


df=df.replace('N/a','')
df=df.fillna('')


# In[103]:


df


# In[104]:


for x in df.index:
    if df.loc[x,"Do_Not_Contact"]=='Y':
        df.drop(x,inplace=True)


# In[105]:


df


# In[108]:


df=df.reset_index(drop=True)


# In[109]:


df


# In[ ]:




