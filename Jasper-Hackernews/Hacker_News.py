import re
from hn import HN

hn = HN()
         

WORDS = ["STORIES","FROM","HACKERNEWS"];

def isValid(text):
    return bool(re.search(r'\bstories from hackernews\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    mic.say("Hi.The top 10 stories are as follows: ");
    for story in hn.get_stories(limit=10):
        s_title = story.title;
        s_rank=story.rank;
        mic.say(s_rank + " " + s_title );
        return 1;
    
    
    
