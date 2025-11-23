import requests

url = "https://www.naver.com/"
response=requests.get(url)

#print(response): resposne 200이면 html get 요청 성공 
#print(response.text) #html 소스 출력