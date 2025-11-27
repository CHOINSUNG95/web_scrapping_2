# requests: 웹 페이지의 HTML을 requests로 가져온다.
# Beautifulsoup: 우리가 처리하기 쉽도록 가져온 HTML 문서를 파싱한다

import requests
from bs4 import BeautifulSoup
import pandas as pd

# google robots.txt: 웹 사이트에서 허용하지 않는 규칙 

url = "https://news.kbs.co.kr/news/pc/view/view.do?ncd=8419292"
html_doc = requests.get(url).text
# print(html_doc)

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup)

#기사 제목 가져오기 
title1 = soup.find('h4', class_ = 'headline-title')
print(title1.text)

#기사 본문 가져오기 
body1 = soup.find('div', class_ = 'detail-body font-size')
print(body1.text)

#딕셔너리 데이터 구조에 원하는 데이터 담기 
data = {'뉴스 url':[url], '제목': [title1.text], '내용':[body1.text]}

#만든 데이터를 데이터프레임 구조로 만들어줌
df = pd.DataFrame(data)

#CSV 파일로 저장 
df.to_csv('news_KBS.csv', index=False) 