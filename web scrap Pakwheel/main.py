import pandas as pd
import requests
from bs4 import BeautifulSoup



product_names = []  # Correct initialization

price = []  # Correct initialization

location= []  # Correct initialization


for i in range(2,10):
    web=requests.get("https://www.pakwheels.com/used-cars/automatic/57336")
        # print(web)

    soup=BeautifulSoup(web.text,"html.parser")

    

    pro_nam = soup.find_all("a", class_="car-name ad-detail-path")
    # Initialize the list to store product names
    # print(pro_nam) # Correct initialization
        # print(soup)
        
    for i in pro_nam:
        name=i.text.strip() 
        product_names.append(name)

    # print(product_names)

    price_elements = soup.find_all("div", class_="price-details generic-dark-grey")

    for i in price_elements:
        pr_name = i.text.strip()  
        price.append(pr_name)

    # print(price)

    location_elements = soup.find_all("ul", class_="list-unstyled search-vehicle-info fs13")

    for i in location_elements:
        loc_elements = i.text.strip()  
        location.append(loc_elements)

    # print(location)


    np = soup.find("li", class_="page").find("a").get("href")
    cnp="https://www.pakwheels.com"+np
    # print(cnp)

    
for i in range(2, 10):    
    full_url = f"{cnp}?page={i}" # Correct initialization

    # print(full_url)    

df=pd.DataFrame({"product_names":product_names,"price":price,"location":location})
# print(df)

df.to_csv("C:\\Users\\basit\\Downloads\\web scrap flipcart\\Car Data.csv", index=False)



