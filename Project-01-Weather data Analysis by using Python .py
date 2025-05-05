#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd 


# In[16]:


# import dataset from laptop  

data=pd.read_csv(r"/Users/babulsarker/Desktop/Python /Project-1 -Weather Data Analysis /file.csv")



# Cmd + Option + C to copy the full path(in mac)
#Using r"" (a raw string) is a common way to avoid Unicode errors or unexpected escape character issues in file paths, 
#especially when the path contains backslashes (\) that could be misinterpreted.


# In[18]:


data


# In[ ]:


# How to analysis DataFrams


# # .head()
# 
# > This one of the most useful methods in pandas for getting a quick look at your data.
# > It shows the first 5 rows of a DataFrame by default.
# 
# 

# In[14]:


data.head()


# # .shape
# 
# It shows total number of rows and column of a dataframe(DF) 
# 

# In[13]:


data.shape


# # .index
# 
# it provides the index of DF 
# 

# In[15]:


data.index


# # .column
# 
# it shows the name of column 
# 

# In[16]:


data.columns


# # .dtypes
# 
# it shows the datatype of each column 
# 

# In[17]:


data.dtypes 


# # .unique()
# 
# In a column it shows all unique value. It can be applid on single column only not the wholw dataframe
# 

# In[21]:


data['Weather'].unique()


# In[23]:


data['Temp_C'].unique()


# # .nunique()
# 
# -This shows the total number of unique values in each column.
# -It can be applied on a single column as well as across the whole DF 
# 

# In[24]:


data.nunique()  #total number of unique values across the whole DF


# In[26]:


data['Weather'].nunique()     # total number of unique values in each column.


# In[27]:


data['Temp_C'].nunique()     #total number of unique values in each column.


# # .count
# 
# -It returns the number of non-null (non-missing) values in a single column as well as across the whole  DataFrame.
# 

# In[28]:


data.count()              # returns the number of non-null (non-missing) values across the whole DataFrame.


# In[29]:


data['Weather'].count()      #returns the number of non-null (non-missing) values in a single column(i.e Weather)


# In[31]:


data['Visibility_km'].count()   #returns the number of non-null (non-missing) values in a single column(i.e Visibility_km)


# # .value_counts
# 
# >it shows all unique values with their count.
# >It can be applied to a single column
# 

# In[37]:


data['Weather'].value_counts()


# In[38]:


data['Temp_C'].value_counts()


# In[39]:


data['Wind Speed_km/h'].value_counts()


# # .info()
# 
# > it provides basic information about the DF
# 

# In[40]:


data.info()


# # Problem-1:  Find out all unique wind speed values in the data.

# In[15]:


data.head(3)


# In[11]:


data.nunique()


# In[13]:


data['Wind Speed_km/h'].nunique()


# In[14]:


data['Wind Speed_km/h'].unique()   #Solution of Problem -1 


# In[ ]:


#SELF LEARNING # 
#Array-In Python, an array is a data structure 
# that stores multiple values of the same type in a single variable


# # Problem-02: Find out the number of times when the weather is exactly clear and cloudy? 

# In[16]:


data.head(3)


# In[18]:


#1st way using value_counts() 

data['Weather'].value_counts() 


# In[19]:


#2nd way using filtering 
data.head(3)


# In[20]:


data['Weather']=='Clear'   #it will show blooen result # == sign uses for filtering data 


# In[21]:


data[data['Weather']=='Clear']


# In[22]:


data['Weather']=='Cloudy'


# In[23]:


data[data['Weather']=='Cloudy']      


# In[24]:


#3rd way using Groupby 
data.head(3)


# # .groupby()
# 
# >In Python, groupby is commonly used to group data based on a specific key or column.
# >It’s most often used with the pandas library for data analysis
# 

# In[27]:


data.groupby('Weather').get_group('Clear')


# In[ ]:


#solution-2:Total number of clear weather-1326


# In[32]:


data.groupby('Weather').get_group('Cloudy')

#.groupby('Weather') 
#This organizes the data into groups based on the Weather column.
#Each group contains all rows where 'Weather' has the same value (e.g., "Cloudy", "Sunny", etc.).

#.get_group('Cloudy')
#This extracts only the group where the 'Weather' value is 'Cloudy' 
#i.e., all rows where the Weather column equals "Cloudy".


# In[ ]:


#solution-2:Total number of cloudy weather-1728


# # Problem-3: Find out the number of times when the wind speed is exactly 7 km/h.

# In[33]:


data.head(3)


# In[48]:


data['Wind Speed_km/h']==7   # it will return result in Boolean format 


# In[49]:


data[data['Wind Speed_km/h']==7]    #using filtering mathod 


# In[ ]:


#soultion of problem: 3 - Total number of times = 677 


# # Problem-4: Find out all null values in  the data 

# In[52]:


#1st way 
data.isnull() 

#This checks each value in the DF to see if it's null (missing).
#It returns a DataFrame of True (if missing/have null values) or False (if not missing/no null values ).



# In[54]:


#1st way

data.isnull().sum() 

#.sum() - When used on a DataFrame of True/False, True counts as 1 and False as 0.
#So .sum() counts how many nulls are in each column.


# In[61]:


#2nd way 

data.notnull().sum()

# data.notnull()
# Returns a DataFrame of True for values that are not missing, and False for missing ones.

# .sum()
# Counts the number of True values (i.e., not null) in each column.



# # Problem: 5- Rename the column name Weather of DF to Weather Condition

# In[62]:


data.head(3)


# In[21]:


data.rename(columns= {'Weather' : 'Weather Condition'})

# But this column name renamed only for this comand not for permanetly on whole DF 



# In[65]:


data.head()


# In[22]:


#To apply the change column name permanently, you need to apply following command

data.rename(columns= {'Weather' : 'Weather Condition'}, inplace=True)

#useing the inplace=True for permanent change 


# In[70]:


data.head(5)


# # Problem-6: What is the mean of 'Visibility' and  'Wind Speed'

# In[71]:


data.head(3)


# In[72]:


data['Visibility_km'].mean()

#This gives the mean of a single column.


# In[73]:


data['Wind Speed_km/h'].mean()


# # Problem-7: What is the Standard Deviation of Pressure and Wind Speed in the Data 

# In[74]:


data.head(3)


# In[75]:


data['Press_kPa'].std()


# In[76]:


data['Wind Speed_km/h'].std()


# # Problem-8: What is the variance of 'Relative Humidity ' in the this data?

# In[78]:


data.head(2)


# In[79]:


data['Rel Hum_%'].var()


# # Problem-9: Find all instances when snow was recorded?

# In[83]:


#1st way using value_counts 

data.head(3)

data['Weather Condition'].value_counts()



# In[85]:


#2nd Way using filtering

data[data['Weather Condition']=='Snow']


# In[91]:


#3rd way str.contains

data[data['Weather Condition'].str.contains('Snow')].tail(50)


# # Problem-10: Find out all instances When 'Wind speed is above 24' and 'Visibility is 25'

# In[92]:


data.head(3)


# In[97]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)]


# # Problem-11 : What is the mean value of each column against each 'Weather Condition'

# In[103]:


data.head(2)


# In[113]:


data.groupby('Weather Condition').mean(numeric_only=True)

#data.groupby('Weather Condition')
#Groups your dataset based on different values in the 'Weather Condition' column (like 'Sunny', 'Cloudy', 'Snow', etc.)

#.mean(numeric_only=True)
#For each group (e.g., all rows with 'Sunny'), it calculates the average (mean) of all the numeric columns only 
#(e.g., Temperature, Humidity, Wind Speed).


# # Problem-12: What is the Min and Max value of each column against each 'Weather Condition'

# In[114]:


data.head(3)


# In[115]:


data.groupby('Weather Condition').min()


# In[116]:


data.groupby('Weather Condition').max()


# # Problem-13:Show all records where 'Weather Condition Is Fog'

# In[19]:


data.head(3)


# In[24]:


data[data['Weather Condition']=='Fog']


# In[23]:


data.head()


# # Problem-14: Find all instances when 'Weather is Clear' or 'Visibility is above 40'

# In[26]:


data.head(3)


# In[28]:


data[(data['Weather Condition']=='Clear') | (data['Visibility_km']>40)]   
 
 #  Verticle bar( '|') sign means 'OR'


# # Problem-15: Find all instances when :
# 
# A.'Weather is Clear' and 'Relative Humidity is greater than 50'
# 
# Or
# 
# B.'Visibility is above 40'
# 

# In[30]:


data.head(3)


# In[35]:


data[((data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)) | (data['Visibility_km'] > 40)]


# In[ ]:




