import requests

url = "https://newscatcher.p.rapidapi.com/v1/search_free"

querystring = {"q":"Tech","lang":"en","media":"True"}

headers = {
    'x-rapidapi-host': "newscatcher.p.rapidapi.com",
    'x-rapidapi-key': "aa7d5b2040msh540baa70a08acf4p191b9ajsn6675cbccb263"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)