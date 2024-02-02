
# import win32com.client

# speaker= win32com.client.Dispatch("SAPI.spVoice")

# while 1:
#     print("Enter the text to speech")
#     s=input()
#     speaker.Speak(s)

# news in loop
import requests
import json
import win32com.client

speaker= win32com.client.Dispatch("SAPI.spVoice")


query=input("what type of news you want to see ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-07-16&sortBy=publishedAt&apiKey=c9c82be98cc1455bb01d5f91fb46d7a7"
r=requests.get(url)
news=json.loads(r.text)
# print(news,type(news))


for article in news["articles"]:
    print(article["title"])
    text=article["title"]   #you can take user input also

    s=text
    speaker.Speak(s)
    #print(article["description"])
    print( "-------------------------------------------------------------------------s") 
