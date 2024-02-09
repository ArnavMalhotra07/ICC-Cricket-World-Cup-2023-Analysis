#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv(r'C:\Users\Arnav\OneDrive\Desktop\Python\Dataset\Fielding\most_catches.csv')
df1 = df.head()
df1


# In[13]:


colors = sns.color_palette('CMRmap',5)
bp = plt.bar(df1['Player'], df1['Ct'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df1['Ct'], label_type = 'edge', padding = 3)
plt.title('Most number of catches in the tournament')
plt.ylabel('Catches')
plt.xticks(rotation = 30)
plt.show()


# In[ ]:





# In[7]:


df = pd.read_csv(r'C:\Users\Arnav\OneDrive\Desktop\Python\Dataset\Fielding\most_catches_in_an_innings.csv')
df2 = df.head(10)
df2


# In[10]:


plt.plot(df2['Player'], df2['Ct Fi'], 'k-')
plt.plot(df2['Player'], df2['Ct Fi'], 'yo', markersize = 10)
plt.ylabel('Catches')
plt.title('Most number of catches in an inning')
plt.xticks(rotation = 30)
plt.xticks(fontsize = 7)


# In[12]:


colors = sns.color_palette('CMRmap',5)
bp = plt.bar(df1['Player'], df1['Ct/Inn'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df1['Ct/Inn'], label_type = 'edge', padding = 3)
plt.title('Best Catch/Inning ratio in the tournament')
plt.ylabel('Catches')
plt.xticks(rotation = 30)
plt.show()


# In[18]:


df = pd.read_csv(r'C:\Users\Arnav\OneDrive\Desktop\Python\Dataset\Fielding\most_dismissals.csv')
df3 = df.head()
df3


# In[22]:


colors = sns.color_palette('afmhot',5)
bp = plt.bar(df3['Player'], df3['Dis'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df3['Dis'], label_type = 'edge', padding = 3)
plt.title('Most number of dismissals by a wicketkeeper in the tournament')
plt.ylabel('Dismissals')
plt.xticks(rotation = 30)
plt.show()


# In[23]:


plt.plot(df3['Player'], df3['Max Dis Inns'], 'b-')
plt.plot(df3['Player'], df3['Max Dis Inns'], 'ro', markersize = 10)
plt.ylabel('Catches')
plt.title('Most number of dismissals by a wicketkeeper in an inning')
plt.xticks(rotation = 30)
plt.xticks(fontsize = 7)


# In[25]:


colors = sns.color_palette('viridis',5)
bp = plt.bar(df3['Player'], df3['Dis/Inn'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df3['Dis/Inn'], label_type = 'edge', padding = 3)
plt.title('Best Dismissal/Innings ration for wicketkeepers')
plt.ylabel('Dismissals')
plt.xticks(rotation = 30)
plt.show()


# In[34]:


plt.figure(figsize = (30,20))
#1
plt.subplot(2,3,1)
colors = sns.color_palette('CMRmap',5)
bp = plt.bar(df1['Player'], df1['Ct'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df1['Ct'], label_type = 'edge', padding = 3)
plt.title('Most number of catches in the tournament')
plt.ylabel('Catches')
plt.xticks(rotation = 30)
#2
plt.subplot(2,3,2)
plt.plot(df2['Player'], df2['Ct Fi'], 'k-')
plt.plot(df2['Player'], df2['Ct Fi'], 'yo', markersize = 10)
plt.ylabel('Catches')
plt.title('Most number of catches in an inning')
plt.xticks(rotation = 30)
plt.xticks(fontsize = 7)
#3
plt.subplot(2,3,3)
colors = sns.color_palette('CMRmap',5)
bp = plt.bar(df1['Player'], df1['Ct/Inn'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df1['Ct/Inn'], label_type = 'edge', padding = 3)
plt.title('Best Catch/Inning ratio in the tournament')
plt.ylabel('Catches')
plt.xticks(rotation = 30)
#4
plt.subplot(2,3,4)
colors = sns.color_palette('afmhot',5)
bp = plt.bar(df3['Player'], df3['Dis'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df3['Dis'], label_type = 'edge', padding = 3)
plt.title('Most number of dismissals by a wicketkeeper in the tournament')
plt.ylabel('Dismissals')
plt.xticks(rotation = 30)
#5
plt.subplot(2,3,5)
plt.plot(df3['Player'], df3['Max Dis Inns'], 'b-')
plt.plot(df3['Player'], df3['Max Dis Inns'], 'ro', markersize = 10)
plt.ylabel('Catches')
plt.title('Most number of dismissals by a wicketkeeper in an inning')
plt.xticks(rotation = 30)
plt.xticks(fontsize = 7)
#6
plt.subplot(2,3,6)
colors = sns.color_palette('viridis',5)
bp = plt.bar(df3['Player'], df3['Dis/Inn'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df3['Dis/Inn'], label_type = 'edge', padding = 3)
plt.title('Best Dismissal/Innings ration for wicketkeepers')
plt.ylabel('Dismissals')
plt.xticks(rotation = 30)
plt.savefig("Fielding_Analysis.pdf")


# In[ ]:




