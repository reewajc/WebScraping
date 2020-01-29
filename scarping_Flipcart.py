from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uclient = uReq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html, 'html.parser')

containers = page_soup.find_all('div', {'class':'bhgxx2 col-12-12'})

container = containers[0]
print(container.div.img['alt'])
