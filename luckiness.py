import pandas as pd

# Load the data
df = pd.read_csv('toto_complete_address_v2.csv')  # Replace with the path to your file

# Convert Group 1 and Group 2 wins to numeric values in case they are not
df['Group 1 Wins'] = pd.to_numeric(df['Group 1 Wins'], errors='coerce')
df['Group 2 Wins'] = pd.to_numeric(df['Group 2 Wins'], errors='coerce')

# Calculate percentile ranks for Group 1 and Group 2 wins
df['Group 1 Percentile Rank'] = df['Group 1 Wins'].rank(pct=True) * 100
df['Group 2 Percentile Rank'] = df['Group 2 Wins'].rank(pct=True) * 100

# Calculate average percentile rank and scale it to 0-10 for Luckiness score
df['Luckiness'] = ((df['Group 1 Percentile Rank'] + df['Group 2 Percentile Rank']) / 2) / 10

# Save the DataFrame with the new 'Luckiness' column as 'toto2.csv'
df.to_csv('toto3.csv', index=False)

print("Data processed and saved as 'toto3.csv'")
