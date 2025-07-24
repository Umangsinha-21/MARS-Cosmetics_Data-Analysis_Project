import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Reviews = []

print("Libraries imported successfully!")

page = 1

while True:
    url = f"https://marscosmetics.in/collections/bestsellers?page={page}"
    r = requests.get(url)
    print(f"Fetching: {url} -> {r.status_code}")

    if r.status_code != 200:
        print("Stopped - Page not found.")
        break

    soup = BeautifulSoup(r.text, 'lxml')

    names = soup.find_all("a", class_="card_titl_height card__title caption")
    prices = soup.find_all("span", class_="price-item price-item--regular")
    reviews = soup.find_all("div", class_="scm-reviews-rate")

    # Stop when no products are found
    if not names:
        print("No more products found. Stopping...")
        break

    for i in names:
        name = i.text.strip()
        Product_name.append(name)

    for i in prices:
        cp = i.text.strip()
        Prices.append(cp)

    for i in reviews:
        rating = i.text.strip()
        Reviews.append(rating)

    page += 1  # move to next page

# Trim lists to same length if necessary
min_len = min(len(Product_name), len(Prices))
df = pd.DataFrame({
    "Product Name": Product_name[:min_len],
    "Prices": Prices[:min_len],
    # "Reviews": Reviews[:min_len]  # optional
})

print(df)

df.to_csv("mars_cosmetics_bestsellers.csv", index=False)
