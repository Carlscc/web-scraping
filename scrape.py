import requests
from bs4 import BeautifulSoup
import pprint

#create response variable and get request to grab the Hackernews URL (first checked robots.txt)
res = requests.get('https://news.ycombinator.com/')
#parse the data from a string to HTML
soup = BeautifulSoup(res.text, 'html.parser')
#create variables to select links and subtext of stories (subtext contains scores and exists even when there are no scores)
links = soup.select('.storylink')
subtext = soup.select('.subtext')

#list stories by votes starting with highest
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    # only enumerating over links, need the index to access the subtext
    for idx, item in enumerate(links):
        #get title and index of each link
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
        #get scores if 100 or over 
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title':title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))

