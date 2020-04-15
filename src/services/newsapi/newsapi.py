from newsapi import NewsApiClient
import os

newsapi = NewsApiClient(api_key=os.environ['newsapi_token'])

def getTopBitcoinHeadlines():
    return newsapi.get_top_headlines(sources='bloomberg',language='en')