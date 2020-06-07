import oauth2
import urllib.parse
import json

class Twitter:

    def __init__(self, consumerKey, consumerSecret, tokenKey, tokenSecret):
        self.conexao(consumerKey, consumerSecret, tokenKey, tokenSecret)

    def conexao(self, consumerKey, consumerSecret, tokenKey, tokenSecret):
        self.consumer = oauth2.Consumer(consumerKey, consumerSecret)
        self.token = oauth2.Token(tokenKey, tokenSecret)
        self.cliente = oauth2.Client(self.consumer, self.token)

    def tweet(self, novoTweet):
        queryCodificada = urllib.parse.quote(novoTweet, safe='')
        req = self.cliente.request(f'https://api.twitter.com/1.1/statuses/update.json?status={queryCodificada}', method="POST")
        decodificar = req[1].decode()
        objeto = json.loads(decodificar)
        return objeto

    def search(self, query, lang):
        queryCodificada = urllib.parse.quote(query, safe='')
        req = self.cliente.request(f'https://api.twitter.com/1.1/search/tweets.json?q={queryCodificada}&lang={lang}')

        decodificar = req[1].decode()

        objeto = json.loads(decodificar)
        twittes = objeto['statuses']
        return twittes