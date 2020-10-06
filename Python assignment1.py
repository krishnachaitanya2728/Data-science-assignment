#!/usr/bin/env python
# coding: utf-8

# In[3]:


string = " I am very keen in building up my career in Data Science, but not sure from where to start. If I search the web it throws me thousands of articles, few are relevant others make me confused, again I come around to the same page. Supervised has provided me a good platform to remove all such qualms which were wrangling in my mind"


# In[ ]:


2. Lower the text in the string.


# In[4]:


string_lower = string.lower()


# In[5]:


print (string_lower)


# In[ ]:


3. Try to get the clean text removing the punctuation from the string.


# In[6]:


string_punc = string 


# In[8]:


# initializing punctuations string  
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''


# In[9]:


for ele in string_punc:  
    if ele in punc:  
        string_punc = string_punc.replace(ele, "") 


# In[10]:


print(string_punc)


# In[ ]:


Extract word "Data Science" from the string.


# In[12]:


import re


# In[16]:


res = re.findall(r"Data Science", string) 


# In[17]:


print(res)


# In[ ]:


4. Find the frequency of words used in the string.


# In[19]:


# Python code to find frequency of each word 
def freq(str): 
  
    # break the string into list of words  
    str = str.split()          
    str2 = [] 
  
    # loop till string values present in list str 
    for i in str:              
  
        # checking for the duplicacy 
        if i not in str2: 
  
            # insert value in str2 
            str2.append(i)  
              
    for i in range(0, len(str2)): 
  
        # count the frequency of each word(present  
        # in str2) in str and print 
        print('Frequency of', str2[i], 'is :', str.count(str2[i]) > 1)     
  
def main(): 
    freq(string)                     
  
if __name__=="__main__": 
    main()             # call main function


# In[ ]:


7.Can you change the word "Supervised" to "Unsupervised" in the string


# In[21]:


string_new = string.replace("Supervised", "Unsupervised")


# In[22]:


string_new


# In[ ]:


8.Splitting of the string with a dot operator(.)


# In[23]:


parts = string.split(" ")
print(parts)


# In[ ]:


1.Consider the above text as a string, figure out the average length of the string.


# In[27]:


average = sum(len(part) for part in parts) / len(parts)
average


# In[ ]:


9.Find the words from the string which ends with "e"


# In[30]:


string_e = [w for w in string.split() if w.endswith('e')]


# In[31]:


string_e


# In[ ]:


10.Figure out number of a's used in the string.


# In[32]:


string.count('a')


# In[ ]:


11.In the weekend , I purchased 250g of apple, 500g of sugar, 2.5 kg of rice, 2.5 litres of milk and finally 1 dozen of egg.
a) Can you help me frame the above purchase in the form of dictionary with commodities as keys to it.


# In[49]:


groceries_dict = {'apple' : 0.25, 'sugar' : 0.5,'rice' : 2.5,'milk' : 2.5, 'egg' : 1}


# In[ ]:


b)I forgot to mention another item, 1kg of atta packet. Can you also add it ?


# In[50]:


groceries_dict.update( {'atta' : 1} )


# In[51]:


groceries_dict


# In[ ]:


c)Instead of 2kg of rice, I bought only 1kg of rice. Can you change the corresponding value ?


# In[52]:


groceries_dict['rice'] = 1


# In[53]:


groceries_dict


# In[ ]:


d) Can you list out all these items using a loop.


# In[54]:


for key in groceries_dict:
    print (key)


# In[ ]:


Create another dictionary for pricing.

Thereby, prepare a bill for me of the overall cost of the total commodities purchased by using two dictionaries !


# In[57]:


pricing = {'apple' : 220, 'sugar' : 43,'rice' : 45,'milk' : 30, 'egg' : 60, 'atta' : 60}


# In[58]:


sum(pricing[k]*groceries_dict[k] for k in pricing)


# In[64]:


AI_companies = ['Amazon','Facebook','HiSilicon','Google','Apple','Microsoft','SenseTime']


# In[66]:


AI_companies.sort()


# In[67]:


print(AI_companies)


# In[68]:


AI_companies.extend(['Nvidia','OpenAI','Qualcomm','Reliance'])


# In[69]:


AI_companies


# In[ ]:


Elimiate 'Reliance' from the list


# In[71]:


AI_companies.pop(10)


# In[72]:


AI_companies


# In[74]:


AI_companies = [e for e in AI_companies if e not in ('Facebook', 'Google', 'Microsoft')]


# In[75]:


AI_companies


# In[ ]:


Questions on Tuple
(a)Consider the above standard price problem statement and place the prices in the form of the tuple.

(b)Find out the min and max price among them.

(c)Also, convert the above "AI_companies" list to a tuple.

(d)Combine two above tuples to a single tuple.

(e)Compare the length of two tuples.


# In[76]:


price =  (220, 43, 45, 30, 60, 60)


# In[77]:


min(price)


# In[78]:


max(price)


# In[79]:


AI_comp = ('Amazon',
 'Apple',
 'Facebook',
 'Google',
 'HiSilicon',
 'Microsoft',
 'SenseTime',
 'Nvidia',
 'OpenAI',
 'Qualcomm',
 'Reliance')


# In[ ]:




