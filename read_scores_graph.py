import matplotlib.pyplot as plt

# Read the scores.csv file
file_path = r"C:\PythonFiles\scores.csv"
file = open(file_path, 'r')

# Lists to store names and scores
names = []
scores = []

# Read each line and extract names and scores
for line in file:
    # Split by comma
    parts = line.strip().split(',')
    names.append(parts[0].strip())
    scores.append(int(parts[1].strip()))

# Close the file
file.close()

# Create the bar graph
plt.bar(names, scores)
plt.xlabel('Student Names')
plt.ylabel('Test Scores')
plt.title('Jarand5122 Graph Practice')
plt.ylim(0, 110)  # Set y-axis range from 0 to 110

# Display the graph
plt.show()
