from selenium import webdriver
import re
from bs4 import BeautifulSoup

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    \.[a-zA-Z]{2,4}
    )''', re.VERBOSE)

browser = webdriver.Firefox()
urls = [# LINKS
        ]
file = open('emails.txt', 'a')

for url in urls:
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    res = re.findall(emailRegex, soup.text)
    file.write(", ".join(res))

file.close()
