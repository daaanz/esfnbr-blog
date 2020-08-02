import requests
import tweepy
import time
import os
from os import environ

auth = tweepy.OAuthHandler(environ["CONSUMER_TOKEN"], environ["CONSUMER_SECRET"])
auth.set_access_token(environ["KEY"], environ["SECRET"])
api = tweepy.API(auth)

url = 'https://www.epicgames.com/fortnite/api/blog/getPosts?category=&postsPerPage=1&offset=0&locale=es-ES&rootPageSlug=blog&sessionInvalidated=true'

setDelay = 30

res = requests.get(url).json()
blogArticle = res['blogList'][1]

while 1:
    resNew = requests.get(url).json()
    articleNew = res['blogList'][1]
    if articleNew != blogArticle:
        try:
            title = blogArticle['title']
            description = blogArticle['short']
            link = blogArticle['urlPattern']
            try:
                api.update_status(title + '\n\n' + description + '\n' + 'https://www.epicgames.com/fortnite/' + link)
                print('Se ha publicado en Twitter (esfnbr) ' + title)
                blogArticle = resNew['blogList'][1]
            except:
                print('Error al publicar en Twitter.')
        except:
            print('No se ha detectado alguna de las variables.')










    
