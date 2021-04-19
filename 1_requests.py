import requests

res = requests.get('http://google.com')

print(f'응답코드{res.status_code}가 {requests.codes.ok}와 일치하면 정상')  # 정상은 200

res.raise_for_status()  # 응답 코드가 200으로 정상이면 통과 아니면 에러 발생
print('웹 스크래핑을 진행합니다.')

# print(len(res.text))
# print(res.text)

with open('mygoogle.html', 'w', encoding='utf8') as f:
    f.write(res.text)
