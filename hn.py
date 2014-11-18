#!/usr/bin/env python

from hn import HN, Story
class stories:
    hn = HN();

    top_iter = hn.get_stories(limit=10) 

    # print top stories from homepage
    for story in top_iter:
        print(story.title.encode('utf-8'))
    print('*' * 50)

    # print 10 latest stories
    for story in hn.get_stories(story_type='newest', limit=5):
         print(story.title.encode('utf-8'))
     
     

 
