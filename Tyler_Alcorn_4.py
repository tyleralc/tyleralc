#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint
count=0
rand_num=randint(1,10)
while True:
    guess= int(input())
    if guess>rand_num:
        count+=1
        print('Lower')
        continue
    elif guess<rand_num:
        count+=1
        print('Higher')
        continue
    elif guess==rand_num:
        count+=1
        break

print('You guessed corrrectly after', count, 'tries, Congrats!')


# In[ ]:





# In[ ]:




