
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

url = 'https://www.aihuishou.com/Home/RenderCategoryItem?categoryId=1&brandid=9'
url1 = 'https://www.aihuishou.com/shouji/b4'
r = requests.get(url=url1, headers=headers)
html_response = r.text
soup = BeautifulSoup(html_response,'lxml')
list_box = soup.find_all('div', class_="list-box")
# print(list_box[1])
phone_urls = list_box[1].find_all('a') # 获取到所有手机种类的url

# p_m = phone_urls[0]['href']
prefix_url = 'https://www.aihuishou.com'
p_urls = []
for p_url in phone_urls:
    url = prefix_url+p_url['href']
    p_urls.append(url)

print(p_urls)