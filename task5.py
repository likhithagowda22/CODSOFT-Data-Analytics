import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Request webpage
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Lists
titles = []
prices = []

# Extract book details
books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    titles.append(title)
    prices.append(price)

# Create DataFrame
df = pd.DataFrame({
    "Book Title": titles,
    "Price": prices
})

# Display data
print(df.head())

# Save CSV
df.to_csv("books_data.csv", index=False)

print("\nWeb Scraping Completed Successfully!")
print("Data saved as books_data.csv")