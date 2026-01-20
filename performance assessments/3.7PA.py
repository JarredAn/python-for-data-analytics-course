import pandas as pd
import matplotlib.pyplot as plt

print("Jarand5122")

data = {'Names': ['Ballroom 1', 'Ballroom 2', 'Ballroom 3'], 'Capacity': [25000, 11000, 5000]}
df = pd.DataFrame(data,columns = ['Names', 'Capacity'])
print(df)

data = {'Names': ['Ballroom 1', 'Ballroom 2', 'Ballroom 3'], 'Capacity': [25000, 11000, 5000]}
df = pd.DataFrame(data,columns = ['Names', 'Capacity'])
df.plot(x = 'Names', y = 'Capacity', kind = 'bar')
plt.show()

data = {"Attendees":[45, 35, 20]}
df = pd.DataFrame(data, index=["Children", "Adults", "Teens"])
df.plot.pie(y = "Attendees")
plt.show()