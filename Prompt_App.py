#!/usr/bin/env python
# coding: utf-8

# # Taking Prompt from user

# In[1]:


import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = "sk-****...."

# Set the API key
openai.api_key = api_key

prompt = input("Write your prompt: \n")
print()

def chatgpt_gen():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role":"user", "content": prompt}]
    )
    print(response.choices[0]['message']['content'])

if __name__== '__main__':
    chatgpt_gen()


# In[ ]:




