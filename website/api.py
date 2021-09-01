
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='fd5be06af4a54a958f2456179a66b86e')


top_headlines = newsapi.get_top_headlines(q='',
category='business',language='en')



sources = newsapi.get_sources()


information =top_headlines['articles']
totalresult =top_headlines['totalResults']
title=[]
for value in information:
   title.append(value['title'])

#print(title)


urlimage=[]
for value in information:
   urlimage.append(value['urlToImage'])

#print(urlimage)


url=[]
for value in information:
  url.append(value['url'])

#print(url)

print(top_headlines)