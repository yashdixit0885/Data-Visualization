import matplotlib.pyplot as plt

squares= [1,4,9,16,25]

fig,ax = plt.subplots() # subplots() function can generate one or more plots in the same figure. The variable fig represents the entire figure whereas ax represents one plot in the figure

ax.plot(squares) # We use ax to plot the squares on the figure

plt.show() # Show is used to open the Matplotlib's viewer and display the plot

