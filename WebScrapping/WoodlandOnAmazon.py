import requests ##Using this we can access the website url and we can pull out the data from the webpage
from bs4 import BeautifulSoup  ##This can help us to parse it and pull out the individual items from it
import re

##from selenium import webdriver as wd

def main():
    URL = 'https://www.amazon.in/Woodland-Olive-Sneakers-8-GC-2336116/dp/B07CWMQ6ST/ref=mp_s_a_1_4?keywords=woodland+shoes&qid=1564581992&s=gateway&sr=8-4'

    """
    You can get the user agent by simple google search of: "my user agent" 
    """
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())

    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()

    print(title)
    print(price)
    maxPrice = float(extractMaximumPrice(price))
    print(maxPrice)

    expected_price = float(3000)

    if(maxPrice <= expected_price):
        email_to = ''
        email_from = ''
        email_subject = ''
        email_body = ''
        sendEmail()

def sendEmail():
    print()

def extractMaximumPrice(valFromWebpage):
    if(re.search(" - ", valFromWebpage)):
        reg = " - ₹ "
        maxPrice = re.sub(",", "", valFromWebpage[(valFromWebpage.find(reg) + len(reg)) : len(valFromWebpage) ] )
        #print("maxPrice: ", maxPrice)
        return maxPrice
    else:
        reg = "₹ "
        maxPrice = re.sub(",", "", valFromWebpage[(valFromWebpage.find(reg) + len(reg)) : len(valFromWebpage) ] )
        #print("maxPrice: ", maxPrice)
        return maxPrice


if(__name__=="__main__"):
    main()
