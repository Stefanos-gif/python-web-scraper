#run pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
URL = 'http://google.com'
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links on the page
    links = soup.find_all('a')

    # Open a CSV file to save the links
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Link'])

        # Write each link to the CSV file
        for link in links:
            writer.writerow([link.get('href')])

    print("Data scraped and saved to scraped_data.csv")
else:
    print("Failed to retrieve the webpage.")
