#!/usr/bin/env python
# coding: utf-8

# In[1]:


def test1():
    a =5+6
    return a


# In[2]:


test1()


# In[3]:


def test2(a,b):
    return a+b


# In[4]:


test2(1,2)


# In[5]:


test2('Bharat', ' Dogra')


# In[6]:


test2(b="444",a='4545')


# In[7]:


def test3(*args):
    return args


# In[8]:


test3(1,2,3,4,"bmd")


# In[9]:


type(test3(1,2,3,4,"bmd"))


# In[10]:


test3([1,2,3,4,5], 'sudh','ineuron', 5+7j, (4,5,6))


# In[11]:


def test4(*args):
    return list(args)


# In[12]:


test4('sudh', True, 8+7j, 34,34.56)


# In[13]:


def test5(*args):
    l=[]
    for i in args:
        l.append(i)
    return l


# In[14]:


test5(34,35,36,37)


# In[17]:


def test6(*sudh):
    return list(sudh)


# In[18]:


test6(1,2,3,4,5)


# In[19]:


###Dictionary


# In[20]:


l=[1,2,3,4,5,6]
t=(4,5,6,8+7j)
s={3,4,5,6,7,8,9,3,4}


# In[21]:


l


# In[22]:


t


# In[23]:


s


# In[24]:


d = {}


# In[25]:


type(d)


# In[26]:


d1={1,2,3,4}


# In[27]:


type(d1)


# In[28]:


d2={'key1':'sudh', 'key2': [2,3,4,5]}


# In[30]:


d2.keys()


# In[31]:


d2.values()


# In[32]:


l


# In[34]:


d2


# In[36]:


d3={234224:'sudh'}


# In[37]:


d3


# In[38]:


d5 = {[1,2,3,4]:"sudh"}


# In[40]:


d6 = {(1,2,3,4):"sudh"}


# In[43]:


d7 = {'name ':'sudhanshu','org':'ineuron', 'mailid': 'sudhansu@ineuron.ai', 'name':'sudh'}


# In[44]:


d7


# In[45]:


d7 = {'name':'sudhanshu','org':'ineuron', 'mailid': 'sudhansu@ineuron.ai', 'name':'sudh'}


# In[46]:


d7


# In[47]:


d7 = {'name':'sudhanshu','org':'ineuron', 'mailid': 'sudhansu@ineuron.ai', 'name':'sudh','name1':'sudh'}


# In[48]:


d7


# In[49]:


d8={"name":"sudh", "mentor":{"fsds":"imram", 'fsda':'anand', 'bigdata':'Shashank'}}


# In[50]:


d8


# In[51]:


d7


# In[53]:


d7['mailid']


# In[54]:


### we have to keep key names not the index to extract the values


# In[55]:


d8


# In[57]:


d8['mentor']['bigdata']


# In[58]:


d7.keys()


# In[59]:


d7.values()


# In[60]:


list(d7 = {'name':'sudhanshu','org':'ineuron', 'mailid': 'sudhansu@ineuron.ai', 'name':'sudh'})


# In[61]:


list(d8['mentor'].values())


# In[64]:


l=[]
for i in d8.keys():
    if type(d8[i])== dict:
        l.append(list(d8[i].values()))
        


# In[65]:


l


# In[66]:


d9 = {'name': 'sudh',
 'mentor': {'fsds': 'imram', 'fsda': 'anand', 'bigdata': 'Shashank'}, 'mailid':{'imran':'imran@ineuron.ai', 'anand':'anand@ineuron.ai', 'shashank':'shashank@ineuron.ai'}}


# In[67]:


l=[]
for i in d9.keys():
    if type(d9[i])== dict:
        l.append(list(d9[i].values()))


# In[68]:


l


# In[69]:


def test9(d):
    l=[]
 
    for i in d.keys():
        if type(d[i])== dict:
            l.append(list(d[i].values()))
    return l


# In[70]:


test9(d8)


# In[71]:


d8['mobile_num']=(2424,345345,3455445)


# In[72]:


d8


# In[73]:


test9(d9)


# In[74]:


d8['name']='sudhanshukumar'


# In[75]:


d8


# In[76]:


d7


# In[77]:


del d7


# In[78]:


d7


# In[79]:


d8


# In[80]:


del d8['name']


# In[81]:


d8


# In[82]:


d8.pop('mentor')


# In[83]:


d8


# In[84]:


d8['name']='sudhanshu'


# In[85]:


d8


# In[88]:


def test10(**kwargs):   #### this can take n number of keys and value
    return kwargs


# In[90]:


test10(a = 4,b = 5,c = 6,d = 7)


# In[91]:


### * will give tuples and ** will give you dict


# In[92]:


test10(a = 4,b = 5,c = 6,d = [7,4,5,9])


# In[93]:


def test11(**sudh):
    return sudh


# In[94]:


test11(b=2,m=456)


# In[98]:


def test12(a):
    return a

def test13(b):
    return b

def test14(func):
    return func('sudh')


# In[101]:


test14(test12)


# In[102]:


test14(test13)


# In[103]:


def test12(a):
    return a

def test13(b):
    return 'sudh'

def test14(func):
    return func('sudh')


# In[104]:


test14(test12)


# In[107]:


test14(test13)


# In[108]:


def test12(a):
    return a

def test13(*args):
    return 'sudh'

def test14(func):
    return func('sudh')


# In[109]:


test14(test13)


# In[114]:


def test15(a):
    print("this is my test 15")
    
    def test16():
        print("This is my test 16")
        
    def test17():
        print("This is my test 17")
        
    if a=='sudh':
        return test16()
    elif a=='kumar':
        return test17()


# In[113]:


test15()


# In[115]:


test15('sudh')


# In[116]:


test15('kumar')


# In[ ]:




