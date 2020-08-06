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
blogArticle = res['blogList'][2]

while 1:
    resNew = requests.get(url).json()
    articleNew = res['blogList'][2]
    if resNew != res:
        try:
            print('Cambios detectados.')
            title = articleNew['title']
            description = articleNew['short']
            link = articleNew['urlPattern']
            try:
                api.update_status(title + '\n\n' + description + '\n' + 'https://www.epicgames.com/fortnite/' + link)
                print('Se ha publicado en Twitter (esfnbr) ' + title)
                resNew = requests.get(url).json()
            except:
                print('Error al publicar en Twitter.')
        except:
            print('No se ha detectado alguna de las variables.')
    else:
        print('No se detectan cambios, buscando de nuevo en 30 segundos...')
    
    time.sleep(setDelay)









    
