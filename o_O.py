import requests
from bs4 import BeautifulSoup
import pandas as pd

# Создаем пустой DataFrame с именами столбцов
columns = ['Город', 'Район', 'Улица', 'Комнат', 'Размер', 'Цена', 'Ссылка']
df = pd.DataFrame(columns=columns)

for count in range(1, 2):
    if count == 1:
        url = f"https://krisha.kz/prodazha/kvartiry/shymkent/?das[live.rooms]=4"
    else:        
        url = f"https://krisha.kz/prodazha/kvartiry/shymkent/?das[live.rooms]=4&page={count}"

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    divs = soup.find_all("div", class_="a-card")
    
    for div_data in divs:        
        img_tag = div_data.find("img")
        alt_text = img_tag.get("alt")
        elements = [elem.strip() for elem in alt_text.split(',')]

        # Проверяем, есть ли все необходимые элементы
        

        
        if len(elements) == 5:            
            apartment_type = elements[0]
            area = elements[1]
            location = elements[2]
            price_city = elements[3].split(" в ")
            street = price_city[0].split(" за ")[0]
            if price_city[0].find(' ~ ') != -1:
                price = price_city[0].split(" ~ ")[1].split(" ")[0]
            else:
                if len(price_city[0].rsplit(" за ", 1)) == 2:
                    street = price_city[0].rsplit(" за ", 1)[0]
                    price = price_city[0].rsplit(" за ", 1)[1]                    
                else:
                    price = price_city[0].split(" за ")[1].split(" ")[0]
                
            city = price_city[1].strip()
            print(1, apartment_type)
            print(2, area)
            print(3,location)
            print(4, street)
            print(5, price)
            print(6, city)
            print("__________________________________")
        elif len(elements) == 4:
            print(len(elements))
            apartment_type = elements[0]
            area = elements[1]
            location = 'NoN'
            price_city = elements[2].split(" в ")
            street = price_city[0].split(" за ")[0]
            try:
                city = price_city[1]
            except:
                print(elements)
            if price_city[0].find(' ~ ') != -1:
                price = price_city[0].split(" ~ ")[1].split(" ")[0]
            else:
                price = price_city[0].split(" за ")[1].split(" ")[0] 
            print(1, apartment_type)
            print(2, area)
            print(3,location)
            print(4, street)
            print(5, price)
            print(6, city)
            print("__________________________________")  
        elif len(elements) == 3:
            print(len(elements))
            print("__________________________________")
        else:
            continue
            print(len(elements))