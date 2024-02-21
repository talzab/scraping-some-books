# Scraping Some Books

## Description
This Python script scrapes information from http://books.toscrape.com for each book, including the title, current price, Universal Product Code (UPC), and a link to the page with further details. The script organizes the data and outputs it in CSV format.

## How to Use
1. Clone the repository:
   
`
git clone https://github.com/your-username/scraping-some-books.git
`

2. Navigate to the project directory:

`
cd scraping-some-books
`

3. Install the required Python packages:

`
pip install beautifulsoup4
`

4. Run the script:

`
python scrape-books.py books.csv
`

This command will execute the script and redirect the output to a file named books.csv. The CSV file will contain four columns: title, link, price, and UPC.




