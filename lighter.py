# for the raspberry thingy
from gpiozero import LED, Button
from time import sleep

import numpy as np
import twitter as tw

#Changed_like = False
#Changed_retweet = False
last_like = 0
last_retweet = 0

LED_like = LED(4)
LED_retweet = LED(5)

while(1):
    api = tw.Api(consumer_key='MKEVTqMVBmrjNEqKztBV4lJ7n',
             consumer_secret='UKUd8JFqs8ThlBNR1u0FfL9X88xIPfJbaSNHFI2j3fBmPiZ3ks',
             access_token_key='927046369445076992-aQaF0Ue1FwYdAuxWpnAOMhKD3XAu0A5',
             access_token_secret='W8HFctZoKSExssa24KU2Jxr62jZTLg9Eep2WrFE2m95Gi')
    
    G = api.VerifyCredentials()
    G1 = api.GetStatus(G.status.id)
    
    # count likes
    if G1._json['favorite_count'] > last_like:
        last_like = G1._json['favorite_count']
        # print('Changed_like')
        LED_like.on()
        sleep(2)
    elif G1._json['favorite_count'] < last_like:
        last_like = G1._json['favorite_count']
    
    # count retweets
    if G1._json['retweet_count'] > last_retweet:
        last_retweet = G1._json['retweet_count']
        # print('Changed_retweet')
        LED_retweet.on()
        sleep(2)
    elif G1._json['retweet_count'] < last_retweet:
        last_retweet = G1._json['retweet_count']
    
    LED_like.off()
    LED_retweet.off()
    sleep(8);
