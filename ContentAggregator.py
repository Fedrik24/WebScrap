import requests
import bs4

base = 'https://alltop.com/{}/'

print("Welcome to content aggregator!")
print("\nAll of this content was from alltop.com!\n")
print("Type tech/news/viral ! ")
print("\nType q/quit/Quit to exit program!\n")

user = "NULL"

while user not in ['q','quit','Quit']:
    user = input("Search Content : ")
    if user == 'tech':
        scrape = base.format(user)

        req = requests.get(scrape)

        soup = bs4.BeautifulSoup(req.text,'lxml')

        content = soup.select('.one-line-ellipsis')

        for konten in content:
            print(konten.text)
            print("\n")
        continue

    elif user == 'news':

        scrape = base.format(user)

        req = requests.get(scrape)

        soup = bs4.BeautifulSoup(req.text,'lxml')

        content = soup.select('.one-line-ellipsis')

        for konten in content:
            print(konten.text)
            print("\n")
        continue


    elif user == 'viral':

        scrape = base.format(user)

        req = requests.get(scrape)

        soup = bs4.BeautifulSoup(req.text,'lxml')

        content = soup.select('.post-title')

        for konten in content:
            print(konten.text)
            print("\n")
        continue

    else:
        print("GOOD BYE~ Thankyou for using this :3 ")
