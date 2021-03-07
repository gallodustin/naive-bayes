#!/usr/bin/env python
# coding: utf-8

# In[44]:


import math


# In[13]:


def readfile(filename, arr):
    with open(filename) as f:
        while True:
            c = f.read(1)
            if not c:
                return arr
            if c == 'a':
                arr[0] += 1
            if c == 'b':
                arr[1] +=1
            if c == 'c':
                arr[2] += 1
            if c == 'd':
                arr[3] += 1
            if c == 'e':
                arr[4] += 1
            if c == 'f':
                arr[5] += 1
            if c == 'g':
                arr[6] += 1
            if c == 'h':
                arr[7] += 1
            if c == 'i':
                arr[8] += 1
            if c == 'j':
                arr[9] += 1
            if c == 'k':
                arr[10] += 1
            if c == 'l':
                arr[11] += 1
            if c == 'm':
                arr[12] += 1
            if c == 'n':
                arr[13] += 1
            if c == 'o':
                arr[14] += 1
            if c == 'p':
                arr[15] += 1
            if c == 'q':
                arr[16] += 1
            if c == 'r':
                arr[17] += 1
            if c == 's':
                arr[18] += 1
            if c == 't':
                arr[19] += 1
            if c == 'u':
                arr[20] += 1
            if c == 'v':
                arr[21] += 1
            if c == 'w':
                arr[22] += 1
            if c == 'x':
                arr[23] += 1
            if c == 'y':
                arr[24] += 1
            if c == 'z':
                arr[25] += 1
            if c == ' ':
                arr[26] += 1


# In[84]:


e = [0] * 27
e = readfile("e0.txt",e)
e = readfile("e1.txt",e)
e = readfile("e2.txt",e)
e = readfile("e3.txt",e)
e = readfile("e4.txt",e)
e = readfile("e5.txt",e)
e = readfile("e6.txt",e)
e = readfile("e7.txt",e)
e = readfile("e8.txt",e)
e = readfile("e9.txt",e)

eprob = [0] * 27
k = 0
for i in e:
    eprob[k] = (i+.5)/(total+13.5)
    # eprob[k] = round((i+.5)/(total+13.5),4)
    k += 1
print(eprob)


# In[85]:


j = [0] * 27
j = readfile("j0.txt",j)
j = readfile("j1.txt",j)
j = readfile("j2.txt",j)
j = readfile("j3.txt",j)
j = readfile("j4.txt",j)
j = readfile("j5.txt",j)
j = readfile("j6.txt",j)
j = readfile("j7.txt",j)
j = readfile("j8.txt",j)
j = readfile("j9.txt",j)

jprob = [0] * 27
k = 0
for i in j:
    jprob[k] = (i+.5)/(total+13.5)
    # jprob[k] = round((i+.5)/(total+13.5),4)
    k += 1
print(jprob)


# In[86]:


s = [0] * 27
s = readfile("s0.txt",s)
s = readfile("s1.txt",s)
s = readfile("s2.txt",s)
s = readfile("s3.txt",s)
s = readfile("s4.txt",s)
s = readfile("s5.txt",s)
s = readfile("s6.txt",s)
s = readfile("s7.txt",s)
s = readfile("s8.txt",s)
s = readfile("s9.txt",s)

sprob = [0] * 27
k = 0
for i in s:
    sprob[k] = (i+.5)/(total+13.5)
    # sprob[k] = round((i+.5)/(total+13.5),4)
    k += 1
print(sprob)


# In[87]:


e10 = [0] * 27
e10 = readfile("e10.txt",e10)
print(e10)


# In[88]:


# p(x|y)
def calcprob(x,y):
    prob = 0
    k = 0
    for i in x:
        prob += (i * math.log(y[k],10))
        k += 1
    return prob


# In[90]:


print(calcprob(e10,eprob))
print(calcprob(e10,jprob))
print(calcprob(e10,sprob))


# In[91]:


def predict(filename):
    arr = [0] * 27
    arr = readfile(filename,arr)
    e = calcprob(arr,eprob)
    j = calcprob(arr,jprob)
    s = calcprob(arr,sprob)
    if e > j and e > s:
        return "e"
    if j > e and j > s:
        return "j"
    if s > e and s > j:
        return "s"
    return "error"


# In[92]:


print(predict("e10.txt"))
print(predict("e11.txt"))
print(predict("e12.txt"))
print(predict("e13.txt"))
print(predict("e14.txt"))
print(predict("e15.txt"))
print(predict("e16.txt"))
print(predict("e17.txt"))
print(predict("e18.txt"))
print(predict("e19.txt"))


# In[93]:


print(predict("s10.txt"))
print(predict("s11.txt"))
print(predict("s12.txt"))
print(predict("s13.txt"))
print(predict("s14.txt"))
print(predict("s15.txt"))
print(predict("s16.txt"))
print(predict("s17.txt"))
print(predict("s18.txt"))
print(predict("s19.txt"))


# In[94]:


print(predict("j10.txt"))
print(predict("j11.txt"))
print(predict("j12.txt"))
print(predict("j13.txt"))
print(predict("j14.txt"))
print(predict("j15.txt"))
print(predict("j16.txt"))
print(predict("j17.txt"))
print(predict("j18.txt"))
print(predict("j19.txt"))


# In[ ]:




