import csv
import pandas as pd

# Load the data
data = pd.read_csv('baby2yo_responses_bytrial.csv')

# Calculate accuracy for each category
accuracy_by_category = data.groupby('Condition')['IsCorrect'].mean().dropna()

# Convert to a DataFrame for better readability
accuracy_df = accuracy_by_category.reset_index()
accuracy_df.rename(columns={'IsCorrect': 'Accuracy'}, inplace=True)

# Display results sorted by accuracy
accuracy_df.sort_values(by='Accuracy', ascending=False)


print(accuracy_df)