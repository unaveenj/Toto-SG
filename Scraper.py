import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import datetime

def extract_toto_data(url):

    response = requests.get(url)


    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return


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

    df = pd.DataFrame(data, columns=['Outlet', 'Group 1 Wins', 'Group 2 Wins'])


    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%d-%m-%Y")
    file_name = f"toto_{formatted_date}.csv"
    df.to_csv(f'{file_name}', index=False)

    print(f"Data extracted and saved as '{file_name}")

# URL of the webpage to scrape
url = 'https://www.singaporepools.com.sg/en/product/Pages/toto_wo.aspx'
extract_toto_data(url)
