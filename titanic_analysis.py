import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset
data = pd.read_csv("titanic.csv")

# Show first 5 rows
print("Preview of dataset:")
print(data.head())

# Basic info
print("\nSummary of data:")
print(data.info())

# Survival count
print("\nSurvival count:")
print(data['Survived'].value_counts())

# Plot survival count
sns.countplot(x='Survived', data=data)
plt.title("Survival Count (0 = Died, 1 = Survived)")
plt.show()

# Average age of survivors vs non-survivors
print("\nAverage age of survivors vs non-survivors:")
print(data.groupby('Survived')['Age'].mean())

# Gender-based survival
sns.countplot(x='Survived', hue='Sex', data=data)
plt.title("Survival by Gender")
plt.show()

# Class-based survival
sns.countplot(x='Survived', hue='Pclass', data=data)
plt.title("Survival by Passenger Class")
plt.show()

import pandas as pd

# Load the CSV
data = pd.read_csv("titanic.csv")

# Preview first 5 rows
data.head()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("titanic.csv")
data.head()

sns.countplot(x='Survived', hue='Sex', data=data)
plt.title("Survival by Gender")
plt.show()
