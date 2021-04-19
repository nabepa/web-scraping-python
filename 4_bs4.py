import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/index.nhn'
res = requests.get(url)
res.raise_for_status()

# 가져온 html 문서를 lxml을 통해서 bs 개체로 만들기
soup = BeautifulSoup(res.text, 'lxml')

# 웹의 구조를 잘 알 때
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)  # soup 개체에서 처음 발견되는 a 요소를 출력
# print(soup.a.attrs) # a 요소의 속성 정보를 출력
# print(soup.a['href']) # a 요소의 href 속성 '값' 정보를 출력

# 웹의 구조를 잘 모를 때
# class='Nbtn_upload'인 첫 요소 출력
# print(soup.find(attrs={'class': 'Nbtn_upload'}))
# class='Nbtn_upload'이고 a 태그인 첫 요소 출력
# print(soup.find('a', attrs={'class': 'Nbtn_upload'}))

# 요소의 부모, 자식, 형제 찾기
rank1 = soup.find('li', attrs={'class': 'rank01'})
print(rank1.a.get_text())
# rank1의 다음 형제 찾기 위해 next_sibling, 하지만 공백이 들어가 있음
print(rank1.next_sibling)
# 다행히 next_sibling을 두번 하면 원하는 다음 순위의 요소에 접근 가능
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
# 이전 형제를 찾기 위해 previous_sibling
reank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())
print(rank1.parent)
# 위와 같이 next_sibling 이나 previous_sibling을 몇 번이고 반복하는 것은 좋지 못함
# 아래와 같이 특정 형제를 찾을 수 있음
rank2 = rank1.find_next_sibling('li')
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling('li')
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling('li')
print(rank2.a.get_text())
# 특정 조건에 부합하는 모든 형제 요소
print(rank1.find_next_siblings('li'))

# 태크의 콘텐츠를 통한 검색도 가능
webtoon = soup.find('a', text='여신강림-153화')
print(webtoon)
