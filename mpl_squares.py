import matplotlib.pyplot as plt

input_values = [1,2,3,4,5] #input data set
squares= [1,4,9,16,25] #Output data set

plt.style.use('seaborn') # There are a lot of in-built styles available that you can check using plt.style.available

fig,ax = plt.subplots() # subplots() function can generate one or more plots in the same figure. The variable fig represents the entire figure whereas ax represents one plot in the figure

ax.plot(input_values,squares, linewidth=3) # We use ax to plot the squares on the figure. Plot() method plots the graph in a meaningful way and linewidth parameter tells the thickness of the line

# Set chart title and label axes

ax.set_title("Square Numbers", fontsize=24) # Sets the title of the chart with fontsize parameter describing the size of the font
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set size of tick labels

ax.tick_params(axis='both', labelsize=14)# tick_params() method styles the tick marks on the graph for better view


plt.show() # Show is used to open the Matplotlib's viewer and display the plot

