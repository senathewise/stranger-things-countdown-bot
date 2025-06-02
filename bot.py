import datetime
import tweepy

# === API Anahtarlarını BURAYA gir ===
api_key = "API_KEY"
api_secret = "API_SECRET"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"

# Twitter'a bağlan
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Hedef tarih: 26 Kasım 2025
target_date = datetime.date(2025, 11, 26)
today = datetime.date.today()
days_left = (target_date - today).days

# Tweet içeriği
if days_left > 0:
    tweet = f"There’s {days_left} day{'s' if days_left != 1 else ''} left until Stranger Things 5 - Volume 1!"
else:
    tweet = "Stranger Things 5 - Volume 1 is out today! 🧇⚡️"

# Tweet at
api.update_status(tweet)
