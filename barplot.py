import pandas as pd
import matplotlib.pyplot as plt

df_wineproduction = pd.read_csv("Wine_Data.csv", index_col=0)
print(df_wineproduction.head())
print(df_wineproduction.columns)

# Checking the number of countries and provinces in the dataset
print("Number of Countries producing wine: ",
      df_wineproduction["country"].unique().size)
print("Number of Provinces producing wine: ",
      df_wineproduction["province"].unique().size)

# Plotting a bar plot for 49 countries or 456 provinces is not realistic and
# very messy. So defining a function that selects the top ten from that
# respective category i.e. column


def barplotfortopten(df, column):
    """ Function to select top ten by summing the counts of unique values in
        the column and taking the first ten values

        Arguments:
        df (DataFrame): dataframe
        column (String): Column name from the dataframe
    """
    # Slicing the top ten by the summation of counts of the unique values
    top_ten = df[column].value_counts()[:10]

    # Plotting a bar plot for the top ten
    top_ten.plot(kind='bar', figsize=(10, 6))
    plt.legend()

    # Save the plots as png based on the column name
    plt.tight_layout()
    plt.savefig("TopTenBy" + column.capitalize() + ".png")
    plt.show()

    return


# Bar plot for the Top Ten Countries producing wine
barplotfortopten(df_wineproduction, "country")

# Bar plot for the Top Ten Provinces producing wine
barplotfortopten(df_wineproduction, "province")
