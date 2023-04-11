import tweepy

# 認証に必要なキーとトークン
API_KEY = 'GbLwuzRw7LX6pl2pV5v6dTVfz'
API_SECRET = 'GwTWLo3dsLcNTBA4p28HDHJ1ZACPTQC5TBvC7R86Snfa5TxfDd'
ACCESS_TOKEN = '750419588156760064-rjYtIWPlipCJapAscJoRhnIWBAe0Wqn'
ACCESS_TOKEN_SECRET = 'i3N6Cc72a0U7KXnDgFow0erYpo3xRiGCMYolG0hA0si69'

# APIの認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# キーワードからツイートを取得
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
