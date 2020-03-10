# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 11:31:12 2020

@author: fhaou
"""
import gzip
import codecs
import json
import pandas as pd

pd.set_option('display.max_colwidth', -1)
#specify the tweets file path
tweetsPath='data/task1/training/CT20-AR-Train-T1-Tweets.gz'
#specify the tweets' labels path
labelsPath='data/task1/training/CT20-AR-Train-T1-Labels.txt'
#specify the topics descriptipn path
topicsPath='data/task1/training/CT20-AR-Train-Topics.json' 

'''read tweets function return an array of tweets where each tweet is presented as a json object'''
def readTweets():
    #unzip the compressed file of tweets and get each tweet in a json format
    tweetsArr=[]
    with gzip.open(tweetsPath, 'rt',encoding='utf-8') as tweets:
        #read each line in the unzipped file of tweets
        for tweet in tweets:
            #Convert each tweet from String format to a json object
            decoded_data=codecs.decode(tweet.encode(),'utf-8')
            tweet_json = json.loads(decoded_data)
            #print each tweet in a json format
            #print(tweet_json)
            tweetsArr.append(tweet_json)
            #print each tweet text only
            #print(tweet_json['full_text'])
        return tweetsArr 

'''read labels function returns a dataframe with three columns ['topicID','tweetID','label']'''
def readLabels():
    #print("***************************************Tweets Labels****************************************")
    #Read the file
    labels=pd.read_csv(labelsPath,sep='\t',header=None)
    #Convert it to a dataframe and add columns names
    labelsDF=pd.DataFrame(labels)
    labelsDF.columns=['topicID','tweetID','label']
    #print(labelsDF)
    return labelsDF

'''read topics description function returns a dataframe three columns ['topicID','title','description']''' 
def readTopics():
    topicsDesc=[]
    #print("*******************************************Topics description**************************************")
    for line in open(topicsPath,'r',encoding='utf-8'):
        description = json.loads(line)
        topicsDesc.append(description)
        #Convert it to a dataframe and add columns names
        topicsDF=pd.DataFrame(topicsDesc)
        topicsDF.columns=['topicID','title','description']
    #print(topicsDF)
    return topicsDF


if __name__=="__main__":
    tweets=readTweets()
    labels=readLabels()
    topicsDesc=readTopics()     
