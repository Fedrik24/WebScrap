import bs4
import requests

base = 'https://en.savefrom.net/18/#url={}'
user = input("Paste youtube Link here : ")

while user not in ['q','quit']:
    scrape = base.format(user)

    link = requests.get(scrape)

    soup = bs4.BeautifulSoup(link.text, 'lxml')

    yt = soup.select('video')

    for li in yt:
        print(li.text)
        for a in soup.find_all('a', href=True):
            print('URL to Download : ' , a['href'])
    break
