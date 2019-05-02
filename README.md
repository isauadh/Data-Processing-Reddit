# Data -Processing-RedditAPI

The project uses reddit API to collect data from subreddit 'Opiates' for the purpose to study addiction and recovery.

## Crawler.py

The crawler program collects maximun of top 1k of all time submissions and comments off the given subreddit.

## Redditor\Submission&Comment.py

First, this program collects redditors on a given subreddit. Second, the program iterates through the list of redditors and gather their all time top submission and comments (maximum of 1k) on any subreddit throughout reddit.com.

## Subreddit_Sort_Author.py

This program goes through submissions and comments on a subreddit and sort them by redditor(Author).

## distributionGraph.py

This program will generate a distribution graph of the number of post in a given subreddit. Also, can generate time distribution of a redditor post in a given subreddit. 

The program will create a directory with files containing submissions and comments of a redditor in a given subreddit. Filename will be the hidden version of the original redditor name.

## Opiates.Zip

The folder has been zipped because it consists files more than the GitHub Limit. This folder consists of three different files. The first CSV folder consists of a csv file for each redditor under the second Opiates folder. The run.py is a python program that parses through the opiates folder to create a csv folder. The csv folder contains filename as numbers to hide redditor name. The index can be found in index_dict under csv folder.

## Authors

Saugat Adhikari

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

