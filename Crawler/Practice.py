import lxml
import requests
from bs4 import BeautifulSoup

res = requests.get("https://tw.stock.yahoo.com/")
soup = BeautifulSoup(res.text,"html.parser")


for item in soup.select('.Jc(fe) Fw(600) D(f) Ai(c) C($c-trend-up)'):
    print(item);





