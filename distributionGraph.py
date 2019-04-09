import praw
import json
import os
import datetime
import random
import string
import pandas as pd
from dateutil.parser import parse

reddit = praw.Reddit(client_id='IFHDQg4dnEQ2AA', \
                     client_secret='bVZAdZRh6XPPn6G0R-kChVsoEMo', \
                     user_agent='tangocharlie1', \
                     username='isauadh', \
                     password='s@ugaT1320')

def writeData(fp, data):
  outputfp = open(fp, "w")
  outputfp.write(json.dumps(data, sort_keys = True, indent = 4))
    
def hideUserid(name):
  s = list(name)
  length = len(name)
  s[int(length/2)] = random.choice(string.ascii_lowercase)
  s[0] = random.choice(string.ascii_lowercase)
  s[1] = random.choice(string.ascii_lowercase)
  s[(length-1)] = random.choice(string.ascii_lowercase)
  s[(length-2)] = random.choice(string.ascii_lowercase)
  return ("".join(s))

def makeDir(name, data):
  os.mkdir(name)
  #writeData("{}.txt".format(os.path.join(name, name)), data)
  for key in data.keys():
    writeData("{}.txt".format(os.path.join(name, hideUserid(key))), data[key])
    #writeData("{}.txt".format(os.path.join(name, key)), data[key])

def createDistribution(data):
    graphingData = {}
    for key in data.keys():
        graphingData[key] = len(data[key][0]['post'])
    df = pd.DataFrame.from_dict(graphingData, orient = 'index', columns = ['count'])
    #bins = [0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80]
    df['binned'] = pd.cut(df['count'], bins = 150)
    print(df['binned'].value_counts().plot.bar())

def timeDistribution(authorName, data):
    graphingData = {}
    graphingData[authorName] = []
    for i in range(0,len(data[authorName][0]['postTime'])):
        time = parse(str(datetime.datetime.fromtimestamp(data[authorName][0]['postTime'][i])))
        graphingData[authorName].append(time.hour)
    df1 = pd.DataFrame.from_dict(graphingData) 
    bins = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    df1['binned'] = pd.cut(df1[authorName], bins = bins)
    print(df1['binned'].value_counts().plot.bar())

def Subreddit(name, limitTo):
      count = 0
      redditors = {}
      subreddit = reddit.subreddit(name)
      submissions = subreddit.top(limit = limitTo)
      for submission in submissions:
        print(count)
        flag_sub = 0
        for key in redditors.keys():
          if submission.author == key:
            redditors[key][0]['post'].append(submission.selftext)
            redditors[key][0]['postTime'].append(submission.created)
            flag_sub = 1
        if flag_sub == 0:
          redditors[str(submission.author)] = [{}]
          redditors[str(submission.author)][0]['post'] = []
          redditors[str(submission.author)][0]['postTime'] = []
          redditors[str(submission.author)][0]['post'].append(submission.selftext)
          redditors[str(submission.author)][0]['postTime'].append(submission.created)    
        submission.comments.replace_more(limit= None)
        for comment in submission.comments.list():
          flag = 0
          for key in redditors.keys():
            if comment.author == key:  
              redditors[key][0]['post'].append(comment.body)
              redditors[key][0]['postTime'].append(comment.created_utc)
              flag = 1
              break
          if flag==0:    
            redditors[str(comment.author)] = [{}]
            redditors[str(comment.author)][0]['post'] = []
            redditors[str(comment.author)][0]['postTime'] = []
            redditors[str(comment.author)][0]['post'].append(comment.body)
            redditors[str(comment.author)][0]['postTime'].append(comment.created_utc)
        count += 1
      print("Done..")
      makeDir(name, redditors)
      return redditors
    
if __name__ == '__main__':
  allPost = Subreddit('OpiatesRecovery', None)
  while(True):
    User = input("Time distribution of the user: ")
    timeDistribution(User, allPost)
    proceed = input("Press 'y' to view more time distribution or 'n' to stop: ")
    if proceed == y:
      continue
    else:
      break
