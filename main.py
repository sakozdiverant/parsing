import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

USER_LOGIN = os.getenv("USER_LOGIN")
USER_PASSWORD = os.getenv("USER_PASSWORD")
brends = os.getenv("BRENDS").split(', ')
reconect = int(os.getenv("RECONECT_SESION"))
name_file = os.getenv("NAMEFILE")

brends_env = os.getenv("BRENDS", "")
brends = dict(item.split('=') for item in brends_env.split(', '))
columns = ['Бренд','Тип устройства', 'Модель', 'Алматы',
           'Алатау', 'Астана', 'Шымкент', 'Караганда',
           'Pозница', 'Бронза', 'Золото', 'Платина', 'Бриллиант']
df = pd.DataFrame(columns=columns)


login_url = "https://b2b.barlau.kz/?login=yes"
data = {
	"AUTH_FORM": "Y",
	"TYPE": "AUTH",
	"USER_LOGIN": USER_LOGIN,
	"USER_PASSWORD": USER_PASSWORD
}

def create_session():
    session = requests.Session()
    login_response = session.post(login_url, data=data)
    if login_response.status_code == 200 and "logout" in login_response.text.lower():
        print("Авторизация прошла успешно!")
        return session
    else:
        print("Ошибка авторизации. Проверьте логин и пароль.")
        exit()

def make_tab(brend, url):
    resp = session.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    divs = soup.find_all("div", class_="product-card-column")
    for div in divs:
        camera = {}
        title = div.find("a", class_="product-card-column__title").text.strip()
        type_title = div.find("div", class_="product-card-column__data-wrapper-outer__type").text.strip()
        citys_quantity = div.find_all("p", class_="dop-info__item")
        camera['Бренд'] = brend
        camera['Тип устройства'] = " ".join(type_title.split(' ')[:3])
        camera['Модель'] = title
        for city in citys_quantity:
            city_q = city.find("span", class_="dop-info__item-title").text.strip()
            quantity = city.find("span", class_="dop-info__item-value").text.strip()
            quantity = quantity.replace("&gt;", ">").strip()
            camera[city_q] = quantity
        df.loc[len(df)] = camera
    df.to_excel(f"{name_file}.xlsx", index=False)
    print("Данные сохранены в файл cameras.xlsx")

session = create_session()

for brend, brend_id in brends.items():
    for page in range(1, int(brend_id) + 1):
        try:
            # Формируем URL
            if page == 1:
                url = f"http://b2b.barlau.kz/catalog/{brend}/"
            else:
                url = f"http://b2b.barlau.kz/catalog/{brend}/?PAGEN_2={page}"

            # Получаем страницу
            resp = session.get(url)
            soup = BeautifulSoup(resp.text, "html.parser")

            # Проверка на последнюю страницу
            if page != 1:
                try:
                    page_now = int(soup.find("span", class_="block_page_current").text.strip())
                    if page_now != page:
                        print(f"Страница {page - 1} для {brend} была последней.")
                        break
                except Exception as inner_e:
                    print(f"Ошибка определения страницы: {inner_e}")
                    session = create_session()
                    sleep(3)  # Задержка перед переподключением
                    resp = session.get(url)
                    soup = BeautifulSoup(resp.text, "html.parser")


            print(url)
            print(f"Обработка страницы {page} для бренда {brend}...")

            # Проверка валидности страницы
            if resp.status_code != 200:
                print(f"Нет данных на странице {page} для {brend}. Завершаем.")
                break

            # Обработка страницы
            make_tab(brend, url)


            # if page % reconect == 0:
            #     print("Переподключаем сессию...")
            #     session = create_session()
            #     sleep(3)  # Задержка перед переподключением

        except Exception as e:
            print(f"Ошибка: {e}. Переподключаем сессию и продолжаем...")
            session = create_session()
            sleep(3)  # Задержка перед повторной попыткой