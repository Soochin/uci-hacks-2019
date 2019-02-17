from flask import Flask
app = Flask(__name__)
import prawdata

@app.route("/")
def hello():
    return "Hello World! You shouldn't be seeing this."


@app.route("/r/<subreddit>", methods=['GET'])
def get_subreddit_data(subreddit):
    """ Returns MAX_POSTS number of Title and
        Contents for a subreddit. """
    return prawdata.get_subreddit(subreddit)


@app.route("/p/<post_id>", methods=['GET'])
def get_post_data(post_id):
    """ Returns post data such as title and contents as
        JSONified format. """
    return prawdata.get_content(post_id)