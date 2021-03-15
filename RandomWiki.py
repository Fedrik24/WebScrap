import random
import sys
import bs4
import requests
from os import system, name
import time


class Topic:
    def __init__(self):
        print("1.Art and culture\n2.Geography and places\n3.Health and fitness\n4.History and events\n5.Mathematics and abstractions\n6.Natural sciences and nature\n7.People and self\n8.Philosophy and thinking\n9.Religion and spirituality\n10.Social sciences and society\n11.Technology and applied sciences")

    def GenTop(self):
        self.search = input("Enter Number : ")
        if self.search == '1':
            ArtCulture()
            
        else:
            print('Bye')
            sys.exit()
    
    def Clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

class ArtCulture:
    def __init__(self):
        print("1.Culture\n2.Art and Entertainment\n3.Performing arts\n4.Visual arts")
        user = input('> ')
        if user == '1':
            self.Culture()
        else:
            None
    def Culture(self):
        lst = ["Classical studies","Cooking","Critical theory","Hobbies","Literature"] 
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        scrap_url = base.format(content)
        res = requests.get(scrap_url)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        wiki = soup.select('div p')
        judul = soup.select('.firstHeading')
        
        while True:
            for title in judul:
                print(title.text)
                for info in wiki:
                    print(info.text)
            time.sleep(3600)
            
        
        



if __name__ == '__main__':
    Top = Topic()
    Top.GenTop()