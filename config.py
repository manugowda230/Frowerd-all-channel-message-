import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25929889"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fd980dbd069e0b45d0dec91f7e616bad")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5456381819"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://manugowda2306:manugowda2306@cluster0.ix1rv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "movie King Hub all saver")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
