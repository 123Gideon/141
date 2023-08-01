from bs4 import BeautifulSoup
from selenium import webdriver

import pandas as pd
import requests
import time

Bright_star_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browers=requests.get(Bright_star_url)
# browers.get(Bright_star_url)

time.sleep(10)

headers=["name","distance","mass","radius"]

soup=BeautifulSoup(browers.text,"html.parser")
startable=soup.find("table")
starlist=[]
tablerows=startable.find_all("tr")
for tr in tablerows:
    td=tr.find_all("td")
    rows=[i.text.rstrip() for i in td]
    starlist.append(rows)
print(starlist)
star_name=[]
star_mass=[]
star_distance=[]
star_raduis=[]
print(len(starlist))
for i in range(1,len(starlist)):
    star_name.append(starlist[i][1])
    star_mass.append(starlist[i][5])
    star_distance.append(starlist[i][3])
    star_raduis.append(starlist[i][6])

data=pd.DataFrame(list(zip(star_name,star_distance,star_mass,star_raduis)),columns=headers)
data.to_csv("Bright_star.csv")    
