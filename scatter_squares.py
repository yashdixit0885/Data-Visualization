import matplotlib.pyplot as plt

input_values = range(1,100)
squares= [x**2 for x in input_values]
plt.style.use('seaborn')
fig,ax = plt.subplots()


ax.scatter(input_values,squares,c= squares,cmap=plt.cm.Blues,s=10) # c as an argument defines a specific color for the dot plot

ax.set_title("Square Numbers", fontsize=24) # Sets the title of the chart with fontsize parameter describing the size of the font
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set size of tick labels

ax.tick_params(axis='both', labelsize=14)# tick_params() method styles the tick marks on the graph for better view

ax.axis([0,101,0,10001])

plt.show()

