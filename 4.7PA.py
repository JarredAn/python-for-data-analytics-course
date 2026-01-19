print ("Jarand5122")

import pandas as pd
import matplotlib.pyplot as plt

logfiles = {"Subject": ["Math", "Science"], "Grade": [92.25, 87.00]}

df = pd.DataFrame(logfiles, columns= ["Subject", "Grade"])

print(df)

sorteddf = df.sort_values(by=["Grade"])
sorteddf.plot(x = 'Subject', y='Grade', kind = 'bar')
plt.title("Average grade by subject")
plt.show()
