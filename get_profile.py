import os
import re
import csv
import sys
import json
import time
import errno
import random
import urllib
import logging
import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


#driver = webdriver.Chrome('./cdriver/chromedriver.exe')
#
#driver.get("https://www.wg-gesucht.de/en/")
#
#
#
#print(driver.title)

session = requests.Session()


payload = {
            "login_email_username": "debayan.sen1994@gmail.com",
            "login_password": "wggesucht@neil94",
            "login_form_auto_login": "1",
            "display_language": "de"
        }


headers = { 'Accept': 'application/json',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9,de;q=0.8',
'Connection': 'keep-alive',
'Content-Length': '140',
'Content-Type': 'application/json',
'Host': 'www.wg-gesucht.de',
'Origin': 'https://www.wg-gesucht.de',
'Referer': 'https://www.wg-gesucht.de/en/logout.html',
'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
'X-Authorization': 'Bearer',
'X-Client-Id': 'wg_desktop_website',
'X-Dev-Ref-No': '',
'X-Requested-With': 'XMLHttpRequest',
'X-User-Id':'' }


response = session.post(
                "https://www.wg-gesucht.de/ajax/sessions.php?action=login",
                data=json.dumps(payload), headers=headers
            )

print("login status",response.json)
response=session.get("https://www.wg-gesucht.de/en/my-profile.html")
with open('index.html','w') as f:
	f.write(response.text)
