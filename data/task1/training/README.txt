CLEF 2020 - CheckThat! Lab 
Arabic
Task: Task1 (Claim check-worthiness)
=====================================


Dataset: CT20-AR-Train
Release Date: March 9th, 2020
==============================


Filenames: 	
==========
	CT20-AR-Train-Topics.json
	CT20-AR-Train-T1-Labels.txt
	CT20-AR-Train-T1-Tweets.gz


Dataset Description:
====================
The set contains 3 topics and potentially related tweets and their associated labels for Arabic Task 1.
In addition, we include: the full json object of these tweets. 


Statistics:
===========
3 Training Topics:
  - CT20-AR-05: 500 tweets (120 check-worthy)
  - CT20-AR-10: 500 tweets (62 check-worthy)
  - CT20-AR-19: 500 tweets (276 check-worthy)


Below is the description of each file in the dataset.

- "CT20-AR-Train-Topics.json" a JSON file containing main information on the topics 
Each line contains a JSON object that corresponds to one topic in the following format:
{
  "topicID": String,
  "title": String,
  "description": String
}

- "CT20-AR-Train-T1-Labels.txt" contains training data for Arabic Task 1. 
Each line is of the format: "topicID,tweetID,label" 
where "label" values can be: [1: check-worthy, 0: not check-worthy]

- "CT20-AR-Train-T1-Tweets.gz" contains the json object for each tweet encoded in UTF-8.
Each line contains a JSON object representing one tweet as formatted by Twitter.
The object also includes two extra fields: 
topicID: The ID of the topic the tweet belongs to
crawlingTime: Time at which the tweet was collected from Twitter
