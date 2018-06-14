import tweepy
from textblob import TextBlob
import string
import matplotlib.pyplot as plt
consumer_key='xxxx'
consumer_secret='xxxxx'
access_token='xxxxx'
access_token_secret='xxxx'
while True:
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    remove_punctuation=[]
    api=tweepy.API(auth)
    user_input=input("Enter what do you want to be searched: ")
    tweets=api.search(user_input,count=10)
    number_of_tweets=10
    negative_value_percentage=0.0
    positive_value_percentage=0.0
    neutral_value_percentage=0.0
    positive_value=0.0
    negative_value=0.0
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
    negative_value_percentage=(neg_count/number_of_tweets)*100
    positive_value_percentage=(pos_count/number_of_tweets)*100
    neutral_value_percentage=(neutral_count/number_of_tweets)*100
    # print("Positive"+str(pos_count))
    # print("Negative"+str(neg_count))
    # print("Neutral"+str(neutral_count))
    x=['Positive','Negative','Neutral']
    colors = ['green', 'red', 'yellow']
    y=[pos_count,neg_count,neutral_count]

    #creating a bar plot
    plt.bar(x,y)
    plt.xlabel("Sentiment Name")
    plt.ylabel("Sentiment Count")
    plt.title("Sentiment analysis for "+str(user_input.upper()))
    plt.figure("Figure1")

    #creating a pie chart
    percentage_data=[positive_value_percentage,negative_value_percentage,neutral_value_percentage]
    explode = (0.1, 0, 0)
    plt.pie(percentage_data, explode=explode,labels=x, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("Sentiment analysis for "+str(user_input.upper()))
    plt.figure("Figure2")

    #creating a line plot
    plt.plot(x,y)
    plt.xlabel("Sentiment Name")
    plt.ylabel("Sentiment Count")
    plt.title("Sentiment analysis for "+str(user_input.upper()))

    #showng all th plots altogether
    plt.show()

#print(tweets)
