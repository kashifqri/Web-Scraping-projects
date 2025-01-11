import requests
from bs4 import BeautifulSoup
import pandas as pd

web=requests.get("https://www.iplt20.com/auction")

# print(web)

soup=BeautifulSoup(web.text,"html.parser")

table=soup.find("table",class_="ih-td-tab auction-tbl")

# print(table)

title=table.find_all("th")
# print(title)

header = []

for i in title:
    name = i.text.strip()
    header.append(name)

df = pd.DataFrame(columns=header)

# print(df)
    


rows=table.find_all("tr")
# print(row)

for i in rows[1:]:
    first_td=i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()

    data=i.find_all("td")[1:]
    row_data =[ tr.text for tr in data]
    # print(rows)
    row_data.insert(0, first_td)
    l=len(df)
    df.loc[l]= row_data 

print(df)    

df.to_csv("Ipl auction stats.csv")
