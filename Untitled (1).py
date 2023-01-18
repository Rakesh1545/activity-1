#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


# In[2]:


df=pd.read_excel('Bank_Personal_Loan_Modelling.xlsx')
df


# In[6]:


df.drop(['ID','ZIP Code'],axis=1,inplace=True)


# In[7]:


df


# In[8]:


X=df.iloc[:,:-5]
y=df.iloc[:,-5]


# In[9]:


y


# In[10]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)


# In[11]:


classifier=RandomForestClassifier()
classifier.fit(X_train,y_train)


# In[12]:


y_pred=classifier.predict(X_test)


# In[13]:


from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,y_pred)


# In[14]:


score


# In[15]:


from sklearn.linear_model import LogisticRegression


# In[16]:


regressor=LogisticRegression()
regressor.fit(X_train,y_train)


# In[17]:


y_pred=regressor.predict(X_test)


# In[18]:


score


# In[19]:


pickle_out = open("classifier.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()


# In[24]:


classifier.predict([[1,2,3,4,5,6,7]])


# In[ ]:





# In[ ]:




