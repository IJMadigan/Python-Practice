import json
import tweepy
import random

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

def lambda_handler(event, context):
    create_tweet()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    # -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:49:04 2021

@author: madig
"""

def create_tweet(): 
# Authenticate to Twitter
# TODO: REMOVE THESE SECURITY CONCERNS
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    
    #pick a random line
    def random_line(fname):
        lines = open(fname).read().splitlines()
        return random.choice(lines)
    
    #write Log file
    def write_log(username, message):
        w = open('logfile.txt','a')
        w.write('Wrote message to {}, with message of {}\n'.format(username, message))
        w.close()
        
    def error_log(username,message):
        w = open('logfile.txt','a')
        w.write('ERROR: COULD NOT WRITE to {}, with message of {}\n'.format(username, message))
        w.close()
        
    
    
    #FIND MOST RECENT TWEET.
    recent = api.user_timeline(count = 1)
    #api.get_user to find mentions. 
    
    statuses = api.mentions_timeline(since_id = recent[0].id) 
    
    
    for mention in statuses:
        reply = mention.user.screen_name
        compliment = random_line('compliments.txt')
        print( mention.user.screen_name)
        print( mention.user.name)
        print(str(len(statuses)) + " number of statuses have been mentioned.") 
        # Create a tweet
        try:
            print('begining of try')
            api.update_status(status = '@{} \n {}'.format(reply,compliment))
            write_log(reply,compliment)
            print('end of try')
        except:
            print('Errored out.')
            error_log(reply,compliment)
        
        
    





