from hn import HN

hn = HN()

def topStories():
    # print the first 10 of newest stories
    for story in hn.get_stories(limit=10):
        print(story.rank, story.title)
        print ('submitter: '+story.submitter)
        print ('comments:' , story.num_comments)
        print ('points:' , story.points)

def latestStories():
    # print the first 10 of latest stories
    for story in hn.get_stories(story_type='newest',limit=10):
        print(story.rank, story.title)
        print ('submitter: '+story.submitter)
        print ('comments:' , story.num_comments)
        print ('points:' , story.points)



topStories();
latestStories();
