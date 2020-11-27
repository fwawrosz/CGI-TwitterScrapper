# YouTube Video: https://www.youtube.com/watch?v=wlnx-7cm4Gg
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import csv #Import csv
import tweepy as tw
import time
access_token = "1713619092-rNn56braFDEwRLyAGh9IbWZ8BlqaHqEhYtIx5em"
access_token_secret = "pt3Kevia17SPtO2x7BgrVryi57i4S7snP2fciBKrtxxXa"
consumer_key = "YAPz4IkJ57pW1ODjdgJ1htuob"
consumer_secret = "1M4v1J90uONGrH092pDDbx1wSMjgPX194ZkKJ6TZm7PSXHHg8W"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
# Define the search term and the date_since date as variables

search_words= input("Enter a subject ")

date_since = input(" Please indicate the start date of search yyyy-mm-dd ")

x=int(input(" Please indicate the number of tweets recently posted "))
# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(int(x))

tweets
with open('tweets.json', 'a') as f:
        for tweet in tweets:
            json.dump(tweet._json, f)
            f.write('\n')



for tweet in tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(int(x)):               
        csvfile = open('my_scraped_tweets.csv','a')
        csvwriter = csv.writer(csvfile)
        print (tweet.user.screen_name.encode('utf-8'), ':', \
                tweet.created_at, ':', tweet.text.encode('utf-8'), ':location', tweet.user.location)
        csvwriter.writerow([(tweet.user.screen_name.encode('utf-8')),(tweet.created_at),(tweet.text.encode('utf-8'))])
        #time.sleep(1)
##        with open('personal.text', 'a',encoding='utf-8') as json_file:
##                 json.dump(tweet.text, json_file)
##                 json_file.write("\n")
     #   csvwriter.writerow([(tweet.user.screen_name.encode('utf-8')),(tweet.created_at),(tweet.text.encode('utf-8')),(tweet.user.location)])
      #  csvwriter.writerow([(tweet.user.screen_name.encode('utf-8')),(tweet.created_at),(tweet.text.encode('utf-8')),(tweet.user.location)])
	# time.sleep(1)
csvfile.close()
        
