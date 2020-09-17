import tweepy
import datetime
#Desde la linea 4 a la linea 13 se establece la conexion con la api, autentificandote con las diferentes keys
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
tweettopublish = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

print("just a few more steps to finish this bot")
twitter_API = tweepy.API(auth)
def publictweet(tweettopublish):
    
    twitter_API.update_status(tweettopublish) #Esta linea publica el tweet que le pasamos como parametro
    print(tweettopublish)

#publictweet('Prueba del bot 2 hola chavales como estamos todo bien #Albacete')

def publicartweetSemana():#dependiendo del dia dde la semana que sea datetime.date.today().weekday() devolvera un numero y con esa comprobacion se publicara un tweet o otro
    if datetime.date.today().weekday() == 0:
        tweettopublish = 'Hi everyone, today is Monday.   #Monday '
    if datetime.date.today().weekday() == 1:
        tweettopublish = 'Enjoy your Tuesday.  #Tuesday'
    if datetime.date.today().weekday() == 2:
        tweettopublish = 'Third week of the Week. #Wednesday'
    if datetime.date.today().weekday() == 3:
        tweettopublish = 'Thursday. I cannot wait for the Weekend'
    if datetime.date.today().weekday() == 4:
        tweettopublish = 'Friday...Finally'
    if datetime.date.today().weekday() == 5:
        tweettopublish = 'Great it is Saturday #weekend #Saturday'
    if datetime.date.today().weekday() == 6:
        tweettopublish = 'Sunday morning...#Weekend #enjoy '
    publictweet(tweettopublish)

#publicartweetSemana()

def retweetsomething():#pasandole la id del tweet se retweetea con el .retweet
    twitter_API.retweet(83407830496968704)

retweetsomething()

    