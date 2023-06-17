# DOLLARTOLIRA IS A AUTOMATIC TWITTER BOT THAT TWEETS THE CURRENT VALUE OF US DOLLARS IN TURKISH LIRA EVERY DAY.
# IN ORDER TO MAKE THIS BOT FUNCTIONAL, YOU NEED TO DO 2 THINGS:
#   -CHANGE THE TWITTER ACCOUNT DATA IN THE CODE WITH YOUR DATA
#   -HOST THIS PYTHON CODE IN CLOUD AND SET UP A TASK TO RUN IT IN THE INTERVAL YOU WOULD LIKE.
# AUTHOR: EREN GUL


import tweepy
import json
from urllib import request
from urllib.request import Request, urlopen
from datetime import date


def retrieve_rate():
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                             'Mobile/15E148'}
    apiUrl = "http://hasanadiguzel.com.tr/api/kurgetir"
    request_site = Request(apiUrl, headers= HEADERS)
    webpage = urlopen(request_site).read().decode('utf-8')
    getData = json.loads(webpage)
    rawdata = getData["TCMB_AnlikKurBilgileri"]
    good_data = (rawdata[:1][0]['BanknoteBuying'])
    best_data = str(good_data)
    return best_data


def post_tweet(best_data):
    today = date.today()
    today_str = str(today)
    ACCESS_TOKEN = 'YOUR ACCESS TOKEN'
    ACCESS_SECRET = 'YOUR ACCESS SECRET'
    CONSUMER_KEY = 'YOUR CONSUMER KEY'
    CONSUMER_SECRET = 'YOUR CONSUMER SECRET'
    BEARER_TOKEN = 'YOUR BEARER TOKEN'

    api = tweepy.Client(
        bearer_token= BEARER_TOKEN,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET)
    api.create_tweet(text=today_str + "    1 USD = " + best_data + " TRY")


def main():
    a = retrieve_rate()
    post_tweet(a)


main()
