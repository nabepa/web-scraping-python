import requests

# 403 에러란?
# 웹사이트는 사용자 정보인 header 정보를 받음
# 근데 만약 사람이 접속하는 것이 아니라고 판단되면, 웹사이트의 부하 방지, 보안 등의 이유로 차단

#   403 에러를 피하는 방법
# requests.get할 때 user agent string을 제공
# user agent string은 https://www.whatismybrowser.com/detect/what-is-my-user-agent서 확인 가능

url = 'http://nadocoding.tistory.com'
headers = {
    'User-Agent': 'Mozilla/(이하생략)'  # 확인 해서 붙이기
}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open('nadocoding.html', 'w', encoding='utf8') as f:
    f.write(res.text)
