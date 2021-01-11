import requests
import bs4

base = 'https://en.wikipedia.org/wiki/{}'
print("Type anything that you wanna search on Wikipedia \nType q/quit to exit the program")
user = input('Search Wikipedia : ')

while user not in ['q','Quit','quit']:
    scrape_url = base.format(user)

    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text,'lxml')

    wiki = soup.select('div p')

    for info in wiki:
        print(info.text)
    user = input('Search Wikipedia : ')
