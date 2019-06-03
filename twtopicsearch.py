import tweepy
import numpy as np
import pandas as pd

#Autenticación
auth = tweepy.OAuthHandler("SBNFOrTshjdEyJDipnAP8bI2J", "OHNUkHtQaz3nUdiL4fcEei9xJqnNiCffgDxQ1nKrfrnSA011em")
auth.set_access_token("131081886-LEsmXtVCzXiH8d0Gt9DO6QhhJwyonKWk6kxUgv0j", "jH96tfoGbP4fvcDRZrLPwYvkQh46YdAGYVKdUzo98RDsL")
api = tweepy.API(auth)

#Definición de búsqueda y resultados mostrados.

#Los atributos que se pueden mostrar son:
# id, created_at, text, user, entities, extended_entities, place, source, in_reply_to_status_id,
#coordinates, is_quote_status, retweeted_status, quote_count, retweet_count, favorite_count, entities,
#extended_entities, lang, 

#También pueden ser los atributos de los usuarios como: name, screen_name, location, url, description,
#followers_count, friends_count, favourites_count, statuses_count, created_at, 
#profile_image_url_https

#generar dataframe vacío
df = pd.DataFrame(columns = ['Tweets', 'User', 'User_statuses_count', 'user_followers', 'User_location', 'User_verified', 'fav_count', 'rt_count', 'tweet_date', 'url', 'retweeted'])

def stream(data, file_name):
	i = 0
	for tweet in tweepy.Cursor(api.search, q = data, count = 100, lang='es', place='mexico').items():
		print(i, end='\r')
		df.loc[i,'Tweets'] = tweet.text
		df.loc[i,'User'] = tweet.user.name
		df.loc[i,'User_statuses_count'] = tweet.user.statuses_count
		df.loc[i,'user_followers'] = tweet.user.followers_count
		df.loc[i,'User_location'] = tweet.user.location
		df.loc[i,'User_verified'] = tweet.user.verified
		df.loc[i,'fav_count'] = tweet.favorite_count
		df.loc[i,'rt_count'] = tweet.retweet_count
		df.loc[i,'tweet_date'] = tweet.created_at
		df.loc[i,'url'] = tweet.user.url
		df.to_excel('{}.xlsx'.format(file_name))
		i+=1
		if i ==100:
			break
		else:
			pass

#llamado de la función asignando nombre y criterios buscados
stream(data = ['BBVA'], file_name = 'bbva201906031212')


