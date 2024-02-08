#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv(r'C:\Users\Arnav\Downloads\most_runs.csv')
df1 = df.head()
df1


# In[4]:


x = df1['Player']
y = df1['Runs']


# In[5]:


def addlabels1(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])


# In[6]:


colors = sns.color_palette('viridis', 5)
plt.bar(x, y,
        color = colors)
addlabels1(x,y)
plt.ylabel('Runs')
plt.xticks(rotation = 45)
plt.xlabel('Player Name')
plt.title('Top 5 run scorers of the tournament')
plt.show()


# In[7]:


df2 = df.sort_values(by = ['HS'], ascending = False)
df3 = df2.head()
df3


# In[8]:


x1 = df3['Player']
y1 = df3['HS']
print(x1)
print(y1)


# In[9]:


colors = sns.color_palette('magma',5)
plt.barh(x1,y1,color = colors)
for index,value in enumerate(y1):
    plt.text(value,index, str(value))
    plt.xlabel('Runs')
    plt.ylabel('Players')
    plt.xticks(np.arange(0,250,25))
    plt.title('Top 5 scores of the tournament')
plt.show()


# In[10]:


df4 = df.sort_values(by = ['Avg'], ascending = False)
df5 = df4.head()
df5


# In[11]:


x2 = df5['Player']
y2 = df5['Avg']
print(x2)
print(y2)


# In[12]:


colors = sns.color_palette('magma',5)
colors = sns.color_palette('magma',5)
bp = plt.bar(x2,y2,color = colors)
plt.bar_label(bp,labels = y2,label_type = 'edge',padding = 3)
plt.xticks(rotation = 30)


# In[16]:


df6 = df.sort_values(by = ['SR'], ascending = False)
df7 = df6[df6['Runs']>=300]
df8 = df7.head()
df8


# In[17]:


x3 = df8['Player']
y3 = df8['SR']


# In[18]:


colors = sns.color_palette('magma',5)
bp = plt.bar(x3,y3,color = colors)
plt.bar_label(bp,labels = y3,label_type = 'edge',padding = 3)
plt.xticks(rotation = 30)


# In[29]:


df9 = df.sort_values(by = ['50'],ascending = False).head()
df9


# In[48]:


x4 = df9['Player']
y4 = df9['50']


# In[49]:


plt.stem(x4,y4,
         linefmt = 'k--',
        basefmt = 'k--')
plt.xticks(rotation=30)
plt.ylabel('Number of times')
plt.title('Most Half centuries in the tournament')
plt.show()


# In[40]:


df10 = df.sort_values(by = ['100'],ascending = False).head()
df10


# In[46]:


x5 = df10['Player']
y5 = df10['100']


# In[50]:


plt.stem(x5,y5,
        basefmt = 'k-')
plt.xticks(rotation=30)
plt.ylabel('Number of times')
plt.title('Most centuries in the tournament')
plt.show()


# In[54]:


df11 = df.sort_values(by = ['4s'],ascending = False).head()
df11


# In[55]:


x6 = df11['Player']
y6 =df11['4s']


# In[56]:


colors = sns.color_palette('magma',5)
bp = plt.bar(x6,y6,color = colors)
plt.bar_label(bp,labels = y6,label_type = 'edge',padding = 3)
plt.xticks(rotation = 30)


# In[60]:


df12 = df.sort_values(by = ['6s'],ascending = False).head()
df12


# In[63]:


x7 = df12['Player']
y7 =df12['6s']


# In[64]:


colors = sns.color_palette('magma',5)
bp = plt.bar(x7,y7,color = colors)
plt.bar_label(bp,labels = y7,label_type = 'edge',padding = 3)
plt.xticks(rotation = 30)


# In[77]:


df = pd.read_csv(r'C:\Users\Arnav\Downloads\most_runs_came_from_boundry_in_an_innings.csv')
z = df.head()
z


# In[80]:


x8 = z['Player']
y8 = z['4+6']


# In[81]:


colors = sns.color_palette('magma',5)
bp = plt.bar(x8,y8,color = colors)
plt.bar_label(bp,labels = y8,label_type = 'edge',padding = 3)
plt.xticks(rotation = 30)


# In[86]:


plt.figure(figsize = (34,30))
#1
plt.subplot(3,3,1)
colors = sns.color_palette('viridis', 5)
plt.bar(x, y,
        color = colors,
        width = 0.6, 
        edgecolor = 'black',
        linewidth = 1,
        linestyle = '-')
addlabels1(x,y)
plt.ylabel('Runs')
plt.xticks(rotation = 30)
plt.title('Highest run scorers of the tournament')
#2
plt.subplot(3,3,2)
colors = sns.color_palette('gist_earth',5)
plt.barh(x1,y1,color = colors, 
        edgecolor = 'black',
        linewidth = 1,
        linestyle = '-')
for index,value in enumerate(y1):
    plt.text(value,index, str(value))
    plt.xlabel('Runs')
    plt.xticks(np.arange(0,250,25))
    plt.title('Best scores of the tournament')
#3
plt.subplot(3,3,3)
colors = sns.color_palette('magma',5)
bp = plt.bar(x2,y2,color = colors,
             width = 0.6,
            edgecolor = 'black',
        linewidth = 1,
        linestyle = '-')
plt.bar_label(bp,labels = y2,label_type = 'edge',padding = 3)
plt.xticks(rotation = 30)
plt.title('Best averages in the tournament')
#4
plt.subplot(3,3,4)
colors = sns.color_palette('plasma',5)
bp = plt.bar(x3,y3,color = colors,
            width = 0.6,
            edgecolor = 'black',
        linewidth = 1,
        linestyle = '-')
plt.bar_label(bp,labels = y3,label_type = 'edge',padding = 3)
plt.ylabel('Strike Rate')
plt.title('Best strike rates in the tournament (minimum 300 runs)')
plt.xticks(rotation = 30)
#5
plt.subplot(3,3,5)
plt.stem(x4,y4,
         linefmt = 'k-',
        basefmt = 'k-')
plt.xticks(rotation=30)
plt.ylabel('Number of times')
plt.title('Most half centuries in the tournament')
#6
plt.subplot(3,3,6)
plt.stem(x5,y5,
        basefmt = 'k-')
plt.xticks(rotation=30)
plt.ylabel('Number of times')
plt.title('Most centuries in the tournament')
#7
plt.subplot(3,3,7)
colors = sns.color_palette('Spectral',5)
bp = plt.bar(x6,y6,
             color = colors,
            width = 0.6,
            edgecolor = 'black',
        linewidth = 1,
        linestyle = '-')
plt.bar_label(bp,labels = y6,label_type = 'edge',padding = 3)
plt.xticks(rotation = 30)
plt.ylabel('Number of 4s')
plt.title('Highest boundary hitters')
#8
plt.subplot(3,3,8)
colors = sns.color_palette('cividis',5)
bp = plt.bar(x7,y7,
             color = colors,
            width = 0.6,
            edgecolor = 'black',
        linewidth = 1,
        linestyle = '-' )
plt.bar_label(bp,labels = y7,label_type = 'edge',padding = 3)
plt.xticks(rotation = 30)
plt.ylabel('Number of Sixes')
plt.title('Most number of sixes')
#9
plt.subplot(3,3,9)
colors = sns.color_palette('gnuplot',5)
bp = plt.bar(x8,y8,
             color = colors,
            width = 0.6,
            edgecolor = 'black',
        linewidth = 1,
        linestyle = '-')
plt.bar_label(bp,labels = y8,label_type = 'edge',padding = 3)
plt.xticks(rotation = 30)
plt.ylabel('Runs')
plt.title('Most runs coming through boundaries in a single innings')
plt.savefig("Batting_Analysis.pdf")


# In[ ]:





# In[ ]:





# In[ ]:




