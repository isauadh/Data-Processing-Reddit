import praw
import json

reddit = praw.Reddit(client_id='client id', \
                     client_secret='client secret', \
                     user_agent='user agent', \
                     username='isauadh', \
                     password='password')

def Subreddit(name, limitTO):
    print("Subreddit {}".format(name))
    subreddit = reddit.subreddit(name)
    submissions = subreddit.top(limit=limitTO)
    submissionCount = 0
    commentCount = 0
    fcount = 0
    redditData = {}
    redditData[str(subreddit)] = [{}]

    for submission in submissions:
      submissionCount += 1
      submission.comments.replace_more(limit= None)
      redditData[str(subreddit)][0][str(submission.author)] = [{}]
      redditData[str(subreddit)][0][str(submission.author)][0]['Title'] = submission.title
      redditData[str(subreddit)][0][str(submission.author)][0]['Text'] = submission.selftext
      redditData[str(subreddit)][0][str(submission.author)][0]['Comment'] = [{}]

      for comment in submission.comments.list():
        commentCount += 1
        if(not userExistInComments(redditData[str(subreddit)][0][str(submission.author)][0]['Comment'][0], str(comment.author))):
                redditData[str(subreddit)][0][str(submission.author)][0]['Comment'][0][str(comment.author)]= [{}]
        redditData[str(subreddit)][0][str(submission.author)][0]['Comment'][0][str(comment.author)][0][str(comment)] = [{}]
        redditData[str(subreddit)][0][str(submission.author)][0]['Comment'][0][str(comment.author)][0][str(comment)][0]["Comment_Text"] = comment.body


      updateTerminal(submissionCount, commentCount)
      
      # each file holds maximum of 200 submissions
      if(submissionCount % 200 == 0):
        writeData("{}-{}.txt".format(name,fcount),redditData)
        fcount += 1
        redditData = {}
        subreddit = reddit.subreddit(name)
        redditData[str(subreddit)] = [{}]

def userExistInComments(commentList, user):
    if user in commentList:
        return True
    return False

def updateTerminal( subCount, comCount):
    print("Downloaded: {} Submissions".format(subCount))
    print("Downloaded: {} Comments".format(comCount))

def writeData(fp, data):
    outputfp = open(fp, "w")
    outputfp.write(json.dumps(data, sort_keys = True, indent = 4))

if __name__ == '__main__':
  Subreddit('opiates', None)
