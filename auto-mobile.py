import time
import requests
from bs4 import BeautifulSoup


headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}  # 爬虫[Requests设置请求头Headers],伪造浏览器

url= 'https://www.dpac.org.cn/qczh/qczhgg1/201907/t20190719_84998.html'
# params = {"show_ram":1}
response = requests.get(url, headers=headers)  # 访问url
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')  # 获取网页源代码
tr = soup.find('table').find_all('tr')  # .find定位到所需数据位置  .find_all查找所有的tr（表格）
# 去除标签栏
for j in tr:        # tr2[1:]遍历第1列到最后一列，表头为第0列
    td = j.find_all('td')  # td表格
    for elem in td:
        print(td.index(elem))
        print(elem.get_text().strip())
