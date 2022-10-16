import requests
from bs4 import BeautifulSoup
import pandas as pd

#获取html网页,设置headers，并进行目标网址的请求
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
params = (('limit', '50'),('reverse_order', '0'),)
url = 'https://www.zhihu.com/billboard'
#请求超时时间为30秒
r = requests.get(url,timeout = 30,headers=headers,params=params)
html = requests.get(url, headers = headers)

#标题
r.text
html=r.text
soup=BeautifulSoup(html,'html.parser')
titles = soup.select('.HotList-itemTitle')
#排名
ranks = soup.select('.HotList-itemPre')
for rank in ranks:
    print(rank.text)
#热度
heats = soup.select('.HotList-itemMetrics')
#保存数据，生成xlsx文件
num=50
dts = []
for i in range(num):
    lst = []
    lst.append(ranks[i].text)
    lst.append(titles[i].text)
    lst.append(heats[i].text.replace('万热度','0000'))
    dts.append(lst)
df = pd.DataFrame(dts, columns=['排名','标题', '热度',])
df.to_excel(r'zhihu.xlsx')