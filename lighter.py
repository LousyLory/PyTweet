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
    api = tw.Api(consumer_key='8xEeUqGVTLmyS2f7Y8rOUnQIk',
             consumer_secret='WQemTaZpY9DoMSf1jRlcPVLe5zHBO47gTvNod7BTe8AdKvpntY',
             access_token_key='254519106-PXVDd8F77zdSv7QdhBO7htThNl5Uk95hmO5Fm2ev',
             access_token_secret='SNaQ1LhYg1bf7IH2JVF4cc6gl8IeuuNY6vPuNdQMvPNAu')
    
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