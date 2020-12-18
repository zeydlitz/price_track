import requests
from bs4 import BeautifulSoup
import smtplib
import time
import re

frommail = 'maksimka.ivashkevich27@gmail.com'
passwd = 'tuudleiomxrxdysw'
tomail = 'lepunir@protonmail.com'

URL = ['https://by.wildberries.ru/catalog/10504392/detail.aspx?targetUrl=ES',
       'https://by.wildberries.ru/catalog/5948830/detail.aspx?targetUrl=ES',
       'https://by.wildberries.ru/catalog/13292664/detail.aspx?targetUrl=ES']


def analyze_price(URL):
    app = requests.get(URL)
    scrapper = BeautifulSoup(app.content, 'html.parser')
    title = scrapper.find(class_="name").get_text()
    price = scrapper.find(class_="final-cost").get_text()
    price = re.findall("\d{3}", price)[0]
    send_notification(price,title)


def send_notification(price,name):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(frommail, passwd)

    msg = 'Subject: {}\n\n{}'.format(name,price).encode('utf-8')

    server.sendmail(frommail, tomail, msg)
    print('Notification has been sent successfully')

    server.quit()


if __name__ == '__main__':
    analyze_price(URL[0])
    analyze_price(URL[1])
    analyze_price(URL[2])
