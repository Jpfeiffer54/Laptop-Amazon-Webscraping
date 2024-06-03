# import libraries
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import pandas as pd

# Connecting to Website
url = 'https://www.amazon.com/Alienware-M18-Gaming-Laptop-i9-14900HX/dp/B0CWHGBWL6?ref_=ast_sto_dp&th=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36","Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content,'html.parser')
soup = BeautifulSoup(soup.prettify(),'html.parser')
title = soup.find(id ='productTitle').get_text(strip=True)
price = soup.find(class_='aok-offscreen').get_text(strip=True)
title=title.strip()[0:30]
price = price.strip()[1:]
print(title)
print(price)

today = datetime.date.today()
print(today)

#Creating csv
import csv
header = ['Product','Price','Date']
data = [title,price,today]

with open('AmazonScrapingLaptop.csv','w',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

#Appending csv
with open('AmazonScrapingLaptop.csv','a+',newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

#Function for checking price
def check_price():
    url = 'https://www.amazon.com/Alienware-M18-Gaming-Laptop-i9-14900HX/dp/B0CWHGBWL6?ref_=ast_sto_dp&th=1'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36","Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    soup = BeautifulSoup(soup.prettify(),'html.parser')
    title = soup.find(id ='productTitle').get_text(strip=True)
    price = soup.find(class_='aok-offscreen').get_text(strip=True)
    title=title.strip()[0:30]
    price = price.strip()[1:]
    today = datetime.date.today()
    header = ['Product','Price','Date']
    data = [title,price,today]
    with open('AmazonScrapingLaptop.csv','a+',newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

#Run Function Daily to update dataset   
while(True):
    check_price()
    time.sleep(86400)