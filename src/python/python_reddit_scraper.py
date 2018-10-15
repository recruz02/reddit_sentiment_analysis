# pip install praw
# PRAW = Python Reddit API Wrapper

import praw

reddit = praw.Reddit(client_id = 'b8kqWqAX_81cNw',client_secret = '2GAyckRha25fh8E-Xe6Xb6vqjjg', username = '',password = '',user_agent = 'recruz.python_praw_test')

					 
print(reddit.read_only)  # Output: True

					 
					 
subreddit = reddit.subreddit('Chargers')



chargers_new = subreddit.new(limit = 10)

for submission in chargers_new:
	print(submission.title)
	print(submission.ups) 