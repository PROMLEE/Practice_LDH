from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://sports.news.naver.com/wfootball/schedule/index'
driver = webdriver.Chrome("C:\\webdriver\\chromedriver.exe")
driver.get(url)
time.sleep(1)

news_titles = driver.find_elements_by_css_selector("tr")
data = []
n = 0
for i in news_titles:
    title_ee = i.text
    title = title_ee.split('\n')
    title.append("\n")
    # if(title == "FT" or title == "문자중계" or title == "경기가 없습니다." or title == "날짜 시간 장소 경기 중계 경기내용"):
    #     data[n].append("\n")
    #     n += 1
    #     data.append([])
    # elif(title == "경기기록" or title == "경기기록 경기영상" or title == "전력비교" or title == "승리팀"):
    #     continue
    # else:
    data.append(title)
print(data)
f = open("2월.txt", 'w')
for i in data:
    f.writelines(",".join(i))
f.close()
