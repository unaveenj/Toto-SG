import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

def extract_toto_data(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the correct table
    table = soup.find('table')
    if not table:
        print("No table found on the webpage")
        return

    # Extract data from the table
    data = []
    rows = table.find_all('tr')
    for row in tqdm(rows, desc="Processing rows"):
        cells = row.find_all(['th', 'td'])
        if len(cells) == 4:  # Ensuring each row has 4 cells
            outlet = cells[0].get_text(strip=True)
            group1_wins = cells[1].get_text(strip=True)
            group2_wins = cells[2].get_text(strip=True)
            data.append([outlet, group1_wins, group2_wins])

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data, columns=['Outlet', 'Group 1 Wins', 'Group 2 Wins'])

    # Save the DataFrame as 'toto.csv'
    df.to_csv('toto.csv', index=False)

    print("Data extracted and saved as 'toto.csv'")

# URL of the webpage to scrape
url = 'https://www.singaporepools.com.sg/en/product/Pages/toto_wo.aspx'
extract_toto_data(url)
