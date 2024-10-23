#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


os.environ["OPENAI_API_KEY"] = ""


# In[3]:


get_ipython().system('pip install langchain')


# In[7]:


get_ipython().system('pip install blosc2==2.0.0 cython>=0.29.21')


# In[8]:


get_ipython().system('pip install black>=22.3.0')


# In[4]:


get_ipython().system('pip install blosc2==2.0.0')
get_ipython().system('pip install cython>=0.29.21')
get_ipython().system('pip install black>=22.3.0')


# In[9]:


get_ipython().system('pip install langchain')


# In[5]:


get_ipython().system('pip install openai')


# In[6]:


get_ipython().system('pip install langchain_community')


# In[7]:


get_ipython().system('pip install -U langchain-openai')


# In[4]:


from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain


# In[5]:


llm_resto = OpenAI(temperature=0.6)


# In[6]:


prompt_template_resto = PromptTemplate(
    input_variables=['weight', 'height', 'gender', 'age', 'allergies','total_calories', 'diet_type'],
    template="Diet Recommendation System:\n"
             " Recommend random 1 healthy breakfast, 1 healthy lunch,1 healthy dinner that collectively total up to {total_calories} calories,"
             "based on the following criteria:\n"
             "Weight: {weight} \n"
             "Height: {height} \n"
             "Gender: {gender} \n"
             "Age: {age} \n"
             "Allergies: {allergies} \n"
             "Total Calories for the Day: {total_calories}\n"
             "Diet Type: {diet_type}\n"
)


chain_resto = LLMChain(llm=llm_resto, prompt=prompt_template_resto)


# In[7]:


chain_resto = LLMChain(llm=llm_resto, prompt=prompt_template_resto)

user_data = {
    'weight': 70,  # in kg
    'height': 175,  # in cm
    'gender': 'male',
    'age': 30,
    'allergies': 'none',
    'total_calories': 2500,  # calories per day
    'diet_type': 'non-vegan'
}

results = chain_resto.run(user_data)


# In[8]:


results


# In[13]:


import re


# In[29]:


breakfast_names = re.findall(r'Breakfast:(.*?)Lunch:', results, re.DOTALL)


# In[30]:


breakfast_names


# In[31]:


lunch_names = re.findall(r'Lunch:(.*?)Dinner:', results, re.DOTALL)


# In[32]:


lunch_names


# In[42]:


dinner_names = re.findall(r'Dinner:(.*?)Total for the day:', results, re.DOTALL)


# In[43]:


dinner_names


# In[44]:


total_cals = re.findall(r'Total for the day:(.*?)$', results, re.DOTALL)


# In[45]:


total_cals


# In[46]:


breakfast_names = [name.strip() for name in breakfast_names[0].strip().split('\n') if name.strip()] if breakfast_names else []


# In[47]:


breakfast_names


# In[48]:


lunch_names = [name.strip() for name in lunch_names[0].strip().split('\n') if name.strip()] if lunch_names else []


# In[49]:


lunch_names


# In[50]:


dinner_names = [name.strip() for name in dinner_names[0].strip().split('\n') if name.strip()] if dinner_names else []


# In[51]:


dinner_names


# In[52]:


total_cals = [name.strip() for name in total_cals[0].strip().split('\n') if name.strip()] if total_cals else []


# In[53]:


total_cals


# In[54]:


# Printing the recommendations separately
print("Recommended Breakfast:", breakfast_names)
print("Recommended Lunch:", lunch_names)
print("Recommended Dinner:", dinner_names)
print("Total Calories for the day", total_cals)


# In[ ]:




