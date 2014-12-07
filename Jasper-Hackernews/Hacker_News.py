import re
from hn import HN

hn = HN()
def topStories():
    # print the first 10 of newest stories
    for story in hn.get_stories(limit=10):
        print (story.title);
        return(story.rank, story.title)
         

 

WORDS=["STORIES","FROM","HACKERNEWS"]
def isValid(text):
    return bool(re.search(r'\bstories from hackernews\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    stories=topStories();
    print (stories);
    mic.say(stories);
    
    
