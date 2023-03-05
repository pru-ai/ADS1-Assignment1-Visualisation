import pandas as pd
import matplotlib.pyplot as plt

# Import HR Analysis Dataset
df_hr = pd.read_csv("data/HR_Analysis.csv")
print(df_hr.head())

# Function to calculate column wise sums for plotting a pie chart


def sumofuniquecounts(df, column):
    """ Function to sum the counts of unique values in
        the column

        Arguments:
        df (DataFrame): dataframe
        column (String): Column name from the dataframe
    """
    sum = df_hr.groupby(column).size()
    return sum


# Pie chart between the levels of education among the employees
sumofuniquecounts(df_hr, "education").plot(kind='pie',
                                           subplots = True, figsize = (8, 8))
plt.title("Levels of education", fontsize = 20)
plt.ylabel("")

# Saving the Pie Chart as png
plt.savefig("plots/LevelOfEducation_Piechart.png")
plt.show()


# Pie chart for gender distribution among the employees
plt.subplots(figsize = (8, 8))
plt.pie(sumofuniquecounts(df_hr, "gender"), labels = ["Female", "Male"],
        explode = [0, 0.1], shadow = True, autopct = "%.2f%%")
plt.title("Gender Distribution", fontsize = 20)

# Saving the Pie Chart as png
plt.savefig("plots/GenderDistribution_Piechart.png")
plt.show()
