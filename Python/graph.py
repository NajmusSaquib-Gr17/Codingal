import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

# Plot the data
plt.plot(x, y, marker='o')  # Line with dots
plt.title('Simple Line Graph')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)

# Show the graph
plt.show()
