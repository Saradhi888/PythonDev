import pandas as pd
import requests
from bs4 import BeautifulSoup

#page = requests.get("https://mausam.imd.gov.in/imd_latest/contents/citizen_charter.php")
page = requests.get("https://mausam.imd.gov.in/")
soup = BeautifulSoup(page.content,'html.parser')

#print all the data from page
#print(soup)

#print list of a tags
#print(soup.find_all('a'))

#list_images = soup.find(id = "images")
#print (list_images)

#image = list_images.find_all(class_ = "magnify")
#print(image[2])



services = soup.find(id = "services")
#print (services)

list_content = services.find_all("li")
#print(list_content)
#print(list_content[0])
#print(list_content[0].get_text())

#if each list have p tag with class you get the inner details
#print(list_content[0].find_all(class_ = "short_desc").get_text())

services = [item.get_text() for item in list_content]
print (services)
dup_servc = [item+"_1" for item in services]
#['Rainfall Information ', 'Monsoon', 'Cyclone', 'Agromet Advisory Services ', 'Climate Services', 'City Forecast ']


services_stuff = pd.DataFrame(
                  { 'services':services,
                    'dup_servc':dup_servc,
                  })
print(services_stuff)

services_stuff.to_csv('services.csv')


