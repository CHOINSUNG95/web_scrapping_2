import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

url1 = "https://news.naver.com/section/105"
url2 = "https://news.naver.com/section/104"
response1 = requests.get(url1) #url에 get 요청 보냄
response2 = requests.get(url2)
#print(response) #200이면 요청 성공을 의미
#print(respnose.text) #HTML 소스 출력

html1 = response1.text 
html2 = response2.text 


#Beautifulsoup 객체 생성
soup1 = BeautifulSoup(html1, 'html.parser')
soup2 = BeautifulSoup(html2, 'html.parser')

#헤드라인 뉴스 기사 담을 리스트 객체 생성
headline_news_title1 = []
headline_news_title2 = []
#헤드라인 뉴스 기사 html 검색 
headline_news_el1 = soup1.select('.section_article.as_headline .sa_text_strong')
#print(headline_news_el1)
headline_news_el2 = soup2.select('.section_article.as_headline .sa_text_strong')
#print(headline_news_el2)

for title in headline_news_el1:
    title_text1 = title.get_text()
    headline_news_title1.append(title_text1)

for title in headline_news_el2:
    title_text2 = title.get_text()
    headline_news_title2.append(title_text2)
#print(headline_news_title1)
#print(headline_news_title2)

data1 = {"네이버 헤드라인 IT 뉴스 제목":headline_news_title1}
data2 = {"네이버 헤드라인 세계 뉴스 제목":headline_news_title2}

print(data1)
print(data2)

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

save_path = 'C:\work\python_projects\뉴스_기사_2.xlsx'
with pd.ExcelWriter(save_path) as writer:
    df1.to_excel(writer, sheet_name="IT", index=False)
    df2.to_excel(writer, sheet_name="세계", index=False)
print(f"{save_path}로 엑셀 파일이 저장되었습니다")