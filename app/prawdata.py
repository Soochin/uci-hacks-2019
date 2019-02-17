import praw

from prawcore import NotFound

MAX_POSTS = 25

reddit = praw.Reddit(client_id = "BuHNPoZ-G1q9QQ",
                     client_secret = "-Da1eZwtF5bizD6QivESFiqCa2w",
                     user_agent = "Traditional_Bridge_")


def subreddit_exists(subreddit):
    exists = True
    try:
        reddit.subreddits.search_by_name(subreddit, exact=True)
    except NotFound:
        exists = False
    return exists

def get_subreddit(subreddit):
    if not subreddit_exists(subreddit):
        return {}

    subreddit = reddit.subreddit(subreddit)

    submissions = {"submissions":list()}

    for submission in subreddit.hot(limit=MAX_POSTS):
        submission_info = {"title": submission.title, "link": submission.shortlink, "id": submission.id}
        submissions["submissions"].append(submission_info)

    return submissions

def get_subreddit_titles(subreddit):
    if not subreddit_exists(subreddit):
        return {}

    subreddit = reddit.subreddit(subreddit)

    titles = list()

    for submission in subreddit.hot(limit=MAX_POSTS):
        titles.append(submission.title)

    return titles

def get_content(post_id):
    post = reddit.submission(id=post_id)
    contents = dict()
    contents['title'] = post.title
    contents['selftext'] = post.selftext

    return contents