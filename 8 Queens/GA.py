#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install geneticalgorithm


# In[14]:


import numpy as np
from geneticalgorithm import geneticalgorithm as ga

def diag_hit(myX,myY,otherX,otherY):
    supX=otherX
    supY=otherY
    while supX>=0 and supY>=0:
        if supX==myX and supY==myY:
            return 1
        supX-=1
        supY-=1
    supX=otherX
    supY=otherY
    while supX<=8 and supY<=8:
        if supX==myX and supY==myY:
            return 1
        supX+=1
        supY+=1
    supX=otherX
    supY=otherY
    while supX<=0 and supY<=8:
        if supX==myX and supY==myY:
            return 1
        supX-=1
        supY+=1
    supX=otherX
    supY=otherY
    while supX<=8 and supY<=0:
        if supX==myX and supY==myY:
            return 1
        supX+=1
        supY-=1
    return 0

def check_hit(myX,myY,otherX,otherY):
    hits = 0
    if myY==otherY:
        hits+=1
    elif diag_hit(myX,myY,otherX,otherY):
        hits+=1
    return hits
    

def f(X):
    index = 0
    failures = 0
    for row in X:
        index_aux = 0
        for row_aux in X:
            #print(row_aux)
            if index!=index_aux:
                failures += check_hit(index,row,index_aux,row_aux)
            index_aux +=1
        index+=1
    return failures

varbound=np.array([[1,8]]*8)

model=ga(function=f,dimension=8,variable_type='int',variable_boundaries=varbound)

model.run()


# In[ ]:





# In[ ]:




