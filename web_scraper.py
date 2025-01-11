import requests
from bs4 import BeautifulSoup
import csv

# The URL of the website you want to scrape
url = 'https://Amazon.com'  # This is the website I want to scrape

# Send an HTTP request to the website and get the HTML response
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize a list to store the data we want to scrape
data = []

# Extract data from the website
# Assuming you're extracting product titles and prices within 'div' elements with the class 'item'
for item in soup.find_all('div', class_='item'):
    title = item.find('h2').text  # Find the title within the 'h2' tag
    price = item.find('span', class_='price').text  # Find the price within the 'span' tag with class 'price'
    
    # Append the extracted data as a list
    data.append([title, price])

# Write the extracted data to a CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price'])  # Write the header
    writer.writerows(data)  # Write the data rows

print("Data has been saved to data.csv")