import requests
import bs4
import re
import random

base = 'https://id.wikihow.com/wikiHowTo?search={}'
user = input('Search WikiHow : ')

while user not in ['q','Quit','quit']:

    scarpe = base.format(user)

    req = requests.get(scarpe)

    soup = bs4.BeautifulSoup(req.text,'lxml')

    wikihow = soup.select('.result_title')

    for li in wikihow:
        result = li.text
        result = re.sub('\s+', ' ', result)
        print(result)
    user = input('Search WikiHow : ')
