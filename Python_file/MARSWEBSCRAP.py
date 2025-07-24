# Importing necessary libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name = []
Prices = []
Reviews = []

# Print a success message
print("Libraries imported successfully!")

for x in range(1, 2):  # You can increase range for more pages
    url = f"https://marscosmetics.in/collections/bestsellers?page={x}"
    
    r = requests.get(url)
    print(r)

    soup = BeautifulSoup(r.text, 'lxml')
    #print(soup)

    #****PRODUCT NAME****
    names = soup.find_all("a", class_ = "card_titl_height card__title caption" )

    for i in names:
        name = i.text.strip()
        Product_name.append(name)

    #print(Product_name)


    #print(len(Product_name))
    #print(names)

    #***PRICES OF PRODUCT***
    price = soup.find_all("span", class_= "price-item price-item--regular" )

    for i in price:
        cp = i.text.strip()
        Prices.append(cp)

    #print(Prices)

    #***REVIEWS OF PRODUCT***
    review = soup.find_all("div", class_= "scm-reviews-rate" )

    for i in review:
        rating = i.text
        Reviews.append(rating)

    #print(Reviews)

    df = pd.DataFrame({"Product Name":Product_name, "Prices":Prices})
    print(df)
