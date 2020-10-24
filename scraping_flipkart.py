from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, {"html.parser"})

containers = page_soup.findAll("div", {"class": "_1UoZlX"})
# print(len(containers))
# print(soup.prettify(containers[0]))
container = containers[0]
# print(container.div.img["alt"])
price = container.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
# print(price[0].text)
rating = container.findAll("div", {"class": "hGSR34"})
# print(rating[0].text)
filename = "products.csv"
f = open(filename, "w")

headers = "Products_Name,Pricing,Rattings\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    price_container = container.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "hGSR34"})
    rating = rating_container[0].text

    # print("Product Name:"+ product_name)
    # print("Product Price:"+ price)
    # print("Product Rating:"+ rating)
    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price = "Rs " + rm_rupee[1]

    print(product_name.replace(",", " |") + "," + add_rs_price + "," + rating + "\n")
    f.write(product_name.replace(",", " |") + "," + add_rs_price + "," + rating + "\n")

f.close()
