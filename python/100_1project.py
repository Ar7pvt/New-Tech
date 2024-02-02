# the url from news.api  link-- https://newsapi.org/

import requests
import json
import gtts
import playsound

query=input("what type of news you want to see ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-06-18&sortBy=publishedAt&apiKey=c9c82be98cc1455bb01d5f91fb46d7a7"
r=requests.get(url)
news=json.loads(r.text)
# print(news,type(news))


for article in news["articles"]:
    print(article["title"])
    text=article["title"]   #you can take user input also

    sound=gtts.gTTS(text,lang="en")  #you can change language
    sound.save(f"100.1Speech.mp3") 
    playsound.playsound(f"100.1Speech.mp3")
    #print(article["description"])
    print( "-------------------------------------------------------------------------s") 

