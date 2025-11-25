import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

url = "https://news.naver.com/section/105"
response = requests.get(url) #url에 get 요청 보냄

#print(response) #200이면 요청 성공을 의미
#print(respnose.text) #HTML 소스 출력

html = response.text 

#Beautifulsoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

#헤드라인 뉴스 기사 담을 리스트 객체 생성
headline_news_title = []
#헤드라인 뉴스 기사 html 검색 
headline_news_el = soup.select('.section_article.as_headline .sa_text_strong')

#반복문 이용하여 헤드라인 뉴스기사 타이틀 뽑아냄 
#타이틀의 text만 추출하여 headline_news_title 리스트에 저장 
for title in headline_news_el:
    title_text = title.get_text()
    headline_news_title.append(title_text)

data = {"네이버 헤드라인 IT 뉴스 제목":headline_news_title}

print(data)
#헤드라인 뉴스 제목을 엑셀에 저장
df = pd.DataFrame(data)
save_path = 'C:\work\python_projects\뉴스_기사_2.xlsx'
#엑셀 파일로 저장 
#df.to_excel(save_path, index=False, engine='openpyxl')
#print(f"{save_path}로 엑셀 파일이 저장되었습니다") 
