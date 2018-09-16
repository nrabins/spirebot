#!/usr/bin/python
import praw

reddit = praw.Reddit('spirebot')

subreddit = reddit.subreddit("robopuppycc")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")