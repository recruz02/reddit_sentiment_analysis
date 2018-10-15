# reddit_comment_contextualizer
Purpose of this project is to be able to identify sentiment against Reddit comments. Later on to apply intelligence and analytics against Reddit subreddits, users, and comments to find patterns and insights

# TODO List:

- Get most active subreddits
- Get most popular submissions (per subreddit, per day?)
- Get most popular comments
  - Parse popular comments for context
- Get most active users
- Get "Top X submissions"?
- Get "Top x comments"?
- Get "Top x subreddits"?

# Other Sample Projects

Twitter Sentiment Analysis Example:
https://github.com/aeryes/twitter_sentiment_lstm

Twitter Sentiment Analysis Example 2:
www.wayscript.com


# Data Structure

RDBMS or NoSQL DB?

comments table or JSON Document: 
- subreddit
- submission id
- submission name
- username
- comment
- date of comment
- number of upvotes

# Prerequisites

- Python 3.6+
- Python Library - PRAW

# External Links / References

PRAW Documentation - Comments (https://praw.readthedocs.io/en/latest/tutorials/comments.html)
