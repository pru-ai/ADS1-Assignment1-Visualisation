import pandas as pd
import matplotlib.pyplot as plt

# Importing World Poverty Data of Countries over the years
df_countries = pd.read_csv("Poverty_Ratio_Dataset.csv")
print(df_countries)
print(df_countries.columns)

# As the third and fourth column have nominal data which are not required for a
# line plot, those columns can be dropped
df_countries.drop(df_countries.columns[[2, 3]], axis = 1, inplace = True)
print(df_countries)

# Data Manipulation to transpose the matrix for a line plot to display the
# changes over years
df_countries_t = pd.DataFrame.transpose(df_countries)

# Setting the first row as column names for the transposed dataframe
# Hence the first two rows are not needed after setting the column names
df_countries_t.columns = df_countries_t.iloc[0]
df_countries_t = df_countries_t.iloc[2:]

# Converting the index to integer datatype so as to plot it n x-axis
df_countries_t.index = df_countries_t.index.astype(int)
print(df_countries_t)


def lineplot(df1, df2, title):
    """ Function to compare poverty rates of two countries by
        creating a lineplot between the index and respective dataframe
        containing single column representing the country's data.

        Arguments:
        Two dataframes with index as "x" and the country specific dataframe
        which has a single column to be taken as "y".
        title (String): Title for the Line plot
    """

    plt.figure()
    plt.plot(df1.index, df1, label = df1.columns.values)
    plt.plot(df2.index, df2, label = df2.columns.values)

    # labelling
    plt.xlabel("Year")
    plt.ylabel("Poverty Headcount Ratio")
    plt.legend()
    plt.title(title)

    # Save the line plot as png
    plt.savefig("PovertyRatioLinePlot.png")
    plt.show()

    return


# Selecting two countries for the line plot and dropping the NA values in each
df_india = df_countries_t[["India"]].dropna()
df_china = df_countries_t[["China"]].dropna()

# Calling lineplot function to plot the poverty rates for India and Argentina
lineplot(df_india, df_china, "Poverty Comparison between China and India")
