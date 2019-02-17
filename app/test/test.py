import praw
import time
import json
import re

sub = "dogpictures"
reddit = praw.Reddit(client_id = "BuHNPoZ-G1q9QQ",
                     client_secret = "-Da1eZwtF5bizD6QivESFiqCa2w",
                     user_agent = "Traditional_Bridge_")
already_done = []
checkWords = ['i.imgur.com',  'jpg', 'png', 'gif', 'gfycat.com', 'webm',]
gyfwords = ['gfycat.com']

subreddit = reddit.subreddit(sub)
url_list = list()
for submission in subreddit.hot(limit=10):
    url_text = submission.url
    has_domain = any(string in url_text for string in checkWords)
    print('[LOG Getting url:    ' + url_text)
    is_gifcat = any(string in url_text for string in gyfwords)
    if submission.id not in already_done and has_domain:
        if is_gifcat:
            url = re.sub('http://.*gfycat.com/', '', url_text)
            url_text = 'http://giant.gfycat.com/' + url + '.gif'
        already_done.append(submission.id)
        url_list.append(url_text)
        print('[LOG] Done Getting ' + url_text)

print(url_list)