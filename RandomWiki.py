import random
import sys
import bs4
import requests
import time
import os
class WebScrap:
    def __init__(self): 
        global lst
        global content
        global base
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
                time.sleep(10)
            time.sleep(3600)        

class Topic:
    def __init__(self):
        print("1.Art and culture\n2.Geography and places\n3.Health and fitness\n4.History and events\n5.Mathematics and abstractions\n6.Natural sciences and nature\n7.People and self\n8.Philosophy and thinking\n9.Religion and spirituality\n10.Social sciences and society\n11.Technology and applied sciences")

    def GenTop(self):
        self.search = input("Enter Number : ")
        if self.search == '1':
            os.system('cls')
            ArtCulture()
        elif self.search == '2':
            os.system('cls')
            GeographyAndPlaces()
        elif self.search == '3':
            os.system('cls')
            HealthAndFitness()
        elif self.search == '4':
            os.system('cls')
            HistoryAndEvents()
        elif self.search == '5':
            os.system('cls')
            MathematicsAndAbstractions()
        elif self.search == '6':
            os.system('cls')
            NaturalSciencesAndNature()      
        elif self.search == '7':
            os.system('cls')
            PeopleAndSelf()
        elif self.search == '8':
            os.system('cls')
            PhilosophyAndThinking()
        elif self.search == '9':
            os.system('cls')
            #Religion()
            print('Not Yet!')
            self.GenTop()
        elif self.search == '10':
            os.system('cls')
            SocialSciencesAndSociety()
        elif self.search == '11':
            os.system('cls')
            TechnologyAndAppliedSciences()            
        else:
            print('Bye')
            sys.exit()

class ArtCulture(WebScrap):
    def __init__(self):
        print("1.Culture\n2.Art and Entertainment\n3.Performing arts\n4.Visual arts")
        user = input('> ')
        if user == '1':
            self.Culture()
        elif user == '2':
            self.ArtAndEntertainment()
        elif user == '3':
            self.PerformingArts()
        elif user == '4':
            self.VisualArts()
        else:
            None
    def Culture(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["Classical studies",
               "Cooking",
               "Critical theory",
               "Hobbies",
               "Literature"] 
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)

    def ArtAndEntertainment(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["Fiction",
               "Game",
               "Poetry",
               "Sports"] 
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)          
    
    def PerformingArts(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["Dance",
               "Film",
               "Music",
               "Opera",
               "Anime"] 
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)    
            
    def VisualArts(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):  
        global lst
        global content
        global base
        lst = ["Architecture",
               "Crafts",
               "Drawing",
               "Painting",
               "Photography",
               "Sculpture",
               "Typography"] 
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)       
        
class GeographyAndPlaces(WebScrap):
    def __init__(self):
        print('Not Yet! Come back later...')
        
class HealthAndFitness(WebScrap):
    def __init__(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["Health",
               "Exercise",
               "Health Science",
               "Nutritions"] 
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)   

class HistoryAndEvents(WebScrap):
    def __init__(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["History",
               "Classical antiquity",
               "Medieval history",
               "Renaissance"] 
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)    

class MathematicsAndAbstractions(WebScrap):
    def __init__(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["Mathematics",
               "Arithmetic",
               "Algebra",
               "Calculus",
               "Discrete mathematics",
               "Geometry",
               "Trigonometry",
               "Logic",
               "Statistics"] 
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)  

class NaturalSciencesAndNature(WebScrap):
    def __init__(self):
        print("1.Main List\n2.Biology\n3.Physical Science")
        user = input("> ")
        
        if user == '1':
            self.Main_list()
        elif user == '2':
            self.Biology()
        elif user == '3':
            self.Physical_science()
        else:
            sys.exit()

    def Main_list(self):
        print("AKAN DI IMPORT DARI SCRIPT LUAR/BIKIN!")
        NaturalSciencesAndNature()
        
    def Biology(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["Animals",
               "Biochemistry",
               "Botany",
               "Ecology",
               "Zoology"] 
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)   
    
    def Physical_science(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["Astronomy",
               "Chemistry",
               "Earth sciences",
               "Physics Fractions"] 
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)          

class PeopleAndSelf(WebScrap):
    def __init__(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["People",
               "Self",
               "Biology",
               "Psychology",
               "Relationships"]
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)  


class PhilosophyAndThinking(WebScrap):
    def __init__(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["Philosophy",
               "Philosophical theories",
               "Humanism",
               "Logic",
               "Thinking",
               "Transhumanism"]
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)  

class Religion(WebScrap):
    pass 

class SocialSciencesAndSociety(WebScrap):
    def __init__(self):
        pass
    
    def Social_sciences(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["Archaeology",
               "Critical theory",
               "Economics",
               "Geography",
               "History",
               "Linguistics",
               "Law",
               "Political science",
               "Psychology",
               "Sociology",
               "Relationships"]
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)  
    
    def Society(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["Community",
               "Criminal justice",
               "Education",
               "Firefighting",
               "Politics",
               "Public affairs"]
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)         

    def Business(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["Economics",
               "Finance",
               "Management",
               "Marketing"]
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)    

class TechnologyAndAppliedSciences(WebScrap):
    def __init__(self):
        user = input("> ")
        while user not in ['q','quit']:
            if user == '1':
                print('Not Yet!')
                print('Automaticly go to SubTopic 2')
                self.TechScience()
            elif user == '2':
                self.TechScience()
            else:
                print('Bye')
                sys.exit()
            
    
    def TechScience(self,scrap_url='https://en.wikipedia.org/wiki/{}',res='',soup='None',wiki='None'):
        global lst
        global content
        global base
        lst = ["Aerospace",
               "Artificial intelligence",
               "Agriculture",
               "Architecture",
               "Big Science",
               "Biotechnology","Communication",
               "Computer science",
               "Information technology",
               "Internet",
               "Programming",
               "Software engineering",
               "Energy development",
               "Engineering",
               "Firefighting",
               "Health science","Industry",
               "Library and information science",
               "Machines",
               "Management",
               "Manufacturing",
               "Military",
               "Nutrition","Permaculture",
               "Robotics","Space exploration",
               "Telecommunication",
               "Internet",
               "Transport",
               "Vehicles"]
        self.scrap_url = scrap_url
        self.res = res
        self.soup = soup
        self.wiki = wiki        
        content = random.choice(lst)
        base = "https://en.wikipedia.org/wiki/{}"
        WebScrap.__init__(self)          


if __name__ == '__main__':
    Top = Topic()
    Top.GenTop()