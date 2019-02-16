from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel #as p
from collections import OrderedDict

#1. download trang
url = "https://bobui.vn/shop"
#1.1 Open a connection to server
conn = urlopen(url)
#1.2 Read data
raw_data = conn.read()
#1.3 Decode data
page_content = raw_data.decode("utf8")

# print(page_content)

# f = open("dantri.html", "wb")
# f.write(raw_data)
# f.close()



#2. Extract ROI (Region of Interest)
soup = BeautifulSoup(page_content, "html.parser")
div = soup.find("div", "row main-content-wrap")
div2 = div.find("div", "main-content col-lg-12")
div3 = div2.find("div", id="primary")
main = div3.find("main", id="main")
div4 = main.find("div", "archive-products")
li_list = div4.find_all("li")
data = []
for i in li_list:
    div1 = i.find("div", "product-inner")
    div2 = div1.find("div", "product-image")
    div3 = div2.find("div", "after-loading-success-message")
    div4 = div3.find("div", "loader success-message-container")
    div5 = div4.find("div", "msg-box")
    title = div5.p.string
    img = div5.img['src']
    clothes = OrderedDict({ 
        "Title": title,
        "Image": img,
    })
    data.append(clothes)

pyexcel.save_as(records=data, dest_file_name="data_bobui.xlsx")










# #4. Save data to excel
# pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")

