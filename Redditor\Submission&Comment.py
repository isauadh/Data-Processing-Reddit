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

# This function will gather maximun of 1k all time submissions and comments of a redditor on any subreddit
def redditorPost(userID, limitTo):
  redditor = {}
  redditor[userID] = [{}]
  redditor[userID][0]['Post'] = []
  redditor[userID][0]['Comment'] = []
  try:
    submissions = reddit.redditor(userID).submissions.top(limit = limitTo)
    for submission in submissions:
      redditor[userID][0]['Post'].append(submission.selftext)
    comments = reddit.redditor(userID).comments.top(limit = limitTo)
    for comment in comments:
      redditor[userID][0]['Comment'].append(comment.body)   
  except:
    redditor[userID][0]['Post'].append("Page Doesn't Exist Anymore")
    redditor[userID][0]['Comment'].append("Page Doesn't Exist Anymore")
  finally:
    writeData("{}.txt".format(userID),redditor)

# limitToSubreddit will limit the number of submissions to go through in a subreddit
# limitToRedditor will limit the number of submissions and comments to go through in a redditor
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
  # set will get rid of repeated redditors 
  redditors['redditors'] = list(set(redditors['redditors'])) 
  writeData("{}.txt".format('RedditorList'), redditors)
  for user in redditors['redditors']:
    redditorPost(user, limitToRedditor)
  
if __name__ == '__main__':
  # Please provide the subreddit before running the program. You can also make changes to the 'None' limit parameters as your want.
  Subreddit('Subreddit_Name', None, None)
