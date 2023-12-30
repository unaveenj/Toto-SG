import pandas as pd
import datetime


df = pd.read_csv('toto_30-12-2023.csv')  # Replace with the path to your file

# Convert Group 1 and Group 2 wins to numeric values
df['Group 1 Wins'] = pd.to_numeric(df['Group 1 Wins'], errors='coerce')
df['Group 2 Wins'] = pd.to_numeric(df['Group 2 Wins'], errors='coerce')

# Calculate the mean and standard deviation for Group 1 and Group 2 wins
mean_g1 = df['Group 1 Wins'].mean()
std_g1 = df['Group 1 Wins'].std()
mean_g2 = df['Group 2 Wins'].mean()
std_g2 = df['Group 2 Wins'].std()

# Calculate the Z-Scores
df['Group 1 Z-Score'] = (df['Group 1 Wins'] - mean_g1) / std_g1
df['Group 2 Z-Score'] = (df['Group 2 Wins'] - mean_g2) / std_g2

# Calculate the Luckiness Index
df['Luckiness Index'] = (df['Group 1 Z-Score'] + df['Group 2 Z-Score']) / 2


current_date = datetime.datetime.now()
formatted_date = current_date.strftime("%d-%m-%Y")
file_name = f"toto_{formatted_date}_luckiness.csv"


df.to_csv(f'{file_name}', index=False)

print(f"Data processed and saved as '{file_name}'")
