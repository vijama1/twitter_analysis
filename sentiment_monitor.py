import tweepy
from textblob import TextBlob
import string
import matplotlib.pyplot as plt
consumer_key='xxxxxx'
consumer_secret='xxxxx'
access_token='xxxx'
access_token_secret='xxxxx'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
remove_punctuation=[]
api=tweepy.API(auth)
user_input=input("Enter what do you want to be searched: ")
tweets=api.search(user_input,count=10)
negative_value=0.0
positive_value=0.0
neg_count=0
pos_count=0
neutral_count=0
for tweet in tweets:
    tblob=TextBlob(tweet.text)
    if tblob.sentiment.polarity<0:
        negative_value+=tblob.sentiment.polarity
        neg_count+=1
    elif tblob.sentiment.polarity>0:
        positive_value+=tblob.sentiment.polarity
        pos_count+=1
    else:
        neutral_count+=1
# print("Positive"+str(pos_count))
# print("Negative"+str(neg_count))
# print("Neutral"+str(neutral_count))
x=['Positive','Negative','Neutral']
y=[pos_count,neg_count,neutral_count]
plt.bar(x,y)
plt.xlabel("Sentiment Name")
plt.ylabel("Sentiment Count")
plt.title("Sentiment analysis for "+str(user_input.upper()))
#plt.plot(x,y)
plt.show()
#print(tweets)
