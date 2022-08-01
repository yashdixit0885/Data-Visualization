import matplotlib.pyplot as plt

input_values = [1,2,3,4,5] #input data set
squares= [1,4,9,16,25] #Output data set
plt.style.use('seaborn')
fig,ax = plt.subplots()


ax.scatter(input_values,squares,s=100)

ax.set_title("Square Numbers", fontsize=24) # Sets the title of the chart with fontsize parameter describing the size of the font
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set size of tick labels

ax.tick_params(axis='both', labelsize=14)# tick_params() method styles the tick marks on the graph for better view

plt.show()