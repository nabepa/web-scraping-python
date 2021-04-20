# 개요
유튜버 '나도코딩'님의 웹 스크래핑 강의 실습
</br>
[https://www.youtube.com/watch?v=yQ20jZwDjTE&list=PLMsa_0kAjjrd8hYYCwbAuDsXZmHpqHvlV&index=7](https://www.youtube.com/watch?v=yQ20jZwDjTE&list=PLMsa_0kAjjrd8hYYCwbAuDsXZmHpqHvlV&index=7)


## Web Crawling VS Web Scraping
- Web Crawling: 웹페이지 내에서 허용된 링크를 따라 가며 데이터를 마구잡이로 가져오는 것
- Web Scraping: 웹페이지 내에서 필요한 부분의 데이터만 가져오는 것


## 설치 패키지
```bash
$ pip install requests
$ pip install beautifulsoup4
$ pip install lxml
```

## 파일 설명
- 1_requests.py: requests 패키지 기본 사용법
- 2_re.py: 정규 분포 패키지 re 사용법
- 3_user_agent.py: 403 에러 회피 feat.헤더에 user agent string 설정하기
- 4_bs4.py: BeautifulSoup4 기본 사용법
- 5_bs4_webtoons.py: BeautifulSoup4을 이용해서 네이버 웬툰의 모든 제목 가져오기
- 6_bs4_favwebtoon.py: BeautifulSoup4을 이용해서 가장 좋아하는 웬툰의 최신 10화의 제목, 링크 가져오고, 평균 평점 구하기