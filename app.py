from bs4 import BeautifulSoup
import requests
import random


class UserAgent:
    user_agents = []

    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            for line in f.readlines():
                self.user_agents.append(line.replace('\n', ''))

            for agent in self.user_agents:
                if len(agent) == 1:
                    print("Empty")
                    #TODO remove emptyline if exists

    def get(self):
        return {'user-agent': random.choice(self.user_agents)}



user_agent = UserAgent("user-agents.txt")
parsing_url = "https://www.facebook.com/bizwithbasanta"
result_set = []

def getPageInfo(url, time_out):
    response = requests.get(url, headers=user_agent.get(), timeout=time_out)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        
        anchor_tags = soup.find_all('a')
        # anchor_tags = soup.find_all("div", {"class": "textContent"})
        print(len(anchor_tags))


getPageInfo(parsing_url, 3)

    
