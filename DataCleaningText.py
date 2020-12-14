
# coding: utf-8

# ### Cleaning Text Data Through a function

# In[9]:


print("Have text to clean? Go ahead and follow the two steps.\n")
text = input("1) Please enter a string:\n")
removedChars = input("2)Please enter the characters you'd like to be removed:\n")
def DataClean(text):
    for char in removedChars:
        text = text.replace(char,"")
        return text

DataClean(text)

