import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')

print(df.describe())
print(df.info())

plt.figure(figsize=(8, 5))
sns.histplot(df['sepal_length'], kde=True)
plt.title('Sepal Length Distribution')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df['petal_length'], kde=True)
plt.title('Petal Length Distribution')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal_length', y='petal_length', hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal_width', y='petal_width', hue='species')
plt.title('Sepal Width vs Petal Width')
plt.xlabel('Sepal Width')
plt.ylabel('Petal Width')
plt.show()

for column in df.select_dtypes(include=[float]).columns:
    mean = df[column].mean()
    std = df[column].std()
    print(f'{column}: mean = {mean}, std = {std}')
