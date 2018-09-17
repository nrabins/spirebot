#!/usr/bin/python
import praw
import pdb
import re
import os
import logging
import json
import os
import logging.config

def setup_logging(
    default_path='logging.json',
    default_level=logging.INFO,
    evn_key='LOG_CFG'
):
    path = default_path
    value = os.getenv(evn_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

setup_logging()

logger = logging.getLogger("spirebot.py")

logger.info("Activating spirebot")
reddit = praw.Reddit('spirebot')

logger.debug("Checking posts_replied_to.txt")
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
    logger.debug("No posts_replied_to.txt found")
else:
    logger.debug("Loading history")
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
    logger.debug("History loaded")

subredditName = "robopuppycc"
subreddit = reddit.subreddit(subredditName)
logger.info("Scanning r/" + subredditName + " for new posts")
for submission in subreddit.hot(limit=10):
    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Spirebot says: Me too!!")
            logger.info("Replying to: %s", submission.title)
            posts_replied_to.append(submission.id)

logger.debug("Saving history")
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
logger.debug("History saved")

logger.info("Deactivating spirebot")