from bs4 import BeautifulSoup
import requests
from db_helper import DbHelper
from bot_functions import BotFunctions


class BaseScraper:

    def __init__(self, url):
        self.db = DbHelper("FootballMatches")

        self.headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

        self.url = url

        self.match_list = {}

        self.connection = self.connection(self.url, self.headers)
        self.scrape_data(self.connection)

    
    def connection(self, url, headers) -> BeautifulSoup:
        r = requests.get(url, headers = headers)
        soup = BeautifulSoup(r.content,'html.parser')
        return soup


    def scrape_data(self, soup) -> None:
        self.match_list = {}
        response = requests.get(self.url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')


            # First for loop
            counter = 0
            for j in soup.find_all("div", {"class":"SimpleMatchCard_simpleMatchCard__matchContent__prwTf"}):
                counter += 1
                if len(j.text) == 5:
                    self.match_list["time"] = j.text


                    # Second for loop
                    second_counter = 0
                    team = 0
                    for x in soup.find_all("div", {"class":"SimpleMatchCard_simpleMatchCard__teamContent__hQHVO SimpleMatchCardTeam_simpleMatchCardTeam___GPYH"}):
                        second_counter += 1
                        if second_counter == (counter*2)-1 or second_counter == counter*2:
                            team += 1
                            takim_string = "team" + str(team)
                            self.match_list[takim_string] = x.text
                        else:
                            pass


                        for a in soup.find("p", {"class":"title-1-bold"}):
                            self.match_list["league"] = a
                    
                    # Save to db
                    self.db.add_single_data(self.match_list, "MatchCards")
                    self.match_list.clear()
                    


                else:
                    pass


        else:
            print(f"Error: {response.status_code}")