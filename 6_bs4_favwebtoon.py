import requests
from bs4 import BeautifulSoup

# 좋아하는 만화 링크
url = 'https://comic.naver.com/webtoon/list.nhn?titleId=748105&weekday=thu'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

# # 만화의 제목 + 링크 가져 오기
# cartoons = soup.find_all('td', attrs={'class': 'title'})
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = 'https://comic.naver.com' + cartoon.a['href']
#     print(title, link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all('div', attrs={'class': 'rating_type'})
for cartoon in cartoons:
    rate = cartoon.find('strong').get_text()
    total_rates += float(rate)
print(f'평점 {total_rates / len(cartoons)}')
