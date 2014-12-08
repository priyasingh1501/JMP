"""
This module demonstrates the HackerNews module that will be used by jasper
to provide a voice output to a particular voice input.It provides the current
top 10 stories as the output whenever it gets an input that contains the following
words-Stories,from,hackernews.

Example:

Audio Input:
Jasper. Give me the top 10 stories from hackernews.

Audio Output:
Your top 10 stories are ---

Attributes and functions:
HN is a class in the HackerNews API that includes all the
functions that are working in the program.hn is an object of the class HN that
is used to call the functions of HN.
"""

import re
from hn import HN


hn = HN()         

WORDS = ["STORIES","FROM","HACKERNEWS"];

def isValid(text):
    return bool(re.search(r'\bstories from hackernews\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    mic.say("Your top 10 stories are ");
    for story in hn.get_stories(limit=10):
        s_title = story.title;
        s_rank=story.rank;
        mic.say(s_rank + " " + s_title );
return "1";
    
    
    
