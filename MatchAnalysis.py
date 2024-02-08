#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df1 = pd.read_csv(r'C:\Users\Arnav\OneDrive\Documents\pyProj.csv')
df1 = df1.set_index('Match_No')
df1.head()


# In[3]:


plt.figure(figsize=(4,4))
textprops = {'fontsize' : 14,
            'color' : 'k'}
wedgeprops = {'linewidth' : 2,
             'linestyle' : '-',
             'edgecolor' : 'k'}
plt.pie(df1['Choice'].value_counts(), labels=df1['Choice'].value_counts().index,
        autopct='%1.1f%%',
        startangle=90,
        colors=['#66b3ff', '#99ff99'],
        textprops = textprops,
        wedgeprops = wedgeprops
       )
plt.title('Teams winning toss and deciding to Ball or Bat')
plt.show()


# In[4]:


toss1 =  df1[((df1['Toss'] == df1['Team_1']) | (df1['Toss'] == df1['Team_2'])).values &
           ((df1['Choice'] == 'Ball') | (df1['Choice'] == 'Bat')).values ]
toss1


# In[5]:


toss_Won = toss1['Toss'].value_counts()
toss_Won


# In[6]:


colors = sns.color_palette('viridis', len(toss_Won))
plt.bar(toss_Won.index, toss_Won, 
        color = colors,
        width = 0.6, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,8,1))
plt.xlabel('Teams')
plt.ylabel('Number')
plt.title('Teams winning toss')
plt.show()


# In[7]:


toss1 =  df1[((df1['Toss'] == df1['Team_1']) | (df1['Toss'] == df1['Team_2'])).values &
           (df1['Choice'] == 'Ball').values ]
toss_Won_and_ball = toss1['Toss'].value_counts()
print(toss_Won_and_ball)
colors = sns.color_palette('viridis', len(toss_Won_and_ball))
plt.bar(toss_Won.index, toss_Won, 
        color = colors,
        width = 0.6, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,8,1))
plt.xlabel('Teams')
plt.ylabel('Number')
plt.title('Teams winning toss and chose to ball')
plt.show()


# In[8]:


toss1 =  df1[((df1['Toss'] == df1['Team_1']) | (df1['Toss'] == df1['Team_2'])).values &
           (df1['Choice'] == 'Bat').values ]
toss_Won_and_bat = toss1['Toss'].value_counts()
print(toss_Won_and_bat)
colors = sns.color_palette('viridis', len(toss_Won_and_bat))
plt.bar(toss_Won_and_bat.index, toss_Won_and_bat, 
        color = colors,
        width = 0.6, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,4,1))
plt.xlabel('Teams')
plt.ylabel('Number')
plt.title('Teams winning toss and chose to bat')
plt.show()


# In[9]:


league_stage = df1.drop([46,47,48], axis = 0, inplace = False)


# In[10]:


most_wins = league_stage['Winner'].value_counts()
most_wins


# In[11]:


plt.plot(most_wins.index, most_wins,'g-')
plt.plot(most_wins.index, most_wins,'bo')
plt.show()


# In[12]:


filtered_data1 = df1[
    ((df1['Toss'] == df1['Team_1']).values | (df1['Toss'] == df1['Team_2'])).values &   # Won the toss
    (df1['Choice'] == 'Ball').values &                                          # Elected to bowl
    (df1['Innings2_Run']<df1['Innings1_Run'] ).values                                     # Wickets equal to 10
]

filtered_data1.drop(35, axis = 0, inplace = True)
filtered_data1


# In[13]:


toss_counts = filtered_data1['Toss'].value_counts()
toss_counts


# In[14]:


plt.figure(figsize = (12,4))
colors = sns.color_palette('viridis', len(toss_counts))
plt.bar(toss_counts.index, toss_counts, 
        color = colors,
        width = 0.6, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,5,1))
plt.xlabel('Teams')
plt.ylabel('Number')
plt.title('Teams elected to bowl and lost')
plt.show()


# In[15]:


filtered_data2 = df1[
    ((df1['Toss'] == df1['Team_1'])| (df1['Toss'] == df1['Team_2'])).values &   # Won the toss
    (df1['Choice'] == 'Bat').values &                                          # Elected to bat
    #(df1['Innings1_Run'] >= 300).values &                                     
    (df1['Winner'] == df1['Toss']).values                                     #won the game
]

filtered_data2


# In[16]:


tw_bf_mw= filtered_data2['Winner'].value_counts()
tw_bf_mw


# In[17]:


plt.figure(figsize = (8,4))
colors = sns.color_palette('husl', len(toss_counts))
plt.bar(tw_bf_mw.index, tw_bf_mw, 
        color = colors,
        width = 0.4, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,4,1))
plt.xlabel('Teams')
plt.ylabel('Number of wins')
plt.title('Teams elected to bat and won')
plt.show()


# In[18]:


filtered_data3 = df1[
    ((df1['Toss'] == df1['Team_1'])| (df1['Toss'] == df1['Team_2'])).values &   # Won the toss
    (df1['Choice'] == 'Ball').values &                                          # Elected to ball
    #(df1['Innings1_Run'] >= 300).values &                                     
    (df1['Winner'] == df1['Toss']).values                                     #won the game
]
filtered_data3


# In[19]:


tw_blf_mw= filtered_data3['Winner'].value_counts()
tw_blf_mw


# In[20]:


plt.figure(figsize = (8,4))
colors = sns.color_palette('husl', len(toss_counts))
plt.bar(tw_blf_mw.index, tw_blf_mw, 
        color = colors,
        width = 0.4, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,4,1))
plt.xlabel('Teams')
plt.ylabel('Number of wins')
plt.title('Teams elected to ball and won')
plt.show()


# In[21]:


filtered_data4 = df1[
    ((df1['Toss'] == df1['Team_1'])| (df1['Toss'] == df1['Team_2'])).values &   # Won the toss
    (df1['Choice'] == 'Bat').values &                                          # Elected to bat                                   
    (df1['Winner'] != df1['Toss']).values                                     #lost the game
]

filtered_data4


# In[22]:


tw_bf_ml= filtered_data4['Toss'].value_counts()
tw_bf_ml


# In[23]:


plt.figure(figsize = (8,4))
colors = sns.color_palette('husl', len(toss_counts))
plt.bar(tw_bf_ml.index, tw_bf_ml, 
        color = colors,
        width = 0.4, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,4,1))
plt.xlabel('Teams')
plt.ylabel('Number of losses')
plt.title('Teams elected to bat and lost')
plt.show()


# In[ ]:





# In[32]:


plt.figure(figsize = (22,24))
plt.subplot(4,3,1)
#1
colors = sns.color_palette('viridis', len(toss_Won))
plt.bar(toss_Won.index, toss_Won, 
        color = colors,
        width = 0.6, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,8,1))
plt.xlabel('Teams')
plt.ylabel('Number')
plt.title('Teams winning toss')
#2
plt.subplot(4,3,2)
plt.pie(df1['Choice'].value_counts(), labels=df1['Choice'].value_counts().index,
        autopct='%1.1f%%',
        startangle=90,
        colors=['#66b3ff', '#99ff99'],
        textprops = textprops,
        wedgeprops = wedgeprops)
plt.title('Teams winning toss and deciding to Ball or Bat')
#3
plt.subplot(4,3,3)
colors = sns.color_palette('viridis', len(toss1))
plt.bar(toss_Won_and_ball.index, toss_Won_and_ball, 
        color = colors,
        width = 0.6, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,8,1))
plt.xlabel('Teams')
plt.ylabel('Number')
plt.title('Teams winning toss and chose to ball')
#4
plt.subplot(4,3,4)
colors = sns.color_palette('viridis', len(toss_Won_and_bat))
plt.bar(toss_Won_and_bat.index, toss_Won_and_bat, 
        color = colors,
        width = 0.6, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,5,1))
plt.xlabel('Teams')
plt.ylabel('Number')
plt.title('Teams winning toss and chose to bat')
#5
plt.subplot(4,3,5)
plt.plot(most_wins.index, most_wins,'g-')
plt.plot(most_wins.index, most_wins,'bo')
plt.yticks(np.arange(1,10,1))
plt.title('Most wins in league stages')

#6
plt.subplot(4,3,6)
colors = sns.color_palette('husl', len(toss_counts))
plt.bar(tw_blf_mw.index, tw_blf_mw, 
        color = colors,
        width = 0.4, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,4,1))
plt.xlabel('Teams')
plt.ylabel('Number of wins')
plt.title('Teams elected to bowl and won')
plt.xlabel('Teams')
plt.ylabel('Number of wins')
#7
plt.subplot(4,3,7)
colors = sns.color_palette('magma', len(toss_counts))
plt.bar(toss_counts.index, toss_counts, 
        color = colors,
        width = 0.6, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,5,1))
plt.xlabel('Teams')
plt.ylabel('Number of losses')
plt.title('Teams elected to bowl and lost')
#8
plt.subplot(4,3,8)
colors = sns.color_palette('rocket', len(toss_counts))
plt.bar(tw_bf_mw.index, tw_bf_mw, 
        color = colors,
        width = 0.4, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,4,1))
plt.xlabel('Teams')
plt.ylabel('Number of wins')
plt.title('Teams elected to bat and won')
#9
plt.subplot(4,3,9)
colors = sns.color_palette('viridis', len(toss_counts))
plt.bar(tw_bf_ml.index, tw_bf_ml, 
        color = colors,
        width = 0.4, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,4,1))
plt.xlabel('Teams')
plt.ylabel('Number of losses')
plt.title('Teams elected to bat and lost')
#10
plt.subplot(4,3,10)
plt.plot(teams, innings_1, label='Innings 1', marker='o')
plt.plot(teams, innings_2, label='Innings 2', marker='o')
plt.xlabel('Teams')
plt.ylabel('Number of times')
plt.legend()
plt.title('Teams scoring 300+ in innings 1 and 2')
#11
plt.subplot(4,3,11)
colors = sns.color_palette('husl', len(df3))
plt.bar(df3.index, df3, 
        color = colors,
        width = 0.4, 
        edgecolor = 'black',
        linewidth = 2,
        linestyle = '-')
plt.yticks(np.arange(1,9,1))
plt.xlabel('Teams')
plt.ylabel('Number of times')
plt.title('Teams with most 100+ partnerships')
#12
plt.subplot(4,3,12)
plt.stem(df4.index,df4)
plt.xticks(rotation=45)
plt.xlabel('Venue')
plt.ylabel('Number of times')
plt.title('Grounds with most 100+ partnerships')
plt.savefig("Matches_Analysis.pdf")


# In[25]:


df = pd.read_csv(r'C:\Users\Arnav\Downloads\scores.csv')
df.head()


# In[26]:


m1t300 = df[
    (df['Innings.1'] == 1).values &
    (df['Score']>=300)
]
daf = m1t300['Team'].value_counts()
daf


# In[27]:


m2t300 = df[
    (df['Innings.1'] == 2).values &
    (df['Score']>=300)
]
dbf = m2t300['Team'].value_counts()
dbf


# In[28]:


teams = ['RSA', 'IND', 'AUS', 'ENG', 'NZ', 'SL', 'BAN', 'PAK']
innings_1 = [5, 4, 3, 3, 2, 1, 1, 0] 
innings_2 = [0, 0, 1, 0, 2, 1, 0, 2]
plt.plot(teams, innings_1, label='Innings 1', marker='o')
plt.plot(teams, innings_2, label='Innings 2', marker='o')
plt.xlabel('Teams')
plt.ylabel('Number of Innings')
plt.title('Innings Comparison by Team')
plt.legend()
plt.show()


# In[29]:


df = pd.read_csv(r'C:\Users\Arnav\Downloads\partnerships.csv')
df.head()


# In[30]:


pmt_150 = df[
    (df['Runs']>=100).values
]
df3 = pmt_150['Team'].value_counts()
df3


# In[31]:


vmt_150 = df[
    (df['Runs']>=100).values
]
df4 = vmt_150['Ground'].value_counts()
df4


# In[ ]:






# In[ ]:




