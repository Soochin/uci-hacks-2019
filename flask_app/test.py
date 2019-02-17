import praw
import wget
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
while True:
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=10):
        url_text = submission.url
        has_domain = any(string in url_text for string in checkWords)
        print('[LOG Getting url:    ' + url_text)
        is_gifcat = any(string in url_text for string in gyfwords)
        if submission.id not in already_done and has_domain:
            if is_gifcat:
                url = re.sub('http://.*gfycat.com/', '', url_text)
                url_text = 'http://giant.gfycat.com/' + url + '.gif'
            wget.download(url_text, '/Users/emily/Desktop/test' + str(time.time())[-8:-3] + url_text[-4:])
            already_done.append(submission.id)
            print('[LOG] Done Getting ' + url_text)
exit()


