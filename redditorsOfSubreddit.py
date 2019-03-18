import praw
import json

reddit = praw.Reddit(client_id='IFHDQg4dnEQ2AA', \
                     client_secret='bVZAdZRh6XPPn6G0R-kChVsoEMo', \
                     user_agent='tangocharlie1', \
                     username='isauadh', \
                     password='s@ugaT1320')

def Subreddit(name, limitTo):
  subreddit = reddit.subreddit(name)
  submissions = subreddit.top(limit = limitTo)
  redditors = {}
  redditors['redditors'] = []
 
  for submission in submissions:
    submission.comments.replace_more(limit= None)
    redditors['redditors'].append(str(submission.author))
    for comment in submission.comments.list():
      redditors['redditors'].append(str(comment.author))
  redditors['redditors'] = list(set(redditors['redditors']))
  writeData("{}.txt".format('Redditor'),redditors)
  
def writeData(fp, data):
    outputfp = open(fp, "w")
    outputfp.write(json.dumps(data, sort_keys = True, indent = 4))

if __name__ == '__main__':
  Subreddit('opiates', None)