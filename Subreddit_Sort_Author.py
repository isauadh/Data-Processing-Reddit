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
    # check if the submission author already exist as a key in post dict
    for key in posts.keys():
      if submission.author == key:
        posts[key].append(submission.selftext)
        flag_sub = 1
    # create a list for new submission author and append submission text to it
    if flag_sub == 0:
      posts[str(submission.author)] = []
      posts[str(submission.author)].append(submission.selftext)
    submission.comments.replace_more(limit= None)
    for comment in submission.comments.list():
      flag = 0
      # check if the comment author already exist as a key in post dict
      for key in posts.keys():
        if comment.author == key:
          posts[key].append(comment.body)
          flag = 1
          break
      # create a list for new comment author and append comment body to it
      if flag==0:    
        posts[str(comment.author)] = []
        posts[str(comment.author)].append(comment.body)        
  writeData("{}.txt".format('Subreddit_Sort_Author'),posts)
  
if __name__ == '__main__':
  # Please provide the subreddit before running the program. You can change the 'None' limit value as your want.
  Subreddit('Subreddit_Name', None)
