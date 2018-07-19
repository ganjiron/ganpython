# 1. 파이썬 Web Scraping
# 웹사이트에서 HTML을 읽어와 필요한 데이타를 긁어오는 것을 Web Scraping이라 한다. 이 과정은 크게 웹페이지를 읽어오는 과정과 읽어온 HTML 문서에서 필요한 데이타를 뽑아내는 과정으로 나뉠 수 있다.
#
# 웹페이지를 읽어오는 일은 여러 모듈을 사용할 수 있는데, 파이썬에서 기본적으로 제공하는 urllib, urllib2 을 사용하거나 편리한 HTTP 라이브러리로 많이 쓰이고 있는 requests 를 설치해 사용할 수 있다.
#  만약 기존 코드를 유지보수하는 일이 아니라면 requests 를 사용할 것을 권장한다.
#
# 2. requests - 웹페이지 읽어오기
# HTTP 라이브러리인 requests를 사용하기 위해서는 먼저 아래와 같이 pip을 이용하여 requests 패키지를 설치한다.
#
# pip install requests
# 기본적인 requests 기능을 먼저 살펴보면, requests는 HTTP GET, POST, PUT, DELETE 등을 사용할 수 있으며, 편리한 데이타 인코딩 기능을 제공하고 있다.
# 즉, 데이타를 Dictionary로 만들어 GET, POST 등에서 사용하면 필요한 Request 인코딩을 자동으로 처리해 준다.
import requests, bs4

resp = requests.get('http://finance.naver.com/')
resp.raise_for_status()

resp.encoding = 'euc-kr'
html = resp.text

bs = bs4.BeautifulSoup(html, 'html.parser')
tags = bs.select('div.news_area h2 a')  # Top 뉴스
title = tags[0].getText()
print(title)

# requests.get(url) 함수를 사용하면 해당 웹페이지 호출 결과를 가진 Response 객체를 리턴한다.
# Response 객체는 HTML Response와 관련된 여러 attribute들을 가지고 있는데, 예를 들어, Response의 status_code 속성을 체크하여 HTTP Status 결과를 체크할 수 있고,
# Response 에서 리턴된 데이타를 문자열로 리턴하는 text 속성이 있으며, Response 데이타를 바이트(bytes)로 리턴하는 content 속성 등이 있다.
# 또한, 만약 Response에서 에러가 있을 경우 프로그램을 중단하도록 할 때는 Response 객체의 raise_for_status() 메서드를 호출할 수 있다.
# 아래 예제는 다음 홈페이지에 접속해서 HTML 문서를 가져와 화면에 출력하는 예이다.
# GET
resp = requests.get('http://httpbin.org/get')
print(resp.text)

# 아래 예제는 네이버 증권사이트에서 주요 Top 뉴스 제목을 발췌하는 코드이다.
# POST
dic = {"id": 1, "name": "Kim", "age": 10}
resp = requests.post('http://httpbin.org/post', data=dic)
print(resp.text)

resp = requests.put('http://httpbin.org/put')
resp = requests.delete('http://httpbin.org/delete')

resp = requests.get('http://daum.net')
# resp.raise_for_status()

if (resp.status_code == requests.codes.ok):
    html = resp.text
    print(html)