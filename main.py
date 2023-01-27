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

# The majority of patients are between 50 and 60
# There is a decrease in patients between the ages of 47-and 50

# "trtbps" variable
sns.distplot(df["trtbps"], hist_kws=dict(linewidth=1, edgecolor="k"), bins=20)
plt.show()

# The resting blood pressure of most patients is mostly between 110 and 140

# "chol" variable
sns.distplot(df["chol"], hist=False)
plt.show()

# Cholesterol value in most patients is between 200-and 280

# "thalach" variable
x, y = plt.subplots(figsize=(8, 6))
sns.distplot(df["thalachh"], hist=False, ax=y)
y.axvline(df["thalachh"].mean(), color="r", ls="--")
plt.show()

# The maximum heart rate in most patients is between 145-and 170

# "oldpeak" variable
x, y = plt.subplots(figsize=(8, 6))
sns.distplot(df["oldpeak"], hist_kws=dict(linewidth=1, edgecolor="k"), bins=20, ax=y)
y.axvline(df["oldpeak"].mean(), color="r", ls="--")
plt.show()

# Values of the ST depression induced by exercise relative to rest in the majority of patients between 0 and 1.5.

# Categorical Variables(analysis with Pie Chart)

categoric_axis_name = ["Gender", "Chest Pain Type", "Fasting Blood sugar", "Resting Electrocardiographic Results",
                      "Exercise Induced Angina", "The Slope of ST Segment", "Number of Major Vessels", "Thal", "Target"]

list(zip(categoric_var, categoric_axis_name))

print(line_separator)

for i, z in list(zip(categoric_var, categoric_axis_name)):
    fig, ax = plt.subplots(figsize=(8, 6))

    observation_values = list(df[i].value_counts().index)
    total_observation_values = list(df[i].value_counts())

    ax.pie(total_observation_values, labels=observation_values, autopct='%1.1f%%', startangle=110, labeldistance=1.1)
    ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title((i + "(" + z + ")"))  # Naming Pie Chart Titles
    plt.legend()
    plt.show()

# Sex Variable
# 68.3% of the patients are male, 31.7% are female.
# The number of male patients is more than twice that of female patients.

# Cp Variable (chest pain type (1 = typical angina; 2 = atypical angina; 3 = non-anginal pain; 0 = asymptomatic)
# 47.2% of the patients asymptomatic (type 0). They have pain without symptoms.
# 28.7% of the patients have an atypical angina (type 2). Means they have shortness of breath or non-classical pain.
# 16.5% of patients have a typical angina (type 1). It is the classic exertion pain that comes during any physical activity.
# 7.6% of patients have a non-anginal pain (type 3).It means chest pain that is not caused by heart disease or a heart attack.

# Fbs Variable (fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
# 85.1% of patients have an observation value of 1
# The fasting blood sugar of these patients is more than 120 mg/dl






