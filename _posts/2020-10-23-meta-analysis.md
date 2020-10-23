---
#Frontmatter
layout: post
title: Meta-Analysis of Research
---

# Description & Method 
I read [Pride, Love, and Twitter Rants: Combining Machine Learning and Qualitative Techniques to Understand What Our Tweets Reveal about Race in the US](https://www.researchgate.net/publication/333231572_Pride_Love_and_Twitter_Rants_Combining_Machine_Learning_and_Qualitative_Techniques_to_Understand_What_Our_Tweets_Reveal_about_Race_in_the_US) published by the International Journal of Environmental Research and Public Health.  The objective of this study is to "describe variation in sentiment of tweets using race-related terms and identify themes charactarizing the social climate related to race". The researchers applied a Stochastic Gradient Descent Classifier, which is an optimization technique that can be used to train machine learning models. In this case, researchers used this method to do a sentiment analysis of 1,249,653 US tweets using race-related terms from 2015 to 2016. To ensure accuracy, a random subset of 6600 tweets were given manual sentiment labels and those labels were compared against computer sentiment labels, acknowledging the subjectivity and spectrum of human sentiment.

# Data 

## Which properties are being tracked?
From March 2015-April 2016, researchers used Twitter's API (Streaming Application Programming Interface) to access a random subset of ~1.25 million tweets. Labeled tweets from Sanders Analytics (5513 tweets) and Kaggle (7086 tweets) and emotions dervied from Sentiment140 were used to train the algorithm researchers used for sentiment analysis. The computer algorithm then categorized the sentiment of the tweets as "positive" or "negative/neutral". Based off of race-related language used in the tweet, they were grouped further into four main racial/ethnic categories: Black, Hispanic, Asian, and Middle Eastern. 

## Which properties are being left out?
They restricted data collection by only analyzing tweets with latitude and longitude coordinates within the United States. Further, tweets with the same "#tweet_id" – every tweet has a distinct id - were removed to rid of duplicates. Finally, tweets that were job postings, which they assumed would include #job and #listing, and came from automated accounts were eliminated from the dataset. 

## Which data points make it to the final dataset?
Tweets within the latitude and longtitude of the United States, were forms of advertisement, or were duplicates were eliminated from the final dataset. Lastly, tweets using at least one or more race-related terms were identified comprising the final dataset of ~1.25 million tweets. In total, 79,848,992 million general topic tweets from 603,363 unique Twitter users were analyzed after these property restrictions were applied. 

## What incentives are driving people to collect this data?
A society in which greater hosilities towards minorities occur has been happening for long in our history as humans. Instances of discrimination are often measured at the individual level by self-report. However, those measures are often influenced by factors such as self-censorship. Although individual level measures or racial bias and discrimination are valuable, assessing social climate can give a broader context of social environment. Social media is a great tool to collect this tyoe of data as it gives people the space and opportunity to publicly express their ideas and sentiment, granting users differing degrees of anonymity. Social media therefore presents some advantages in illuminating national and potentially place-specific sentiments about race/ethnicity, providing a “temperature” of the social environment where the tweets are written.

## How was this data collected?
To prepare the dataset, each tweet was divided into tokens, which roughly corresponded to words, by the Stanford Tokenizer. To conduct sentiment analysis on the tweets, researchers used the Stochastic Gradient Descent Classifier (SGD). Additionally, preprocessing was done to remove inconsquential variation and to allow the model to focus on the tweet itself. Preprocessing steps included removing stop words (ex: the, is, a), additional white space, punctuations, hashtags, URLs, and usernames. All characters were converted to lowercase. The researchers trained sentiment analysis algorithm then categorized tweets as "positive" or "negative/neutral" from the total final sample of ~1.25 million tweets. Then, tweets were grouped into four racial/ethic categories, Black, Hispanic, Asian, and Middle Eastern, according to certain words that were contained in the tweets themselves. 

 ## Who is funding the collection of this data?
Although its unclear who funded this study, professors from University of California San Francisco, Furman University, UC Berkeley, Harvard, University of Maryland, and DePaul University collaborated and published this research together. 

 ## How accessible is this dataset?
This dataset is accessible as it is open to the public through Research Gate.

# Results 


# Analysis 
#Trust
#Publish or Perish