#!/usr/bin/env python
# coding: utf-8

# In[142]:


import matplotlib.pyplot as plt
import numpy as np
print(matplotlib.__version__)


# In[64]:


fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4, 5], [1, 5, 3, 4, 5])


# In[65]:


# Multiple subplots in one figure
x = np.linspace(0, 2, 100)
fig, ax = plt.subplots(2, 2)
ax[0][0].plot(x, x)
ax[0][1].plot(x, x**2)
ax[1][0].plot(x, x**3)
ax[1][1].plot(x, x**4)


# In[66]:


x = np.linspace(0, 2, 100)
fig, ax = plt.subplots(1, 2)
ax[0].plot(x, x)
ax[1].plot(x, x**2)


# In[67]:


x = np.linspace(0, 2, 100)
fig, ax = plt.subplots()
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.plot(x, x**3, label='cubic')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple Plot")
ax.legend()


# In[89]:


# Line Plot
x = [1, 2, 3, 4, 5]
y = [1, 5, 3, 5, 1]
plt.plot(x, y)
plt.xlabel('My X Level')
plt.ylabel('My Y Level')
plt.show()


# In[97]:


x = [1, 2, 3, 4, 5]
y = [1, 5, 3, 5, 1]
plt.plot(x, y, linewidth=5.0)
plt.show()


# In[105]:


x = [1, 2, 3, 4, 5]
y = [1, 5, 3, 5, 1]
plt.plot(x, y)
plt.show()
plt.plot(x, y, '-')
plt.show()
plt.plot(x, y, '--')
plt.show()
plt.plot(x, y, 'r--')
plt.show()
plt.plot(x, y, 'ro')
plt.show()
plt.plot(x, y, 'g^')
plt.show()
plt.plot(x, y, '-.')
plt.show()
plt.plot(x, y, ':')
plt.show()


# In[109]:


# Working with Image
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# In[124]:


img = mpimg.imread('a.jpeg')
lum_img = img[:, :, 0]


# In[125]:


imgplot = plt.imshow(img)


# In[127]:


plt.imshow(lum_img)


# In[129]:


plt.imshow(lum_img, cmap="hot")


# In[130]:


imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')


# In[132]:


imgplot = plt.imshow(lum_img)
plt.colorbar()


# In[137]:


imgplot = plt.imshow(lum_img, clim=(0.1, 0.2))


# In[138]:


# Bar Chart
# x-coordinates of left sides of bars  
left = [1, 2, 3, 4, 5] 
  
# heights of bars 
height = [10, 24, 36, 40, 5] 
  
# labels for bars 
tick_label = ['one', 'two', 'three', 'four', 'five'] 
  
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['red', 'green']) 
  
# naming the x-axis 
plt.xlabel('x - axis') 
# naming the y-axis 
plt.ylabel('y - axis') 
# plot title 
plt.title('My bar chart!') 
  
# function to show the plot 
plt.show()


# In[139]:


# Histogram
# frequencies 
ages = [2,5,70,40,30,45,50,45,43,40,44, 
        60,7,13,57,18,90,77,32,21,20,40] 
  
# setting the ranges and no. of intervals 
range = (0, 100) 
bins = 10  
  
# plotting a histogram 
plt.hist(ages, bins, range, color = 'green', 
        histtype = 'bar', rwidth = 0.8) 
  
# x-axis label 
plt.xlabel('age') 
# frequency label 
plt.ylabel('No. of people') 
# plot title 
plt.title('My histogram') 
  
# function to show the plot 
plt.show() 


# In[140]:


# Scatter plot
# x-axis values 
x = [1,2,3,4,5,6,7,8,9,10] 
# y-axis values 
y = [2,4,5,7,6,8,9,11,12,12] 
  
# plotting points as a scatter plot 
plt.scatter(x, y, label= "stars", color= "green",  
            marker= "*", s=30) 
  
# x-axis label 
plt.xlabel('x - axis') 
# frequency label 
plt.ylabel('y - axis') 
# plot title 
plt.title('My scatter plot!') 
# showing legend 
plt.legend() 
  
# function to show the plot 
plt.show() 


# In[141]:


# Pie-chart
# defining labels 
activities = ['eat', 'sleep', 'work', 'play'] 
  
# portion covered by each label 
slices = [3, 7, 8, 6] 
  
# color for each label 
colors = ['r', 'y', 'g', 'b'] 
  
# plotting the pie chart 
plt.pie(slices, labels = activities, colors=colors,  
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0), 
        radius = 1.2, autopct = '%1.1f%%') 
  
# plotting legend 
plt.legend() 
  
# showing the plot 
plt.show() 


# In[144]:


from matplotlib.backends.backend_pdf import PdfPages
pdf = PdfPages('multipage.pdf')

fig1 = plt.figure()
plt.plot([0,1,2,3,4])
plt.close()
pdf.savefig(fig1)

fig1 = plt.figure()
plt.plot([0,1,2,3,4])
plt.close()
pdf.savefig(fig1)

pdf.close()

