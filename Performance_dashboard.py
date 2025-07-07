import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('student_data.csv')  # columns: student_id, marks, attendance, logins

# Calculations
df['risk'] = (df['attendance'] < 75) | (df['marks'] < 40)

# Correlation
print(df[['marks', 'attendance', 'logins']].corr())

# Visualization
sns.heatmap(df[['marks', 'attendance', 'logins']].corr(), annot=True)
plt.title('Correlation Heatmap')
plt.show()

sns.barplot(x='student_id', y='marks', data=df.sort_values('marks'), palette='coolwarm')
plt.title('Student Performance')
plt.xticks(rotation=90)
plt.show()
