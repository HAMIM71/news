
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='fd5be06af4a54a958f2456179a66b86e')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='',
category='business',language='en')


# /v2/top-headlines/sources
sources = newsapi.get_sources()

# print(top_headlines['articles'])
article = top_headlines['articles']

information =top_headlines['articles']

subtitle=[]
for value in information:
   subtitle.append(value['title'])

print(subtitle)






