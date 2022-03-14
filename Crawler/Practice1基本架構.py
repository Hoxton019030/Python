import requests
res = requests.get("https://s.taobao.com/search?q=多樣屋+葫蘆+保溫杯&type=p&tmhkh5=&from=sea_1_searchbutton&catId=100&spm"
                   "=a2141.241046-tw.searchbar.d_2_searchbox");
print(res.text)
