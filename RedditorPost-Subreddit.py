import praw
import json

reddit = praw.Reddit(client_id='IFHDQg4dnEQ2AA', \
                     client_secret='bVZAdZRh6XPPn6G0R-kChVsoEMo', \
                     user_agent='tangocharlie1', \
                     username='isauadh', \
                     password='s@ugaT1320')

def writeData(fp, data):
    outputfp = open(fp, "w")
    outputfp.write(json.dumps(data, sort_keys = True, indent = 4))

def get_posts(userID):
  redditorPost = {}
  redditorPost[userID] = []
  try:
    submissions = reddit.redditor(userID).submissions.top(limit = 1)
    for submission in submissions:
      redditorPost[userID].append(submission.selftext)
  except:
    redditorPost[userID].append("404 Error")
  finally:
    writeData("{}.txt".format(user),redditorPost)

subreddit = reddit.subreddit('opiates')
submissions = subreddit.top(limit = 1)
redditorList = {}
redditorList['redditors'] = []
commenterList = {}
commenterList['commenters'] = []

for submission in submissions:
  submission.comments.replace_more(limit= None)
  redditorList['redditors'].append(str(submission.author))
  for comment in submission.comments.list():
    commenterList['commenters'].append(str(comment.author))
 

newRedditorList = []
newRedditorList = redditorList['redditors'] + commenterList['commenters']
totalRedditorList = list(set(newRedditorList))
redditorList['redditors'] = totalRedditorList
writeData("{}.txt".format('Redditor'),redditorList)

print(len(redditorList['redditors']))
print(len(commenterList['commenters']))  
print(len(newRedditorList))  
print(len(totalRedditorList)) 
for user in redditorList['redditors']:
  print("Getting posts of user: " + user)
  get_posts(user)
