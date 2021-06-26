#importando as bibliotecas necess?rias
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import csv

# endereço URL dos dispositivos iphone no site da amazon
url = 'https://www.amazon.com/s?k=iphone&ref=nb_sb_noss_2'

#variavel para armazenar e abrir a url
html = urlopen(url)

#iniciando o objeto bs4
bsObj = BeautifulSoup(html, 'lxml')
def getTitle(url):
    try:
       html
    except HTTPError as e:
        return None
    try:
        bsObj
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle(url)

if title == None:
    print("Title could not be found")
else:
    print(title)
# criar array para os nomes dos iphones
device = []

# criar array para os pre?os dos iphones
price = []

# listar os dados encontrados
for name in bsObj.find_all('div',class_='s-include-content-margin'):

    # adiciona ao array device os dados encontrados
    device.append(name.find('span', class_='a-text-normal').get_text())

    # adiciona ao array price os dados encontrados
    price.append(str(name.find('span', class_='a-price-whole').text))

    # definindo o dataframe
    df = pd.DataFrame({
        "Device Iphone":device,
        "Price Device Iphone":price
    })

    # definindo o nome da coluna index
    df.index.name = 'Index'

    # mostrando os dados no terminal
    print(df)

    # criar arquivo excel csv
    df.to_csv('files/amazon.csv')
