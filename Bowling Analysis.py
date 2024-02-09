#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


df = pd.read_csv(r'C:\Users\Arnav\Downloads\bowling.csv')
df1 = df.head()
df1


# In[22]:


colors = sns.color_palette('PRGn',5)
bp = plt.bar(df1['Player'], df1['Wkts'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df1['Wkts'], label_type = 'edge', padding = 3)
plt.title('Highest wicket takers of the tournamnet')
plt.ylabel('Wickets')
plt.xticks(rotation = 30)
plt.show()


# In[17]:


min250 = df[df['Balls']>=200]
df3 = min250.sort_values(by = 'Avg').head()
df3


# In[24]:


colors = sns.color_palette('tab10',5)
bp = plt.bar(df3['Player'], df3['Avg'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df3['Avg'], label_type = 'edge', padding = 3)
plt.title('Best bowling average in the tournamnet')
plt.ylabel('Average')
plt.xticks(rotation = 30)
plt.show()


# In[25]:


min250 = df[df['Balls']>=200]
df4 = min250.sort_values(by = 'Econ').head()
df4


# In[26]:


colors = sns.color_palette('inferno',5)
bp = plt.bar(df4['Player'], df4['Econ'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df4['Econ'], label_type = 'edge', padding = 3)
plt.title('Best bowling economy in the tournamnet')
plt.ylabel('Economy')
plt.xticks(rotation = 30)
plt.show()


# In[34]:


df5 = df.sort_values(by = 'Mdns', ascending = False)
df6 = df5.head(10)
df6


# In[52]:


plt.plot(df6['Player'], df6['Mdns'], 'g-')
plt.plot(df6['Player'], df6['Mdns'], 'yo', markersize = 10)
plt.ylabel('Maidens')
plt.title('Most number of maiden overs bowled')
plt.xticks(rotation = 30)
plt.xticks(fontsize = 7)


# In[54]:


min250 = df[df['Balls']>=200]
df7 = min250.sort_values(by = 'SR').head()
df7


# In[56]:


colors = sns.color_palette('turbo',5)
bp = plt.bar(df7['Player'], df7['SR'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df7['SR'], label_type = 'edge', padding = 3)
plt.title('Best bowling strike rates in the tournamnet')
plt.ylabel('SR')
plt.xticks(rotation = 30)
plt.show()


# In[58]:


df = pd.read_csv(r'C:\Users\Arnav\OneDrive\Desktop\Python\Dataset\most_four_wickets_in_an_innings.csv')
df8 = df.head()
df8


# In[61]:


plt.plot(df8['Player'], df8['4+'], 'k-')
plt.plot(df8['Player'], df8['4+'], 'ro', markersize = 10)
plt.ylabel('Wicketss')
plt.title('Most number of 4+ wicket hauls')
plt.yticks(np.arange(1,5,1))
plt.xticks(rotation = 30)
plt.xticks(fontsize = 7)


# In[78]:


df = pd.read_csv(r'C:\Users\Arnav\OneDrive\Desktop\Python\Dataset\Bowling\best_economy_rates_in_an_innings.csv')
df9 = df[df['Wkts']>=2].head()
df9


# In[80]:


colors = sns.color_palette('Wistia',5)
bp = plt.bar(df9['Player'], df9['Econ'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df9['Econ'], label_type = 'edge', padding = 3)
plt.title('Best economy rate in an inning (Mininimun 2 wickets)')
plt.ylabel('SR')
plt.yticks(np.arange(0,3,0.5))
plt.xticks(rotation = 30)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[88]:


plt.figure(figsize = (30,30))
#1
plt.subplot(3,3,1)
colors = sns.color_palette('PRGn',5)
bp = plt.bar(df1['Player'], df1['Wkts'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df1['Wkts'], label_type = 'edge', padding = 3)
plt.title('Highest wicket takers of the tournament')
plt.ylabel('Wickets')
plt.xticks(rotation = 30)
#2
plt.subplot(3,3,2)
colors = sns.color_palette('inferno',5)
bp = plt.bar(df4['Player'], df4['Econ'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df4['Econ'], label_type = 'edge', padding = 3)
plt.title('Best bowling economy in the tournament')
plt.ylabel('Economy')
plt.xticks(rotation = 30)
#3
plt.subplot(3,3,3)
colors = sns.color_palette('tab10',5)
bp = plt.bar(df3['Player'], df3['Avg'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df3['Avg'], label_type = 'edge', padding = 3)
plt.title('Best bowling average in the tournament')
plt.ylabel('Average')
plt.xticks(rotation = 30)
#4
plt.subplot(3,3,4)
plt.plot(df6['Player'], df6['Mdns'], 'g-')
plt.plot(df6['Player'], df6['Mdns'], 'yo', markersize = 10)
plt.ylabel('Maidens')
plt.title('Most number of maiden overs bowled')
plt.xticks(rotation = 30)
plt.xticks(fontsize = 7)
#5
plt.subplot(3,3,5)
colors = sns.color_palette('turbo',5)
bp = plt.bar(df7['Player'], df7['SR'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df7['SR'], label_type = 'edge', padding = 3)
plt.title('Best bowling strike rates in the tournament')
plt.ylabel('SR')
plt.xticks(rotation = 30)
#6
plt.subplot(3,3,6)
plt.plot(df8['Player'], df8['4+'], 'k-')
plt.plot(df8['Player'], df8['4+'], 'ro', markersize = 10)
plt.ylabel('Wicketss')
plt.title('Most number of 4+ wicket hauls')
plt.yticks(np.arange(1,5,1))
plt.xticks(rotation = 30)
plt.xticks(fontsize = 7)
#7
plt.subplot(3,3,7)
colors = sns.color_palette('Wistia',5)
bp = plt.bar(df9['Player'], df9['Econ'],
        color = colors,
        width = 0.6,
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.bar_label(bp, labels = df9['Econ'], label_type = 'edge', padding = 3)
plt.title('Best economy rate in an inning (Mininimun 2 wickets)')
plt.ylabel('Economy')
plt.yticks(np.arange(0,3,0.5))
plt.xticks(rotation = 30)
plt.savefig("Bowling_Analysis.pdf")


# In[ ]:




