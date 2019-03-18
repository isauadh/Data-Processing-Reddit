import praw
import json

reddit = praw.Reddit(client_id='', \
                     client_secret='', \
                     user_agent='', \
                     username='isauadh', \
                     password='')

def writeData(fp, data):
    outputfp = open(fp, "w")
    outputfp.write(json.dumps(data, sort_keys = True, indent = 4))

def redditorPost(userID, limitTo):
  redditorPost = {}
  redditorPost[userID] = []
  try:
    submissions = reddit.redditor(userID).submissions.top(limit = limitTo)
    for submission in submissions:
      redditorPost[userID].append(submission.selftext)
  except:
    redditorPost[userID].append("404 Error")
  finally:
    writeData("{}.txt".format(userID),redditorPost)

def Subreddit(name, limitToSubreddit, limitToRedditor):
  subreddit = reddit.subreddit(name)
  submissions = subreddit.top(limit = limitToSubreddit)
  redditors = {}
  redditors['redditors'] = []
 
  for submission in submissions:
    submission.comments.replace_more(limit= limitToSubreddit)
    redditors['redditors'].append(str(submission.author))
    for comment in submission.comments.list():
      redditors['redditors'].append(str(comment.author))
  # get rid of repeated redditor
  redditors['redditors'] = list(set(redditors['redditors']))
   
  for user in redditors['redditors']:
    print("Submissions of : " + user)
    redditorPost(user, limitToRedditor)
  
if __name__ == '__main__':
  Subreddit('opiates', None, None)
