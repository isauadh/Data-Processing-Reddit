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

def Subreddit(name, limitTo):
  subreddit = reddit.subreddit(name)
  submissions = subreddit.top(limit = limitTo) 
  posts = {}
  
  for submission in submissions:
    flag_sub = 0
    for key in posts.keys():
      if submission.author == key:
        posts[key].append(submission.selftext)
        flag_sub = 1
    if flag_sub == 0:
      posts[str(submission.author)] = []
      posts[str(submission.author)].append(submission.selftext)
    for comment in submission.comments.list():
      flag = 0
      for key in posts.keys():
        if comment.author == key:
          posts[key].append(comment.body)
          flag = 1
          break
      if flag==0:    
        posts[str(comment.author)] = []
        posts[str(comment.author)].append(comment.body)
        
  writeData("{}.txt".format('Sort_Post_By_Author'),posts)
  
if __name__ == '__main__':
  Subreddit('opiates', None)
