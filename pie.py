import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_pie_chart():
    # Data for the pie chart
    labels = ['Label 1', 'Label 2', 'Label 3']
    sizes = [30, 40, 30]
    colors = ['red', 'green', 'blue']

    # Create a Figure and Axes
    fig = Figure(figsize=(5, 5))
    ax = fig.add_subplot(111)

    # Plot the pie chart
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

    # Create a canvas to display the pie chart in the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Create the tkinter window
window = tk.Tk()
window.title('Simple Pie Chart')

# Create the pie chart on a button click
button = tk.Button(window, text="Show Pie Chart", command=create_pie_chart)
button.pack()

# Start the tkinter main loop
window.mainloop()