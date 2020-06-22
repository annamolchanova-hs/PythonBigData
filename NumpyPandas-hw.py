#!/usr/bin/env python
# coding: utf-8

# In[1]:


import collections
import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


olimpic = pd.read_csv('./olimpic_medals.csv', names=['City','Edition','Sport','Discipline','Athlete','NOC','Gender','Event','Event_gender','Medal'])


# In[3]:


olimpic_by_year = olimpic.set_index('Edition')


# In[4]:


olimpic_by_year


# In[11]:


#1 Сколько медалей выиграл Jesse Owens в 1936?
len(olimpic_by_year[olimpic_by_year.Athlete.str.contains('OWENS, Jesse')].loc['1936'])
len(olimpic[(olimpic.Edition == '1936') & (olimpic.Athlete.str.contains('OWENS, Jesse'))])


# In[15]:


#2 Какая страна выйграла большинство золотых медалей мужчинами в бадминтоне?
olimpic[(olimpic.Discipline == 'Badminton') & 
        (olimpic.Gender == 'Men') & 
        (olimpic.Medal == 'Gold')].NOC.value_counts()[0:1] #TODO


# In[16]:


#3  Какие три страны выйграли большинство медалей в последние годы (с 1984 по 2008)?
olimpic_by_year.loc['1984':'2008'].NOC.value_counts()[0:3]


# In[17]:


#4. Покажите мужчин золотых медалистов по 100m. Выведите результаты по убыванию года выйгрыша.
#Покажите город в котором проходила олимпиала, год, имя атлета и страну за которую он выступал.
olimpic[(olimpic.Event == '100m') & 
        (olimpic.Event_gender == 'M') & 
        (olimpic.Medal == 'Gold')].sort_values(by='Edition', ascending=False).loc[:,['City', 'Edition', 'Athlete', 'NOC']]


# In[18]:


#5. Как много медалей было выйграно мужчинами и женщинами в истории олимпиады. Как много
#золотых, серебрянных и бронзовых медалей было выйграно каждым полом?
olimpic.groupby('Gender')['Medal'].value_counts()


# In[19]:


#6. Используя groupby(), постройте график числа всех медалей выйгранных на каждой олимпиаде.
olimpic.groupby('Edition').Medal.count().plot()
pp.ylabel('Medals')


# 7. Создайте список показывающий число всех медалей выйгранных каждой страной в течение всей
# истории олимпийских игр. Для каждой страны, необходимо показать год первой и последней
# заработанной медали.
# 

# In[25]:


olimpic.groupby('NOC').agg({'Edition': ['min', 'max'], 'Medal': 'count'
})


# 8. Атлеты выигравшие медали в Beijing на дистанции 100m или 200m

# In[28]:


olimpic[((olimpic.Event == '100m') | (olimpic.Event == '200m')) & 
        (olimpic.City == 'Beijing')]


# In[29]:


#9. Постройте график числа золотых медалей выйгранных США мужчинами и женщинами в атлетике.
olimpic[(olimpic.Sport == 'Athletics') & 
        (olimpic.NOC == 'USA') &
        (olimpic.Medal == 'Gold')].Gender.value_counts().plot.pie(figsize=(5, 5)) 


# In[31]:


#10. Постройте график 5 атлетов которые выйграли большинство золотых медалей.
olimpic[(olimpic.Medal == 'Gold')].Athlete.value_counts()[0:5].plot.bar()


# In[293]:


#11. Покажите суммарное количество медалей выйгранных странами в последних олимпийских играх.
olimpic[(olimpic.Edition == olimpic.Edition.max())].Medal.count()
olimpic[(olimpic.Edition == olimpic.Edition.max())].NOC.value_counts()


# In[100]:


#12. Постройте таблицу в которой по годам всех олимпиад покажите топовых атлетов США(1 атлет на год)
#по общему количеству медалей. Включите дисциплину атлета.
df = olimpic[(olimpic.NOC == 'USA')].groupby(['Edition','Athlete','Sport']).agg({'Medal': 'count'})
df.loc[df.groupby(['Edition'])['Medal'].idxmax()]

