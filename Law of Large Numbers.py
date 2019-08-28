#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from numpy.random import randn


# In[5]:


randn()


# In[13]:


import numpy as np
from numpy.random import randn
N = 500
counter = 0
for i in randn(N):
    if i > -1 and i < 1:
        counter = counter + 1
answer = (counter / N)*100
print(answer)
    


# In[19]:


Ns = [10, 1000, 100000, 1000000]
for N in Ns:
    y = 0
    for i in range(N):
        x = randn()
        if x <= 1 and x >= -1:
            y = y + 1
    m = y / N * 100   
    print(y, "observations out of a total of", str(N), "or", str(m) + "%", "is between 1 and -1.")
print("\n")
print("This shows a regression to mean as total observations increases.")


# In[ ]:





# In[20]:


Ns = [5, 500, 5000]
for N in Ns:
    y = 0
    for i in range(N):
        x = randn()
        if x >= -1 and x <= 1:
            y = y + 1
    m = (y/N)*100
    print(y, "observation out of a total of", str(N), "or", str(m) + "%", "is between 1 and -1.")
print("\n")
print("This exercise can show a regression to mean as total observations increase")


# In[69]:


import numpy as np
from numpy.random import randn

N = 10000
counter = 0
for i in randn(N):
    if (i > -1 and i < 1):
        counter = counter + 1
counter/N
        
        


# In[ ]:




