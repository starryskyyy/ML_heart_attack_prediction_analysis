# Importing libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno
import warnings

warnings.filterwarnings("ignore")

line_separator = "\n"

# Reading both csv files and display 5 first rows to make sure that data imported correctly.
df = pd.read_csv('heart.csv')
print(df.head())

o2Saturation = pd.read_csv('o2Saturation.csv')
print(o2Saturation.head())

# Print Data Frame shape.
print("\nShape of Data Frame:", df.shape)

print(line_separator)
df.info()

# The Data Frame consists of total 303 Rows and 14 Columns.
# The type of all the variables in the data frame are in numerical format.

# *********************** Missing Values ***********************

# We have to make sure that there is no missing values in the Data Frame.
# It is important in Machine Learning because it affects accuracy.
print(line_separator)
print(df.isnull().sum())

# Visualizing the missing data
missingno.bar(df, color="b")
plt.show()

# Data Frame has no missing data - bars are all full in the graph.

# ***********************  Unique Values ***********************
# According to the result we determined the variables with few unique values as categorical variables,
# and the variables with high unique values as numeric variables.

# Numeric Variables: "age", "trtbps", "chol", "thalachh" and "oldpeak"
# Categorical Variables: "sex", "cp", "fbs", "restecg", "exng", "slp", "caa", "thall", "output"

unique_number = []
for i in df.columns:
    x = df[i].value_counts().count()
    unique_number.append(x)

print(line_separator)
print(pd.DataFrame(unique_number, index=df.columns, columns=["Total Unique Values"]))

# Separating variables (Numeric or Categorical)

numeric_var = ["age", "trtbps", "chol", "thalachh" and "oldpeak"]
categoric_var = ["sex", "cp", "fbs", "restecg", "exng", "slp", "caa", "thall", "output"]

# Display basic statistics of numerical data

print(line_separator)
print(df[numeric_var].describe())

# Analyzing different graphs.

# "age" variable
sns.distplot(df["age"], hist_kws=dict(linewidth=1, edgecolor="k"))
plt.show()

# The minimum age is 29, and the maximum is 77.
# The data average is in the middle of the 25% and 75% quarters.
# This means that the age variable is prone to the normal distribution.

# "trtbps" variable
sns.distplot(df["trtbps"], hist_kws=dict(linewidth=1, edgecolor="k"), bins=20)
plt.show()

# The minimum value for the "trtbps" (resting blood pressure (in mm Hg))
# variable is 94, and the maximum is 200. The average is 147.
# The major average is 131.
# This data is prone to a normal distribution, but there is a slight right skew.

# "chol" variable
sns.distplot(df["chol"], hist=False)
plt.show()


