#!/usr/bin/env python
# coding: utf-8

# # Foundations of Data Science Project - Diabetes Analysis
# 
# ---------------
# ## Context
# ---------------
# 
# Diabetes is one of the most frequent diseases worldwide and the number of diabetic patients are growing over the years. The main cause of diabetes remains unknown, yet scientists believe that both genetic factors and environmental lifestyle play a major role in diabetes.
# 
# A few years ago research was done on a tribe in America which is called the Pima tribe (also known as the Pima Indians). In this tribe, it was found that the ladies are prone to diabetes very early. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients were females at least 21 years old of Pima Indian heritage. 
# 
# -----------------
# ## Objective
# -----------------
# 
# Here, we are analyzing different aspects of Diabetes in the Pima Indians tribe by doing Exploratory Data Analysis.
# 
# -------------------------
# ## Data Dictionary
# -------------------------
# 
# The dataset has the following information:
# 
# * Pregnancies: Number of times pregnant
# * Glucose: Plasma glucose concentration over 2 hours in an oral glucose tolerance test
# * BloodPressure: Diastolic blood pressure (mm Hg)
# * SkinThickness: Triceps skin fold thickness (mm)
# * Insulin: 2-Hour serum insulin (mu U/ml)
# * BMI: Body mass index (weight in kg/(height in m)^2)
# * DiabetesPedigreeFunction: A function that scores the likelihood of diabetes based on family history.
# * Age: Age in years
# * Outcome: Class variable (0: a person is not diabetic or 1: a person is diabetic)

# ## Q 1: Import the necessary libraries and briefly explain the use of each library (3 Marks)

# In[1]:


import numpy as np

import pandas as pd

import seaborn as sns

import plotly as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# #### Write your Answer here: 
NUMPY- Numpy is a math library which uses arrays, vectors, and metrics instead of lists. Arrays are considered better because they take up less memory allowing the computations to be faster. 

PANDAS- Pandas is used in conjunction with numpy. Pandas is best used for bilateral and multilateral dataframes and can produce different visualizations of the data.

SEABORN- Seaborn is a visualization library which is used to format data in useful ways to see distribution and trends.

PLOTLY- Plotly is a resource of graphing options which you can impose on your data. 

MATPLOTLIB INLINE- Shows the graphic you request in line with the code, not on a seperate screen.

# ## Q 2: Read the given dataset (2 Marks)

# In[2]:


pima = pd.read_csv("diabetes.csv")


# ## Q3. Show the last 10 records of the dataset. How many columns are there? (2 Marks)

# In[3]:


pima.tail(10)


# #### Write your Answer here: 
# 
Ans 3: There are nine (9) collumns in this data set.
# ## Q4. Show the first 10 records of the dataset (2 Marks)

# In[4]:


pima.head(10)


# ## Q5. What do you understand by the dimension of the dataset? Find the dimension of the `pima` dataframe. (3 Marks)

# In[5]:


pima.shape


# #### Write your Answer here: 
# 
Ans 5: There are 768 rows (data points) and 9 collumns (features).
# ## Q6. What do you understand by the size of the dataset? Find the size of the `pima` dataframe. (3 Marks)

# In[6]:


pima.size


# #### Write your Answer here: 
# 
Ans 6: There are 6912 elements, this is the product of the rows and collumns.
# ## Q7. What are the data types of all the variables in the data set? (2 Marks)
# **Hint: Use the info() function to get all the information about the dataset.**

# In[7]:


pima.info()


# #### Write your Answer here: 
# 
Ans 7: This dataframe uses both INTEGER and FLOAT data types.
# ## Q8. What do we mean by missing values? Are there any missing values in the `pima` dataframe? (4 Marks)

# In[8]:


pima.isnull().values.any()


# #### Write your Answer here: 
# 
Ans 8: Missing Values refers to there not being any data for an element. There are no missing values in this dataframe.
# ## Q9. What do the summary statistics of the data represent? Find the summary statistics for all variables except 'Outcome' in the `pima` data. Take one column/variable from the output table and explain all its statistical measures. (5 Marks)

# In[9]:


pima.iloc[: , 0 : 8].describe()


# #### Write your Answer here: 
# 
Ans 9: We will look at the statistics for the pregnancy variable:

COUNT: Total number of pregnancies for all respondents.

MEAN: Average amount of pregnancies for each woman.

STD: Standard deviation is the measure of variance in the amount of pregnancies (i.e. square root of variance).

MIN: This is the least amount of pregnancies reported.

25%: Tells us the bottom 25% of our data have either one or no pregnancies.

50%: Tells us the bottom half of our data had three or fewer pregnancies.

75%: Tells us that the bottom 75% of the women had 6 or fewer pregnancies.

MAX: The largest number of pregnancies is 17, which deserves a medal.
# ## Q 10. Plot the distribution plot for the variable 'BloodPressure'. Write detailed observations from the plot. (2 Marks)

# In[10]:


sns.displot(pima['BloodPressure'], kind = 'kde')

#Removed plt.show because it kept coming back with errors.


# #### Write your Answer here: 
# 
Ans 10: This graphic shows a Gauissian distribution, the mean/median/mode looks to be about 75BP. A majority,~95%, of respondents fall between 40BP and 100BP with ~68% falling between about 60BP and 85BP.  
# ## Q 11. What is the 'BMI' of the person having the highest 'Glucose'? (2 Marks)

# In[11]:


pima[pima['Glucose'] == pima['Glucose'].max()]['BMI']


# #### Write your Answer here: 
# 
Ans 11: The highest glucose (661) has a BMI of 42.9.
# ## Q12.
# ### 12.1 What is the mean of the variable 'BMI'? 
# ### 12.2 What is the median of the variable 'BMI'? 
# ### 12.3 What is the mode of the variable 'BMI'?
# ### 12.4 Are the three measures of central tendency equal?
# 
# ### (4 Marks)

# In[12]:


m1 = pima['BMI'].mean()  # mean
print(m1)

m2 = pima['BMI'].median()  # median
print(m2)

m3 = pima['BMI'].mode()[0]  # mode
print(m3)


# #### Write your Answer here: 
# 
Ans 12: The three measurements are basically equal, with the mean varying slightly higher:
MEAN, the average: 32.45080515543617
MEDIAN, the number in the middle of the data set: 32.0
MODE, the number which was most common: 32.0
# ## Q13. How many women's 'Glucose' levels are above the mean level of 'Glucose'? (2 Marks)

# In[13]:


pima[pima['Glucose'] > pima['Glucose'].mean()].shape[0]


# #### Write your Answer here: 
# 
Ans 13: There are 343 women whose glucose levels are above the mean.
# ## Q14. How many women have their 'BloodPressure' equal to the median of 'BloodPressure' and their 'BMI' less than the median of 'BMI'? (2 Marks)

# In[14]:


print(pima[(pima['BloodPressure'] == pima['BloodPressure'].median()) & (pima['BMI'] < pima['BMI'].median())])

len(pima[(pima['BloodPressure'] == pima['BloodPressure'].median()) & (pima['BMI'] < pima['BMI'].median())])


# #### Write your Answer here: 
# 
Ans 14: 22 women have the median blood pressure and their BMI less than the median.
# ## Q15. Create a pairplot for the variables 'Glucose', 'SkinThickness', and 'DiabetesPedigreeFunction'. Write your observations from the plot. (3 Marks)

# In[15]:


#Added regression line to make the relationships more apparent

sns.pairplot(data = pima, vars = ['Glucose', 'SkinThickness', 'DiabetesPedigreeFunction'], hue = 'Outcome', kind = 'reg')
# Removed plt.show() because it kept showing an error.


# #### Write your Answer here: 
# 
Ans 15: Across the graphs there seems to be little to no correlation between the pairings of "Glucose", "SkinThickness" and "DiabetesPedigreeFunction". The most prominent exception is the 'SkinThickness' to 'DiabetesPedigreeFunction' which shows a slightly positive correlation between increased 'SkinThickness' and 'DiabetesPedigreeFunction'.
# ## Q16. Plot the scatterplot between 'Glucose' and 'Insulin'. Write your observations from the plot. (4 Marks)

# In[16]:


#I know the function is more likely the scatterplot function, but I like the regression line to be a part of the graph.

sns.lmplot(x = 'Glucose', y = 'Insulin', data = pima, line_kws = {'color': 'red'})
#Removed plt.show() because an error kept showing up.


# #### Write your Answer here: 
# 
Ans 16: The plot shows a slight positive correlation between 'Glucose' and 'Insulin'. There is a good bit of data which shows Insluin as about 100, this would point to it being the mean of the glucose data.
# ## Q 17. Plot the boxplot for the 'Age' variable. Are there outliers? (2 Marks)

# In[17]:


import plotly.express as px
fig = px.box(pima, y = 'Age')
fig.show()


# #### Write your Answer here: 
# 
Ans 17: There are six women whose ages are above the upper fence of data.
# ## Q18. Plot histograms for the 'Age' variable to understand the number of women in different age groups given whether they have diabetes or not. Explain both histograms and compare them. (5 Marks)

# In[18]:


import matplotlib.pyplot as plt
plt.hist(pima[pima['Outcome'] == 1]['Age'], bins = 5)
plt.title('Distribution of Age for Women who has Diabetes')
plt.xlabel('Age')
plt.ylabel('Frequency')
#plt.show()


# In[19]:


import matplotlib.pyplot as plt
plt.hist(pima[pima['Outcome'] == 0]['Age'], bins = 5)
plt.title('Distribution of Age for Women who do not have Diabetes')
plt.xlabel('Age')
plt.ylabel('Frequency')
#plt.show()


# #### Write your Answer here: 
# 
Ans 18: The histograms are showing the relatinship between the age of women and how many do or do not have diabetes. The incidence of women who do not have diabetes are orders of magnitude more than those who are sick in all categories. The ages from 21-31 have the highest numbers, but is the after 31 which the percentage of women with diabetes is much higher. 
# ## Q 19. What is the Interquartile Range of all the variables? Why is this used? Which plot visualizes the same? (5 Marks)

# In[20]:


Q1 = pima.quantile(0.25)
Q3 = pima.quantile(0.75)
IQR = Q3 - Q1
print(IQR)


# #### Write your Answer here: 
# 
Ans 19: The Interquartile Range (IQR) tells you about the middle of your data, it is the length of the middle 50%. So, there are five numbers in the middle 50% of data for pregnancies. The IQR is great for controlling for outliers as it is not as affected like the mean can be. The boxplot is a good graphing option for showing the IQR.
# ## Q 20. Find and visualize the correlation matrix. Write your observations from the plot. (3 Marks)

# In[21]:


corr_matrix = pima.iloc[ : ,0 : 8]
sns.heatmap(corr_matrix.corr(), annot = True)


# #### Write your Answer here: 
# 
Ans 20: The highest correlation is between age and number of pregnancies, the lowest is between DPF and blood pressure. None of the correlations are especially high but the ones that are higher make sense. Obviously the older you are the more pregnancies you are likely to have and the higher the BMI the thicker the skin due to fat and stress. The insulin and glucose correlation seems like it should be higher.