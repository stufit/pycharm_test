#selenium
from selenium import webdriver
import time
import socket
from webdriver_manager.chrome import ChromeDriverManager
#drive = webdriver.chrome(ChromeDriverManager().install())
drive = webdriver.Chrome('/Users/gaegul/PycharmProjects/pythonProject/venv/chromedriver-mac')
drive.get("https://pypi.org/")

menus = drive.find_elements_by_css_selector('#top ui.menu li')

pypl = None
for m in menus:
    if m.text == 'pypl':
        pypl = m
    print(m.text)

pypl.click()

time.sleep(5) #5초동안 대기
drive.quit()  #브라우저 종료


