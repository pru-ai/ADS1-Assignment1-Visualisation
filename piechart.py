import pandas as pd
import matplotlib.pyplot as plt

# Import HR Analysis Dataset
df_hr = pd.read_csv("HR_Analysis.csv")
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


# Pie chart between the levels of education among the applicants
plt.subplots(figsize = (15, 8))
plt.pie(sumofuniquecounts(df_hr, "department"),
        labels = df_hr['department'].unique())
plt.title("Levels of Education")
plt.ylabel("")

# Saving the Pie Chart as png
plt.savefig("LevelsOfEducation_Piechart.png")
plt.show()


# Pie chart for gender distribution among the applicants
plt.subplots(figsize = (8, 8))
plt.pie(sumofuniquecounts(df_hr, "gender"), labels = ["Male", "Female"],
        explode = [0, 0.1], shadow = True, autopct = "%.2f%%")
plt.title("Gender Distribution", fontsize = 20)
plt.legend()

# Saving the Pie Chart as png
plt.savefig("GenderDistribution_Piechart.png")
plt.show()
