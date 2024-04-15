import tweepy
import time

api_key = "FSUwzH3AJB2KR2l54xDNl3Fgm"
api_secret = "sYJyimeV6D8CDewRaKD2fxoFTBWhtGPHyxVJMMGeky3VS0j3MF"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAAM%2FtQEAAAAADNw9JTcFrAvO9Ryffvg1%2BrKxPe8%3DQDFwb38G3wy0DaG1oyVtOCaPcVoFx9mpj0634QPdHgpoOmC7Pk"
access_token = "1717510317767270400-geMNM1lq13yUozHzMbgVyrwzE7iShv"
access_token_secret = "VPZHmq1CXV1sKk1ZaXXfaavzNtXQQiwSRVH5fmf8ZEyi3"

#connect twitter to bot
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)
    
#to create tweet use client.create_tweet()

#client.create_tweet(text='Hello twitter')




#client.delete_tweet('1779496100505784351')
