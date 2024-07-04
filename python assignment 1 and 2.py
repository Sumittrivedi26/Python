#!/usr/bin/env python
# coding: utf-8

# #### In the below elements which of them are values or an expression?
# eg:- values can be integer or string and expressions will be mathematical operators.

# In[ ]:


*  - mathematical operator
'hello' -- values
-87.8  -- values
-    -- mathematical operator
(--, mathematical, operator)
+	-- mathematical operstor
6   -- value


# #### What is the difference between string and variable?

# In[ ]:


A variable is a a type of empty box which we can use to store a data
where as string is the data is to be stored in the variable.


# #### Describe three different data types.

# In[ ]:


the three different types of data types are:-
    1. String
    2. Int
    3. float
    4. boolean


# #### What is an expression made up of? What do all expressions do?

# In[ ]:


the expressions in python are a combination of operators and operands
and all these expressions give a value after being interpreted by python interpretor


# #### This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# 

# In[ ]:


An expression is a piece of code that evaluates to a values after being interpreted by python whereas
a statement is an action
for eg assignment of spam = 10 that means span is asssigned to value 10 without any calculation


# #### After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1
# 

# In[ ]:


it will contain 22 only


# In[17]:


b = 22
b+1 
b


# #### What should the values of the following two terms be?
# 'spam' + 'spamspam'
# \
# 'spam' * 3
# 

# In[19]:


"spam" + "spamspam"


# In[21]:


"spam" * 3


# #### What three functions can be used to get the integer, floating-point number, or string version of a value?

# In[ ]:


int(), float(), str(), these are the functions used to get the integer
floating point number and string of any value passed


# #### hy does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'
# 

# In[ ]:


99 is a integer and the rest are string so we cannot concanate a string and 
integer together to do so first we need to convert 99 into str and then do the same process


# In[ ]:





# # Assignment 2

# In[ ]:





# #### What are the two values of the Boolean data type? How do you write them?

# In[ ]:


The two values of a boolean datatype are true and false


# In[ ]:





# #### What are the three different types of Boolean operators?

# In[ ]:


boolean operastors are the word "AND" "OR" "NOT".


# #### Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

# In[ ]:


AND                               OR                               NOT
TRUE TRUE   TRUE                  TRUE TRUE    TRUE                TRUE FALSE
TRUE FALSE  FALSE                 TURE FALSE   TRUE                FALSE TRUE
FALSE TRUE  FALSE                 FALSE TRUE.  TRUE
FALSE FALSE FALSE                 FALSE FALSE.  FALSE


# #### What are the values of the following expressions?

# In[22]:


(5 > 4) and (3 == 5) 


# In[23]:


not (5 > 4)


# In[24]:


(5 > 4) or (3 == 5)


# In[25]:


not ((5 > 4) or (3 == 5))


# In[26]:


(not False) or (not True)


# In[27]:


(True and True) and (True == False)


# #### What are the six comparison operators?

# In[ ]:


==, !=, < , > , <=, >=


# #### How do you tell the difference between the equal to and 
# #### assignment operators?Describe a condition and when you would use one.

# In[ ]:


WHEN WE USE DOULE EQUALS SIGN IT MEANS equal to operator 
whereas when we s=us esingle equal to sign it means assignment operator
to assign a value of x we use x = 5 and to compaire whether x == 5 we use double equal to.


# #### Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam

# In[39]:


spam = 3
if spam == 1:
    print ("hello")
elif spam == 2:
    print ("howdy")
else:
    print ("Greetings") 


# #### If your programme is stuck in an endless loop, what keys you’ll press?

# In[ ]:


ctrl + c


# #### How can you tell the difference between break and continue?

# In[ ]:


Break	Continue
In the break statement, the control exits from the loop.	In the continue statement, the control remains within the loop.
It is used to stop the execution of the loop at a specific condition.	It is used to skip a particular iteration of the loop.


# #### In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)
# 

# In[ ]:


RANGE(10)= it gived a range of number from 0 to 10 without including 10 
as lower limit is not specifies hence its 10


# In[ ]:


range(0,10) = it gives a range of number fron 0 to 10  without including 10 
but here the lower limit is specified as 10


# In[ ]:


range(0,10,1) = it gives a range of number fron 0 to 10  without including 10 with 1 as step size
but here the lower limit is specified as 10


# #### Write a short program that prints the numbers 1 to 10 using a for loop. 
# #### Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[50]:


i = 12
for i in range(1,11):
    print(i)


# In[64]:


i = 0
while (i  < 10):
    i = i + 1
    print(i)
    


# In[ ]:




