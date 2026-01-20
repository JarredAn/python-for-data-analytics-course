print ("Jarand5122")

import pandas as pd
import matplotlib.pyplot as plt

# input data for subject and grade and assign them to logfiles dictionary
logfiles = {"Subject": ["Math", "Science"], "Grade": [92.25, 87.00]}

# Convert dictionary to DataFrame and assign to df
df = pd.DataFrame(logfiles, columns= ["Subject", "Grade"])

# Display the DataFrame
print(df)

# Sort DataFrame by Grade
sorteddf = df.sort_values(by=["Grade"])

# Create bar chart
sorteddf.plot(x = 'Subject', y='Grade', kind = 'bar')
plt.title("Average grade by subject")

# Display chart
plt.show()
