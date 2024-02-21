from bs4 import BeautifulSoup
import requests
import csv

page_number = 1
book_list = []  # Use a list to store dictionaries

while True:
    # Construct the URL for the current page
    url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
    
    # Make a request to the current page
    r = requests.get(url)

    # Check if the page is not found (status code 404)
    if r.status_code == 404:
        break  # Break the loop if the page is not found

    # Parse the HTML content of the current page
    soup = BeautifulSoup(r.content, 'html.parser')

    # Use CSS selectors to extract a list of elements containing book details
    books = soup.select("h3 a")
    prices = soup.select(".product_price .price_color")

    # Loop through the elements and append a dictionary for each book
    for book, price in zip(books, prices):
        book_title = book['title']
        book_url = "http://books.toscrape.com/catalogue/" + book['href']
        book_price = price.text

        # Make a request to the book details page
        book_r = requests.get(book_url)  # Use a different variable for the book details page
        book_soup = BeautifulSoup(book_r.content, 'html.parser')

        # Extract the UPC information
        upc = book_soup.select(".table.table-striped th:contains('UPC') + td")
        book_upc = upc[0].text if upc else "N/A"

        # Create a dictionary with book information and append it to the list
        book_info = {
            "title": book_title,
            "link": book_url,
            "price": book_price,
            "UPC": book_upc
        }
        book_list.append(book_info)
    
    # Move to the next page
    page_number += 1 

# Print the list of dictionaries (for debugging purposes)
# print(book_list)

# Write the book information to a CSV file
csv_columns = ['title', 'link', 'price', 'UPC']
csv_file = 'books.csv'

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for book_info in book_list:
        writer.writerow(book_info)

print(f"CSV file '{csv_file}' created successfully.")
