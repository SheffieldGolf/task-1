CLEF 2020 - CheckThat! Lab 
Arabic

Description: Arabic Dataset Reader
Release Date: March 9th, 2020

This file describes the functionality of the reader for the Arabic dataset for CheckThat! Lab at CLEF2020
1.	reader_config.py: a configuration file where you specify the paths of the following:
	a.	tweetsPath: path of the compressed tweets file
	b.	labelsPath: path of labels file
	c.	topicsPath: path of the topics json file

2.	CT20-AR_reader.py: main reader. It has the following functions:
	a.	readTweets(): reads the compressed file of the tweets and returns an array of tweets where each tweet is presented as a json object.
	b.	readLabels(): reads the text file containing the labels and returns a dataframe with the following columns ['topicID','tweetID','label']
	c.	readTopics(): reads the json file of the topics description and returns a dataframe with three columns ['topicID','title','description']
3.	To run the code: python CT20-AR_reader.py 
