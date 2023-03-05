import pandas as pd
import matplotlib.pyplot as plt

df_hr = pd.read_csv("HR_Analysis.csv")
print(df_hr.head())


df = df_hr.groupby('department').size()
df.plot(kind='pie', subplots=True, figsize=(15, 8))
plt.title("Pie Chart of different types of education")
plt.ylabel("")
#plt.show()

size = [38496, 16312]
labels = "Male", "Female"
explode = [0, 0.1]

plt.subplots(figsize=(8,8))
plt.pie(size, labels = labels, explode = explode, shadow = True, autopct = "%.2f%%")
plt.title('A Pie Chart Representing GenderGap', fontsize = 20)
plt.legend()
plt.show()