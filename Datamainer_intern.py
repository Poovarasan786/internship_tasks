import requests
from bs4 import BeautifulSoup
import csv

# Function to fetch and parse HTML content
def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Function to extract relevant information (e.g., titles, descriptions, etc.)
def parse_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Example: Extract all the headlines (Assuming the website has <h2> tags for headlines)
    data = []
    for headline in soup.find_all('h2'):
        title = headline.get_text(strip=True)
        link = headline.find('a')['href'] if headline.find('a') else 'No link'
        data.append([title, link])
    
    return data

# Function to save the data into a CSV file
def save_to_csv(data, filename):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Link'])  # CSV headers
            writer.writerows(data)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

# Main scraping function
def scrape_website(url, output_file):
    html_content = fetch_html(url)
    if html_content:
        data = parse_data(html_content)
        if data:
            save_to_csv(data, output_file)
        else:
            print("No data found to scrape.")
    else:
        print("Failed to retrieve the webpage.")

# URL of the website to scrape
website_url = 'https://example.com'  # Replace with the target website
output_csv = 'scraped_data.csv'

# Start scraping
scrape_website(website_url, output_csv)
